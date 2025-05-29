from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from datetime import timedelta
import logging

from .registers import REGISTER_DEFINITIONS, ALARM_REGISTER_BASE, ALARM_REGISTER_COUNT, ALARM_TEXTS
from .base_sensor import ModbusConnector, KwbSensorBase, KwbAlarmSensorBase
from .const import DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    ip = entry.data.get("ip_address")
    port = entry.data.get("port")

    try:
        modbus = ModbusConnector(ip, port)
    except Exception as e:
        _LOGGER.error("Modbus-Verbindungsfehler: %s", e)
        return

    async def async_update_data():
        def read_all():
            data = {}

            for name, definition in REGISTER_DEFINITIONS.items():
                try:
                    result = modbus.read_register(address=definition["address"], count=1)
                    if result.isError():
                        _LOGGER.warning("Modbus-Fehler bei %s (Adresse %s)", name, definition["address"])
                        data[name] = None
                    else:
                        raw = result.registers[0]
                        dtype = definition["type"]
                        scale = definition["scale"]

                        if dtype == "float":
                            value = round(raw * scale, 2)
                        elif dtype == "status":
                            value = int(raw)
                        else:
                            value = int(raw * scale)

                        data[name] = value
                except Exception as e:
                    _LOGGER.error("Fehler beim Lesen von %s: %s", name, e)
                    data[name] = None

            # Alarme lesen
            try:
                result = modbus.read_register(address=ALARM_REGISTER_BASE, count=ALARM_REGISTER_COUNT)
                alarms = []
                if not result.isError():
                    for i, reg in enumerate(result.registers):
                        for bit in range(16):
                            if reg & (1 << bit):
                                alarm_id = 1000 + (i * 16 + bit)
                                alarms.append(ALARM_TEXTS.get(alarm_id, f"Alarm {alarm_id}"))
                data["alarms"] = alarms
            except Exception as e:
                _LOGGER.error("Fehler beim Lesen der Alarme: %s", e)
                data["alarms"] = []

            return data

        return await hass.async_add_executor_job(read_all)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="kwb_tcp",
        update_method=async_update_data,
        update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
    )

    await coordinator.async_config_entry_first_refresh()

    sensors = [
        KwbSensorBase(coordinator, name, definition, entry)
        for name, definition in REGISTER_DEFINITIONS.items()
        if not (
            definition.get("writable") and
            definition.get("type") == "status" and
            "value_map" in definition
        )
    ]
    sensors.append(KwbAlarmSensorBase(coordinator, ALARM_TEXTS))
    async_add_entities(sensors)

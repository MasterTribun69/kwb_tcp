from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from datetime import timedelta
from .base_sensor import ModbusConnector
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL
from .registers import REGISTER_DEFINITIONS
import logging

_LOGGER = logging.getLogger(__name__)

async def create_coordinator(hass, entry):
    ip = entry.data.get("ip_address")
    port = entry.data.get("port")
    modbus = ModbusConnector(ip, port)

    async def async_update_data():
        def read_all():
            data = {}
            for name, definition in REGISTER_DEFINITIONS.items():
                try:
                    result = modbus.read_register(address=definition["address"], count=1)
                    if result.isError():
                        data[name] = None
                    else:
                        raw = result.registers[0]
                        invalid_values = definition.get("invalid_values")
                        if invalid_values and raw in invalid_values:
                            data[name] = None
                            continue
                        dtype = definition["type"]
                        scale = definition["scale"]
                        if dtype == "float":
                            value = round(raw * scale, 2)
                        elif dtype == "status":
                            value = int(raw)
                        else:
                            value = int(raw * scale)
                        data[name] = value
                except Exception:
                    data[name] = None
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
    return coordinator
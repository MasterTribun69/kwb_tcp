# base_sensor.py

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity
from pymodbus.client import ModbusTcpClient
import logging
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)

TEMP_CELSIUS = "°C"

class ModbusConnector:
    def __init__(self, ip: str, port: int):
        self.client = ModbusTcpClient(host=ip, port=port)
        if not self.client.connect():
            raise ConnectionError(f"Modbus-Verbindung fehlgeschlagen: {ip}:{port}")

    def read_register(self, address, count=1):
        return self.client.read_holding_registers(address=address, count=count)

class KwbSensorBase(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, name, definition, entry):
        super().__init__(coordinator)
        self._name = name
        self._definition = definition
        self._address = definition["address"]
        self._type = definition["type"]
        self._scale = definition["scale"]
        self._unit = definition["unit"]
        self._description = definition["description"]
        self._attr_unique_id = f"kwb_{self._address}"
        self._attr_native_unit_of_measurement = self._unit
        self._attr_config_entry_id = entry.entry_id

    @property
    def name(self):
        return f"KWB {self._name}"

    @property
    def native_value(self):
        val = self.coordinator.data.get(self._name)
        if self._type == "status":
            if "value_map" in self._definition:
                return self._definition["value_map"].get(val, str(val))
            return "Ein" if val == 1 else "Aus"
        return val

    @property
    def extra_state_attributes(self):
        attrs = {"Beschreibung": self._description}
        if self._type == "status":
            val = self.coordinator.data.get(self._name)
            if val is not None:
                if "value_map" in self._definition:
                    attrs["Status Info"] = self._definition["value_map"].get(val, str(val))
                else:
                    attrs["Status Info"] = "Ein" if val == 1 else "Aus"
        return attrs
    
    @property
    def device_info(self):
        return {
            "identifiers": {(self._attr_config_entry_id, "kwb_heizung")},
            "name": "KWB Heizung",
            "manufacturer": "KWB",
            "model": "Modbus TCP",
            "configuration_url": None
        }

class KwbAlarmSensorBase(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, alarm_texts):
        super().__init__(coordinator)
        self._alarm_texts = alarm_texts
        self._attr_unique_id = "kwb_alarme"

    @property
    def name(self):
        return "KWB Alarme"

    @property
    def native_value(self):
        return "Alarm" if self.coordinator.data.get("alarms") else "OK"

    @property
    def extra_state_attributes(self):
        return {"aktive_alarme": self.coordinator.data.get("alarms", [])}
    

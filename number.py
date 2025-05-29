from homeassistant.components.number import NumberEntity
from .const import DOMAIN
from .registers import REGISTER_DEFINITIONS
from .base_sensor import ModbusConnector

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip = config_entry.data.get("ip_address")
    port = config_entry.data.get("port")
    modbus = ModbusConnector(ip, port)

    entities = []
    for name, definition in REGISTER_DEFINITIONS.items():
        if (
            definition.get("writable")
            and definition["type"] in ["int", "float"]
            and "value_map" not in definition
        ):
            entities.append(KwbNumberEntity(name, definition, modbus))

    async_add_entities(entities)


class KwbNumberEntity(NumberEntity):
    def __init__(self, name, definition, modbus):
        self._name = name
        self._address = definition["address"]
        self._scale = definition.get("scale", 1.0)
        self._unit = definition.get("unit")
        self._modbus = modbus
        self._value = None

        self._attr_name = f"KWB {name}"
        self._attr_unique_id = f"kwb_{self._address}_number"
        self._attr_native_unit_of_measurement = self._unit
        self._attr_min_value = definition.get("min", 0)
        self._attr_max_value = definition.get("max", 100)
        self._attr_step = definition.get("step", 1 if self._scale >= 1.0 else 0.1)

    @property
    def native_value(self):
        result = self._modbus.read_register(self._address)
        if result.isError():
            return None
        raw = result.registers[0]
        self._value = round(raw * self._scale, 2)
        return self._value

    async def async_set_native_value(self, value: float) -> None:
        raw = int(round(value / self._scale))
        self._modbus.client.write_register(address=self._address, value=raw)
        self._value = value
        self.async_write_ha_state()

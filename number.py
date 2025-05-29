from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from typing import Any
import logging

from .const import DOMAIN
from .registers import REGISTER_DEFINITIONS
from .base_sensor import KwbSensorBase, ModbusConnector

_LOGGER = logging.getLogger(__name__)


class KwbNumberEntity(KwbSensorBase, NumberEntity):
    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        name: str,
        definition: dict,
        entry: ConfigEntry
    ):
        super().__init__(coordinator, name, definition, entry)
        self._address = definition["address"]
        self._scale = definition.get("scale", 1.0)
        self._unit = definition.get("unit")
        self._min = definition.get("min", 0)
        self._max = definition.get("max", 100)

        self._attr_native_min_value = self._min
        self._attr_native_max_value = self._max
        self._attr_native_step = 1 if self._scale >= 1.0 else 0.1
        self._attr_native_unit_of_measurement = self._unit

    @property
    def native_value(self) -> float | None:
        value = self.coordinator.data.get(self._name)
        return round(value, 2) if value is not None else None

    async def async_set_native_value(self, value: float) -> None:
        raw_value = int(round(value / self._scale))
        ip = self.coordinator.config_entry.data.get("ip_address")
        port = self.coordinator.config_entry.data.get("port")

        try:
            modbus = ModbusConnector(ip, port)
            result = modbus.client.write_register(address=self._address, value=raw_value)
            if result.isError():
                _LOGGER.error("Schreibfehler bei %s (%s)", self._name, self._address)
            else:
                _LOGGER.info("Wert %s erfolgreich auf %s geschrieben (skaliert: %s)", self._name, value, raw_value)
                self.coordinator.data[self._name] = value
                self.async_write_ha_state()
        except Exception as e:
            _LOGGER.exception("Modbus-Fehler beim Schreiben in %s: %s", self._name, e)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]
    numbers = []

    for name, definition in REGISTER_DEFINITIONS.items():
        if definition.get("writable") and definition.get("type") in ("int", "float"):
            numbers.append(KwbNumberEntity(coordinator, name, definition, entry))

    if numbers:
        async_add_entities(numbers)

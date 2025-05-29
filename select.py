from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from typing import Any
import logging

from .const import DOMAIN
from .registers import REGISTER_DEFINITIONS
from .base_sensor import ModbusConnector, KwbSensorBase

_LOGGER = logging.getLogger(__name__)


class KwbSelectEntity(KwbSensorBase, SelectEntity):
    _attr_device_class = "enum"  # Für Dropdown

    def __init__(self, coordinator: DataUpdateCoordinator, name: str, definition: dict, entry: ConfigEntry):
        super().__init__(coordinator, name, definition, entry)
        self._address = definition["address"]
        self._scale = definition.get("scale", 1.0)
        self._value_map = definition["value_map"]
        self._reverse_map = {v: k for k, v in self._value_map.items()}
        self._attr_options = list(self._reverse_map.keys())

    @property
    def current_option(self) -> str | None:
        value = self.coordinator.data.get(self._name)
        return self._value_map.get(value, None)

    async def async_select_option(self, option: str) -> None:
        value = self._reverse_map.get(option)
        if value is None:
            _LOGGER.error("Ungültige Option '%s' für %s", option, self._name)
            return

        ip = self.coordinator.config_entry.data.get("ip_address")
        port = self.coordinator.config_entry.data.get("port")

        try:
            modbus = ModbusConnector(ip, port)
            result = modbus.client.write_register(address=self._address, value=value)
            if result.isError():
                _LOGGER.error("Fehler beim Schreiben von %s auf %s", value, self._name)
            else:
                _LOGGER.info("%s erfolgreich auf %s (%s) gesetzt", self._name, option, value)
                self.coordinator.data[self._name] = value
                self.async_write_ha_state()
        except Exception as e:
            _LOGGER.exception("Modbus-Schreibfehler bei %s: %s", self._name, e)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]

    selects = []
    for name, definition in REGISTER_DEFINITIONS.items():
        if (
            definition.get("type") == "status"
            and definition.get("writable")
            and "value_map" in definition
        ):
            selects.append(KwbSelectEntity(coordinator, name, definition, entry))

    if selects:
        async_add_entities(selects)

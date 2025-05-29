from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from typing import Any

import logging

from .base_sensor import KwbSensorBase, ModbusConnector
from .const import DOMAIN
from .registers import REGISTER_DEFINITIONS

_LOGGER = logging.getLogger(__name__)


class KwbSelectEntity(KwbSensorBase, SelectEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, name: str, definition: dict):
        super().__init__(coordinator, name, definition)

        self._value_map = definition.get("value_map", {})
        self._reverse_map = {v: k for k, v in self._value_map.items()}
        self._address = definition["address"]

        self._attr_name = f"KWB {name}"
        self._attr_unique_id = f"kwb_{self._address}_select"
        self._attr_device_class = "enum"

    @property
    def current_option(self) -> str | None:
        value = self.coordinator.data.get(self._name)
        return self._value_map.get(value)

    @property
    def options(self) -> list[str]:
        return list(self._reverse_map.keys())

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
                _LOGGER.info("%s erfolgreich gesetzt auf %s (%s)", self._name, option, value)
                self.coordinator.data[self._name] = value
                self.async_write_ha_state()
        except Exception as e:
            _LOGGER.exception("Fehler beim Schreiben in Register: %s", e)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]["coordinator"]

    selects = []
    for name, definition in REGISTER_DEFINITIONS.items():
        if (
            definition.get("type") == "status"
            and definition.get("writable") is True
            and "value_map" in definition
        ):
            selects.append(KwbSelectEntity(coordinator, name, definition))

    if selects:
        async_add_entities(selects)

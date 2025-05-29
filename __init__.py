from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "kwb_tcp"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    try:
        unloaded = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
        return unloaded
    except Exception as e:
        import logging
        _LOGGER = logging.getLogger(__name__)
        _LOGGER.error("Fehler beim Entladen der KWB TCP Integration: %s", e)
        return False
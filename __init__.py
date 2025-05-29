from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
import voluptuous as vol
import logging

from .registers import REGISTER_DEFINITIONS
from .base_sensor import ModbusConnector
from .coordinator import create_coordinator

DOMAIN = "kwb_tcp"
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    coordinator = await create_coordinator(hass, entry)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "coordinator": coordinator
    }

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor", "number", "select"])

    hass.services.async_register(
        DOMAIN,
        "write_register",
        lambda call: handle_write_register(hass, call, entry),
        schema=vol.Schema({
            vol.Required("register_name"): str,
            vol.Required("value"): vol.Coerce(float),
        }),
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    try:
        unloaded = await hass.config_entries.async_forward_entry_unload(entry, ["sensor", "number", "select"])
        if entry.entry_id in hass.data[DOMAIN]:
            hass.data[DOMAIN].pop(entry.entry_id)
        return unloaded
    except Exception as e:
        _LOGGER.error("Fehler beim Entladen der KWB TCP Integration: %s", e)
        return False

def handle_write_register(hass, call, entry):
    register_name = call.data["register_name"]
    value = call.data["value"]

    if register_name not in REGISTER_DEFINITIONS:
        _LOGGER.error("Unbekanntes Register: %s", register_name)
        return

    definition = REGISTER_DEFINITIONS[register_name]
    if not definition.get("writable"):
        _LOGGER.warning("Register %s ist nicht beschreibbar!", register_name)
        return

    address = definition["address"]
    scale = definition["scale"]
    raw_value = int(round(value / scale))

    ip = entry.data.get("ip_address")
    port = entry.data.get("port")

    try:
        modbus = ModbusConnector(ip, port)
        result = modbus.client.write_register(address=address, value=raw_value)
        if result.isError():
            _LOGGER.error("Fehler beim Schreiben in Register %s (Adresse %s)", register_name, address)
        else:
            _LOGGER.info("Register %s erfolgreich geschrieben: %s (skaliert: %s)", register_name, value, raw_value)
    except Exception as e:
        _LOGGER.exception("Modbus-Schreibfehler: %s", e)
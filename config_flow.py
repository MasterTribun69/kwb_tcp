# config_flow.py

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import area_registry as ar
from homeassistant.const import CONF_IP_ADDRESS, CONF_PORT
from .const import DOMAIN

class KwbTcpConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="KWB Heizung", data=user_input)

        area_registry = ar.async_get(self.hass)
        areas = {area.id: area.name for area in area_registry.async_list_areas()}

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Required(CONF_PORT, default=502): int,
                vol.Optional("area_id"): vol.In(areas),
            }),
            errors=errors,
        )
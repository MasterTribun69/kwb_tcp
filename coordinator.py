from datetime import timedelta
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


class KwbDataCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, update_method):
        super().__init__(
            hass,
            _LOGGER,
            name="KWB TCP Coordinator",
            update_method=update_method,
            update_interval=timedelta(seconds=30),  # Intervall für automatische Aktualisierung
        )

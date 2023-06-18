"""Entry point for the devices_api component."""

from __future__ import annotations
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .constants import DOMAIN, CONFIG, YAML_CONFIG
from .configuration import Configuration
from .router import (
    Router,
    DevicesAPIDevicesListView,
    DevicesAPIDeviceInformationView,
    DevicesAPIAreasListView,
    DevicesAPIAreaInformationView,
    DevicesAPIAreaDevicesListView,
)


# Initializes the component
def setup(hass: HomeAssistant, configuration: ConfigType) -> bool:
    """Perform the setup for devices_api component."""
    _initialize_configuration(hass, configuration)
    _register_routes(hass)
    return True


# Initializes the configuration of the component
def _initialize_configuration(hass: HomeAssistant, configuration: ConfigType) -> None:
    """Initialize the configuration of the component."""
    hass.data[DOMAIN] = {}
    hass.data[DOMAIN][CONFIG] = Configuration.from_any(configuration[DOMAIN])
    hass.data[DOMAIN][YAML_CONFIG] = configuration


# Registers all available routes of the component
def _register_routes(hass: HomeAssistant) -> None:
    router = Router(hass)
    router.add_routes(
        [
            DevicesAPIAreasListView(),
            DevicesAPIAreaInformationView(),
            DevicesAPIDevicesListView(),
            DevicesAPIDeviceInformationView(),
            DevicesAPIAreaDevicesListView(),
        ]
    )
    router.register()

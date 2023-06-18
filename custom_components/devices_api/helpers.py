"""Helpers for the Devices API component."""

from __future__ import annotations
from typing import List, Dict, Any
from homeassistant.core import HomeAssistant
from aiohttp.web import Request
from .constants import DOMAIN, CONFIG
from .configuration import Configuration
from .manager import AreaManager, DeviceManager


# Builds the view name for the endpoint
def build_view_name(endpoint_name: str) -> str:
    """Build the view name for the endpoint."""
    prefix = f"api:{DOMAIN}"
    endpoint_name = endpoint_name.strip()

    if endpoint_name == "":
        return prefix
    return f"{prefix}:{endpoint_name}"


# Builds the URL for the endpoint
def build_url(endpoint_name: str, has_placeholder: bool = False) -> str:
    """Build the URL for the endpoint."""
    prefix = f"/api/{DOMAIN}"
    endpoint_name = endpoint_name.strip()

    if endpoint_name == "":
        return prefix

    if not has_placeholder:
        return f"{prefix}/{endpoint_name}"
    else:
        return prefix + "/" + endpoint_name


# Returns the HomeAssistant instance from the Request object
def get_hass_from_request(request: Request) -> HomeAssistant:
    """Return the HomeAssistant instance from the Request object."""
    return request.app["hass"]


# Returns the Configuration instance from the Request object
def get_config_from_request(request: Request) -> Configuration:
    """Return the Configuration instance from the Request object."""
    return get_hass_from_request(request).data[DOMAIN][CONFIG]


# Returns the DeviceManager instance from the Request object
def get_device_manager_from_request(request: Request) -> DeviceManager:
    """Return the DeviceManager instance from the Request object."""
    return DeviceManager(
        get_hass_from_request(request),
        get_config_from_request(request),
    )


# Returns the AreaManager instance from the Request object
def get_area_manager_from_request(request: Request) -> AreaManager:
    """Return the AreaManager instance from the Request object."""
    return AreaManager(
        get_hass_from_request(request),
        get_config_from_request(request),
    )


# Returns TRUE if component is enabled in the configuration (from the Request object)
def is_component_enabled(request: Request) -> bool:
    """Return TRUE if component is enabled in the configuration."""
    return get_config_from_request(request).is_enabled()


# Removes the unwanted keys from the dictionary
def dictionary_without(dictionary: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Return the dictionary without the unwanted keys."""
    return {k: v for k, v in dictionary.items() if k not in keys}


# Returns dictionary with only wanted keys
def dictionary_with(dictionary: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Return the dictionary with only the wanted keys."""
    return {k: v for k, v in dictionary.items() if k in keys}

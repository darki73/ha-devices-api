"""Router for the Devices API component."""

from __future__ import annotations
from typing import List
from aiohttp.web import Request, Response
from homeassistant.core import HomeAssistant
from homeassistant.components.http import HomeAssistantView
from .helpers import (
    build_view_name,
    build_url,
    get_hass_from_request,
    get_config_from_request,
    get_area_manager_from_request,
    get_device_manager_from_request,
    is_component_enabled,
)
from .http import respond
from .manager import AreaManager, DeviceManager
from .configuration import Configuration
from .errors import ERROR_METHOD_NOT_ALLOWED_DISABLED, ERROR_NOT_FOUND
from .helpers import dictionary_with


# Class: Router
class Router:
    """Router for the Devices API component."""

    # HomeAssistant instance
    _hass: HomeAssistant = None
    # Routes list
    _routes: List[DevicesAPIRouter] = []

    # Constructor
    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the router."""
        self._hass = hass

    # Adds a route to the router
    def add_route(self, route: DevicesAPIRouter):
        """Add a route to the router."""
        self._routes.append(route)

    # Adds multiple routes to the router
    def add_routes(self, routes: List[DevicesAPIRouter]):
        """Add multiple routes to the router."""
        for route in routes:
            self.add_route(route)

    # Registers the routes in the HomeAssistant instance
    def register(self):
        """Register the routes in the HomeAssistant instance."""
        for route in self._routes:
            self._hass.http.register_view(route)


# Class: DevicesAPIRouter
class DevicesAPIRouter(HomeAssistantView):
    """Base class for the Devices API component routes."""

    # Returns the configuration of the component
    @staticmethod
    def _get_configuration(request: Request) -> Configuration:
        return get_config_from_request(request)

    # Returns the HomeAssistant instance from the Request object
    @staticmethod
    def _get_hass(request: Request) -> HomeAssistant:
        return get_hass_from_request(request)

    # Returns the DeviceManager instance from the Request object
    @staticmethod
    def _get_device_manager(request: Request) -> DeviceManager:
        return get_device_manager_from_request(request)

    # Returns the AreaManager instance from the Request object
    @staticmethod
    def _get_area_manager(request: Request) -> AreaManager:
        return get_area_manager_from_request(request)

    # Returns TRUE if component is enabled in the configuration (from the Request object)
    @staticmethod
    def _is_component_enabled(request: Request) -> bool:
        return is_component_enabled(request)


# Class: DevicesAPIDevicesListView
class DevicesAPIDevicesListView(DevicesAPIRouter, HomeAssistantView):
    """View to handle the Devices API component devices list."""

    # URL path
    url = build_url("devices")

    # Name of the view
    name = build_view_name("devices:list")

    # Returns the list of devices
    async def get(self, request: Request) -> Response:
        """Return the list of devices."""

        if not self._is_component_enabled(request):
            return ERROR_METHOD_NOT_ALLOWED_DISABLED.as_http_response()

        device_manager = self._get_device_manager(request)
        devices = []

        for device in device_manager.get_devices():
            if not device.is_disabled():
                devices.append(device.as_dict())

        return respond(devices)


# Class: DevicesAPIDeviceInformationView
class DevicesAPIDeviceInformationView(DevicesAPIRouter, HomeAssistantView):
    """View to handle the Devices API component device information."""

    # URL path
    url = build_url("devices/{device_id}", True)

    # Name of the view
    name = build_view_name("devices:device")

    # Returns the device information
    async def get(self, request: Request, device_id: str) -> Response:
        """Return the device information."""

        if not self._is_component_enabled(request):
            return ERROR_METHOD_NOT_ALLOWED_DISABLED.as_http_response()

        device_manager = self._get_device_manager(request)

        return respond(device_manager.get_device(device_id).with_entities())


# Class: DevicesAPIAreasListView
class DevicesAPIAreasListView(DevicesAPIRouter, HomeAssistantView):
    """View to handle the Devices API component devices list."""

    # URL path
    url = build_url("areas")

    # Name of the view
    name = build_view_name("areas:list")

    # Returns the list of areas
    async def get(self, request: Request) -> Response:
        """Return the list of areas."""

        if not self._is_component_enabled(request):
            return ERROR_METHOD_NOT_ALLOWED_DISABLED.as_http_response()

        area_manager = self._get_area_manager(request)
        areas = []

        for area in area_manager.get_areas():
            areas.append(
                dictionary_with(
                    area.as_dict(),
                    [
                        "id",
                        "name",
                    ],
                )
            )

        return respond(areas)


# Class: DevicesAPIAreaInformationView
class DevicesAPIAreaInformationView(DevicesAPIRouter, HomeAssistantView):
    """View to handle the Devices API component device information."""

    # URL path
    url = build_url("areas/{area_id}", True)

    # Name of the view
    name = build_view_name("areas:area")

    # Returns the area information
    async def get(self, request: Request, area_id: str) -> Response:
        """Return the area information."""

        if not self._is_component_enabled(request):
            return ERROR_METHOD_NOT_ALLOWED_DISABLED.as_http_response()

        area_manager = self._get_area_manager(request)

        return respond(area_manager.get_area(area_id))


# Class: DevicesAPIAreaDevicesListView
class DevicesAPIAreaDevicesListView(DevicesAPIRouter, HomeAssistantView):
    """View to handle the Devices API component area devices list."""

    # URL path
    url = build_url("areas/{area_id}/devices", True)

    # Name of the view
    name = build_view_name("areas:devices:list")

    # Returns the list of devices in the area
    async def get(self, request: Request, area_id: str) -> Response:
        """Return the list of devices in the area."""

        if not self._is_component_enabled(request):
            return ERROR_METHOD_NOT_ALLOWED_DISABLED.as_http_response()

        area_manager = self._get_area_manager(request)
        area = area_manager.get_area(area_id)
        if area is None:
            return respond(ERROR_NOT_FOUND)

        devices = []

        for device in area.get_devices():
            if device.get_area() == area_id and not device.is_disabled():
                devices.append(device.as_dict())

        return respond(devices)

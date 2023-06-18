"""Device Manager for the Devices API component."""

from __future__ import annotations
from typing import List, Dict, Any
from json import dumps
from homeassistant.core import HomeAssistant
from homeassistant.helpers.area_registry import (
    AreaRegistry,
    AreaEntry,
    async_get as async_get_area_registry,
)
from homeassistant.helpers.device_registry import (
    DeviceRegistry,
    DeviceEntry,
    async_get as async_get_device_registry,
)
from homeassistant.helpers.entity_registry import (
    EntityRegistry,
    RegistryEntry,
    async_get as async_get_entity_registry,
)
from .configuration import Configuration


# Class: Manager
class Manager:
    """Base manager class."""

    # HomeAssistant instance
    _hass: HomeAssistant = None
    # Configuration instance
    _config: Configuration = None
    # Area Registry instance
    _area_registry: AreaRegistry = None
    # Device Registry instance
    _device_registry: DeviceRegistry = None
    # Entity Registry instance
    _entity_registry: EntityRegistry = None

    # Constructor
    def __init__(self, hass: HomeAssistant, config: Configuration) -> None:
        """Initialize the base manager class."""
        self._hass = hass
        self._config = config
        self._area_registry = async_get_area_registry(hass)
        self._device_registry = async_get_device_registry(hass)
        self._entity_registry = async_get_entity_registry(hass)

    # Returns the area registry
    def get_area_registry(self) -> AreaRegistry:
        """Return the area registry."""
        return self._area_registry

    # Returns the device registry
    def get_device_registry(self) -> DeviceRegistry:
        """Return the device registry."""
        return self._device_registry

    # Returns the entity registry
    def get_entity_registry(self) -> EntityRegistry:
        """Return the entity registry."""
        return self._entity_registry

    # Returns the HomeAssistant instance
    def get_hass(self) -> HomeAssistant:
        """Return the HomeAssistant instance."""
        return self._hass

    # Returns the configuration
    def get_configuration(self) -> Configuration:
        """Return the configuration."""
        return self._config


# Class: DeviceManager
class DeviceManager(Manager):
    """Device Manager class."""

    # Returns the devices list
    def get_devices(self) -> List[Device]:
        """Return the devices list."""
        devices: List[Device] = []

        for device in self._device_registry.devices.values():
            devices.append(
                Device(
                    device,
                    self.get_entity_registry(),
                )
            )

        return devices

    # Returns the device by ID
    def get_device(self, device_id: str) -> Device:
        """Return the device by ID."""
        return Device(
            self._device_registry.async_get(device_id),
            self.get_entity_registry(),
        )


# Class: Device
class Device:
    """Device class."""

    # Device entry
    _entry: DeviceEntry
    # Entity registry
    _entity_registry: EntityRegistry
    # Entities list
    _entities: List[Entity] = []

    # Constructor
    def __init__(
        self,
        device_entry: DeviceEntry,
        entity_registry: EntityRegistry,
    ) -> None:
        """Constructor."""
        self._entry = device_entry
        self._entity_registry = entity_registry
        self._entities = []

    # Returns the device ID
    def get_id(self) -> str:
        """Return the device ID."""
        return self._entry.id

    # Returns the device name
    def get_name(self) -> str:
        """Return the device name."""
        if self._entry.name_by_user:
            return self._entry.name_by_user
        return self._entry.name

    # Returns the device manufacturer
    def get_manufacturer(self) -> str:
        """Return the device manufacturer."""
        return self._entry.manufacturer

    # Returns the device model
    def get_model(self) -> str:
        """Return the device model."""
        return self._entry.model

    # Returns the device area
    def get_area(self) -> str:
        """Return the device area."""
        return self._entry.area_id

    # Returns the hardware version
    def get_hw_version(self) -> str:
        """Return the hardware version."""
        return self._entry.hw_version

    # Returns the software version
    def get_sw_version(self) -> str:
        """Return the software version."""
        return self._entry.sw_version

    # Returns TRUE if the device is disabled
    def is_disabled(self) -> bool:
        """Return TRUE if the device is disabled."""
        return self._entry.disabled_by is not None

    # Returns the device type
    def get_type(self) -> str:
        """Return the device type."""
        return self._entry.entry_type

    # Returns the entity registry
    def get_entity_registry(self) -> EntityRegistry:
        """Return the entity registry."""
        return self._entity_registry

    # Loads list of entities for the device
    def with_entities(self) -> Device:
        """Load list of entities for the device."""

        for entity_entry in self.get_entity_registry().entities.values():
            if entity_entry.device_id == self.get_id():
                self._entities.append(
                    Entity(
                        entity_entry,
                    )
                )

        return self

    # Returns list of entities for the device
    def get_entities(self) -> List[Entity]:
        """Return list of entities for the device."""
        return self._entities

    # Returns the device as a dictionary
    def as_dict(self) -> dict:
        """Return the device as a dictionary."""
        dictionary: Dict[str, Any] = {
            "id": self.get_id(),
            "name": self.get_name(),
            "manufacturer": self.get_manufacturer(),
            "model": self.get_model(),
            "area": self.get_area(),
            "hw_version": self.get_hw_version(),
            "sw_version": self.get_sw_version(),
            "disabled": self.is_disabled(),
            "type": self.get_type(),
        }

        if len(self._entities) > 0:
            dictionary["entities"] = [
                entity.as_dict() for entity in self.get_entities()
            ]

        return dictionary

    # Returns the device as a JSON string
    def as_json(self) -> str:
        """Return the device as a JSON string."""
        return dumps(self.as_dict(), indent=4)

    # Returns the device as a string
    def __str__(self) -> str:
        """Return the device as a string."""
        return self.as_json()


# Class: Entity
class Entity:
    """Entity class."""

    # Entity entry
    _entry: RegistryEntry

    # Constructor
    def __init__(self, entity_entry: RegistryEntry) -> None:
        """Constructor."""
        self._entry = entity_entry

    # Returns the entity ID
    def get_id(self) -> str:
        """Return the entity ID."""
        return self._entry.entity_id

    # Returns the entity unique ID
    def get_unique_id(self) -> str:
        """Return the entity unique ID."""
        return self._entry.unique_id

    # Returns the entity name
    def get_name(self) -> str:
        """Return the entity name."""
        if self._entry.name:
            return self._entry.name
        return self._entry.original_name

    # Returns the entity category
    def get_category(self) -> str | None:
        """Return the entity category."""
        if self._entry.entity_category:
            return self._entry.entity_category.value
        return None

    # Returns the entity icon
    def get_icon(self) -> str:
        """Return the entity icon."""
        if self._entry.icon:
            return self._entry.icon
        return self._entry.original_icon

    # Returns the entity device ID
    def get_device_id(self) -> str:
        """Return the entity device ID."""
        return self._entry.device_id

    # Returns the entity device class
    def get_device_class(self) -> str:
        """Return the entity device class."""
        if self._entry.device_class:
            return self._entry.device_class
        return self._entry.original_device_class

    # Returns the entity platform
    def get_platform(self) -> str:
        """Return the entity platform."""
        return self._entry.platform

    # Returns the entity unit of measurement
    def get_unit_of_measurement(self) -> str:
        """Return the entity unit of measurement."""
        if self._entry.unit_of_measurement is None:
            mappings = {
                "timestamp": "s",
            }
            return mappings.get(self.get_device_class(), None)
        return self._entry.unit_of_measurement

    # Returns the entity capabilities
    def get_capabilities(self) -> Dict[str, Any]:
        """Return the entity capabilities."""
        if self._entry.capabilities is None:
            return []
        return self._entry.capabilities

    # Converts the entity to a dictionary
    def as_dict(self) -> dict:
        """Convert the entity to a dictionary."""
        dictionary: Dict[str, Any] = {
            "id": self.get_id(),
            "unique_id": self.get_unique_id(),
            "name": self.get_name(),
            "category": self.get_category(),
            "icon": self.get_icon(),
            "device_id": self.get_device_id(),
            "device_class": self.get_device_class(),
            "platform": self.get_platform(),
            "unit_of_measurement": self.get_unit_of_measurement(),
            "capabilities": self.get_capabilities(),
        }

        return dictionary

    # Converts the entity to a JSON string
    def as_json(self) -> str:
        """Convert the entity to a JSON string."""
        return dumps(self.as_dict(), indent=4)

    # Converts the entity to a string
    def __str__(self) -> str:
        """Convert the entity to a string."""
        return self.as_json()


# Class: AreaManager
class AreaManager(Manager):
    """Area Manager class."""

    # Returns the list of areas
    def get_areas(self) -> List[Area]:
        """Return the list of areas."""
        areas: List[Area] = []

        for area in self.get_area_registry().areas.values():
            areas.append(
                Area(
                    area,
                    self.get_device_registry(),
                    self.get_entity_registry(),
                )
            )

        return areas

    # Returns the area by ID
    def get_area(self, area_id: str) -> Area | None:
        """Return the area by ID."""
        area = self.get_area_registry().areas.get(area_id)
        if area is None:
            return None
        return Area(
            area,
            self.get_device_registry(),
            self.get_entity_registry(),
        )


# Class: Area
class Area:
    """Area class."""

    # Area entry
    _entry: AreaEntry
    # Device registry
    _device_registry: DeviceRegistry
    # Entity registry
    _entity_registry: EntityRegistry

    # Constructor
    def __init__(
        self,
        area_entry: AreaEntry,
        device_registry: DeviceRegistry,
        entity_registry: EntityRegistry,
    ) -> None:
        """Constructor."""
        self._entry = area_entry
        self._device_registry = device_registry
        self._entity_registry = entity_registry

    # Returns the area ID
    def get_id(self) -> str:
        """Return the area ID."""
        return self._entry.id

    # Returns the area name
    def get_name(self) -> str:
        """Return the area name."""
        return self._entry.name

    # Returns the area normalized name
    def get_normalized_name(self) -> str:
        """Return the area normalized name."""
        return self._entry.normalized_name

    # Returns the area picture
    def get_picture(self) -> str | None:
        """Return the area picture."""
        return self._entry.picture

    # Returns the list of devices in the area
    def get_devices(self) -> List[Device]:
        """Return the list of devices in the area."""
        devices: List[Device] = []

        for device in self._device_registry.devices.values():
            if device.area_id == self.get_id():
                devices.append(
                    Device(
                        device,
                        self._entity_registry,
                    )
                )

        return devices

    # Converts the area to a dictionary
    def as_dict(self) -> dict:
        """Convert the area to a dictionary."""
        dictionary: Dict[str, Any] = {
            "id": self.get_id(),
            "name": self.get_name(),
            "normalized_name": self.get_normalized_name(),
            "picture": self.get_picture(),
        }

        return dictionary

    # Converts the area to a JSON string
    def as_json(self) -> str:
        """Convert the area to a JSON string."""
        return dumps(self.as_dict(), indent=4)

    # Converts the area to a string
    def __str__(self) -> str:
        """Convert the area to a string."""
        return self.as_json()

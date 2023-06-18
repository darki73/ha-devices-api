"""Container for the Device API configuration"""

from __future__ import annotations
from typing import Any, Dict, List
from json import dumps, loads


# Class: ChatGPTConfiguration
class ChatGPTConfiguration:
    """Configuration for the ChatGPT service integration"""

    # Model name
    _model_name: str
    # API Key
    _api_key: str

    # Constructor
    def __init__(self, api_key: str = "", model_name: str = "gpt-3.5-turbo") -> None:
        self._model_name = model_name
        self._api_key = api_key

    # Returns the model name
    def get_model_name(self) -> str:
        """Returns the model name"""
        return self._model_name

    # Returns the API key
    def get_api_key(self) -> str:
        """Returns the API key"""
        return self._api_key

    # Returns the configuration as a dictionary
    def as_dict(self) -> Dict[str, Any]:
        """Returns the configuration as a dictionary"""
        return {
            "model_name": self._model_name,
            "api_key": self._api_key,
        }

    # Returns the configuration as a JSON string
    def as_json(self) -> str:
        """Returns the configuration as a JSON string"""
        return dumps(self.as_dict(), indent=4)

    # Returns the configuration as a string
    def __str__(self) -> str:
        """Returns the configuration as a string"""
        return self.as_json()

    # Creates a configuration from a dictionary
    @staticmethod
    def from_dict(config: Dict[str, Any]) -> ChatGPTConfiguration:
        """Creates a configuration from a dictionary"""
        return ChatGPTConfiguration(
            model_name=config.get("model_name", "gpt-3.5-turbo"),
            api_key=config.get("api_key", ""),
        )

    # Creates a configuration from a JSON string
    @staticmethod
    def from_json(config: str) -> ChatGPTConfiguration:
        """Creates a configuration from a JSON string"""
        return ChatGPTConfiguration.from_dict(loads(config))

    # Creates a configuration from either a dictionary or a JSON string
    @staticmethod
    def from_any(config: Any) -> ChatGPTConfiguration:
        """Creates a configuration from either a dictionary or a JSON string"""
        if isinstance(config, str):
            return ChatGPTConfiguration.from_json(config)
        elif isinstance(config, dict):
            return ChatGPTConfiguration.from_dict(config)
        else:
            raise ValueError("Invalid configuration")


# Class: IgnoredDomainsConfiguration
class IgnoredDomainsConfiguration:
    """Configuration for the list of ignored domains"""

    # Ignored domains
    _ignored_domains: List[str]

    # Constructor
    def __init__(self, ignored_domains: List[str] = []) -> None:
        self._ignored_domains = ignored_domains

    # Adds a domain to the list of ignored domains
    def add_ignored_domain(self, domain: str) -> None:
        """Adds a domain to the list of ignored domains"""
        self._ignored_domains.append(domain)

    # Removes a domain from the list of ignored domains
    def remove_ignored_domain(self, domain: str) -> None:
        """Removes a domain from the list of ignored domains"""
        self._ignored_domains.remove(domain)

    # Returns the list of ignored domains
    def get_ignored_domains(self) -> List[str]:
        """Returns the list of ignored domains"""
        return self._ignored_domains

    # Indicates whether a domain is ignored
    def is_ignored_domain(self, domain: str) -> bool:
        """Indicates whether a domain is ignored"""
        return domain in self._ignored_domains

    # Indicates whether entity belongs to an ignored domain
    def is_ignored_entity(self, entity_id: str) -> bool:
        """Indicates whether entity belongs to an ignored domain"""
        return self.is_ignored_domain(entity_id.split(".")[0])

    # Returns the configuration as a dictionary
    def as_dict(self) -> Dict[str, Any]:
        """Returns the configuration as a dictionary"""
        return {
            "ignored_domains": self._ignored_domains,
        }

    # Returns the configuration as a JSON string
    def as_json(self) -> str:
        """Returns the configuration as a JSON string"""
        return dumps(self.as_dict(), indent=4)

    # Returns the configuration as a string
    def __str__(self) -> str:
        """Returns the configuration as a string"""
        return self.as_json()

    # Creates a configuration from a dictionary
    @staticmethod
    def from_dict(config: Dict[str, Any]) -> IgnoredDomainsConfiguration:
        """Creates a configuration from a dictionary"""
        return IgnoredDomainsConfiguration(
            ignored_domains=config.get("ignored_domains", []),
        )

    # Creates a configuration from a JSON string
    @staticmethod
    def from_json(config: str) -> IgnoredDomainsConfiguration:
        """Creates a configuration from a JSON string"""
        return IgnoredDomainsConfiguration.from_dict(loads(config))

    # Creates a configuration from list of domains
    @staticmethod
    def from_list(domains: List[str]) -> IgnoredDomainsConfiguration:
        """Creates a configuration from list of domains"""
        return IgnoredDomainsConfiguration(ignored_domains=domains)

    # Creates a configuration from either a dictionary, list or a JSON string
    @staticmethod
    def from_any(config: Any) -> IgnoredDomainsConfiguration:
        """Creates a configuration from either a dictionary, list or a JSON string"""
        if isinstance(config, str):
            return IgnoredDomainsConfiguration.from_json(config)
        elif isinstance(config, dict):
            return IgnoredDomainsConfiguration.from_dict(config)
        elif isinstance(config, list):
            return IgnoredDomainsConfiguration.from_list(config)
        else:
            raise ValueError("Invalid configuration")


# Class: AllowedIPsConfiguration
class AllowedIPsConfiguration:
    """Configuration for the list of allowed IPs"""

    # Allowed IPs
    _allowed_ips: List[str]

    # Constructor
    def __init__(self, allowed_ips: List[str] = []) -> None:
        self._allowed_ips = allowed_ips

    # Adds an IP to the list of allowed IPs
    def add_allowed_ip(self, ip: str) -> None:
        """Adds an IP to the list of allowed IPs"""
        self._allowed_ips.append(ip)

    # Removes an IP from the list of allowed IPs
    def remove_allowed_ip(self, ip: str) -> None:
        """Removes an IP from the list of allowed IPs"""
        self._allowed_ips.remove(ip)

    # Returns the list of allowed IPs
    def get_allowed_ips(self) -> List[str]:
        """Returns the list of allowed IPs"""
        return self._allowed_ips

    # Indicates whether an IP is allowed
    def is_allowed_ip(self, ip: str) -> bool:
        """Indicates whether an IP is allowed"""
        return ip in self._allowed_ips

    # Returns the configuration as a dictionary
    def as_dict(self) -> Dict[str, Any]:
        """Returns the configuration as a dictionary"""
        return {
            "allowed_ips": self._allowed_ips,
        }

    # Returns the configuration as a JSON string
    def as_json(self) -> str:
        """Returns the configuration as a JSON string"""
        return dumps(self.as_dict(), indent=4)

    # Returns the configuration as a string
    def __str__(self) -> str:
        """Returns the configuration as a string"""
        return self.as_json()

    # Creates a configuration from a dictionary
    @staticmethod
    def from_dict(config: Dict[str, Any]) -> AllowedIPsConfiguration:
        """Creates a configuration from a dictionary"""
        return AllowedIPsConfiguration(
            allowed_ips=config.get("allowed_ips", []),
        )

    # Creates a configuration from a JSON string
    @staticmethod
    def from_json(config: str) -> AllowedIPsConfiguration:
        """Creates a configuration from a JSON string"""
        return AllowedIPsConfiguration.from_dict(loads(config))

    # Creates a configuration from list of allowed IPs
    @staticmethod
    def from_list(allowed_ips: List[str]) -> AllowedIPsConfiguration:
        """Creates a configuration from list of allowed IPs"""
        return AllowedIPsConfiguration(allowed_ips=allowed_ips)

    # Creates a configuration from either a dictionary, list or a JSON string
    @staticmethod
    def from_any(config: Any) -> AllowedIPsConfiguration:
        """Creates a configuration from either a dictionary, list or a JSON string"""
        if isinstance(config, str):
            return AllowedIPsConfiguration.from_json(config)
        elif isinstance(config, dict):
            return AllowedIPsConfiguration.from_dict(config)
        elif isinstance(config, list):
            return AllowedIPsConfiguration.from_list(config)
        else:
            raise ValueError("Invalid configuration")


# Class: Configuration
class Configuration:
    """Configuration for the component"""

    # Enables or disables the component
    _enabled: bool
    # ChatGPT configuration
    _chatgpt: ChatGPTConfiguration
    # Ignored domains configuration
    _ignored_domains: IgnoredDomainsConfiguration
    # Allowed IPs configuration

    # Constructor
    def __init__(
        self,
        enabled: bool,
        chatgpt: ChatGPTConfiguration,
        ignored_domains: IgnoredDomainsConfiguration,
        allowed_ips: AllowedIPsConfiguration,
    ) -> None:
        self._enabled = enabled
        self._chatgpt = chatgpt
        self._ignored_domains = ignored_domains
        self._allowed_ips = allowed_ips

    # Enables or disables the component
    def set_enabled(self, enabled: bool) -> None:
        """Enables or disables the component"""
        self._enabled = enabled

    # Indicates whether the component is enabled
    def is_enabled(self) -> bool:
        """Indicates whether the component is enabled"""
        return self._enabled

    # Returns the ChatGPT configuration
    def get_chatgpt(self) -> ChatGPTConfiguration:
        """Returns the ChatGPT configuration"""
        return self._chatgpt

    # Returns the ignored domains configuration
    def get_ignored_domains(self) -> IgnoredDomainsConfiguration:
        """Returns the ignored domains configuration"""
        return self._ignored_domains

    # Returns the allowed IPs configuration
    def get_allowed_ips(self) -> AllowedIPsConfiguration:
        """Returns the allowed IPs configuration"""
        return self._allowed_ips

    # Returns the configuration as a dictionary
    def as_dict(self) -> Dict[str, Any]:
        """Returns the configuration as a dictionary"""
        return {
            "enabled": self._enabled,
            "chatgpt": self._chatgpt.as_dict(),
            "ignored_domains": self._ignored_domains.get_ignored_domains(),
            "allowed_ips": self._allowed_ips.get_allowed_ips(),
        }

    # Returns the configuration as a JSON string
    def as_json(self) -> str:
        """Returns the configuration as a JSON string"""
        return dumps(self.as_dict(), indent=4)

    # Returns the configuration as a string
    def __str__(self) -> str:
        """Returns the configuration as a string"""
        return self.as_json()

    # Creates a configuration from a dictionary
    @staticmethod
    def from_dict(config: Dict[str, Any]) -> Configuration:
        """Creates a configuration from a dictionary"""
        return Configuration(
            enabled=config.get("enabled", True),
            chatgpt=ChatGPTConfiguration.from_any(config.get("chat_gpt", {})),
            ignored_domains=IgnoredDomainsConfiguration.from_any(
                config.get("ignored_domains", [])
            ),
            allowed_ips=AllowedIPsConfiguration.from_any(config.get("allowed_ips", [])),
        )

    # Creates a configuration from a JSON string
    @staticmethod
    def from_json(config: str) -> Configuration:
        """Creates a configuration from a JSON string"""
        return Configuration.from_dict(loads(config))

    # Creates a configuration from either a dictionary or a JSON string
    @staticmethod
    def from_any(config: Any) -> Configuration:
        """Creates a configuration from either a dictionary or a JSON string"""
        if isinstance(config, str):
            return Configuration.from_json(config)
        elif isinstance(config, dict):
            return Configuration.from_dict(config)
        else:
            raise ValueError("Invalid configuration")

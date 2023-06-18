"""Errors for the Devices API component."""

from __future__ import annotations
from json import dumps
from aiohttp.web import Response


# Class: Error
class Error(Exception):
    """Base class for exceptions in this module."""

    # Error code
    _code: int
    # Error message
    _message: str

    # Constructor
    def __init__(self, code: int, message: str) -> None:
        """Constructor."""
        self._code = code
        self._message = message
        super().__init__(self, message)

    # Return error code
    def get_code(self) -> int:
        """Return error code."""
        return self._code

    # Return error message
    def get_message(self) -> str:
        """Return error message."""
        return self._message

    # Returns the error as a dictionary
    def as_dict(self) -> dict:
        """Return error as a dictionary."""
        return {"code": self.get_code(), "message": self.get_message()}

    # Returns the error as a JSON string
    def as_json(self) -> str:
        """Return error as a JSON string."""
        return dumps(self.as_dict(), indent=4)

    # Returns the error as a JSON for HTTP response
    def as_http_json(self) -> str:
        """Return error as a JSON for HTTP response."""
        return dumps({"error": self.as_dict()}, indent=4)

    # Returns the error as aiohttp response
    def as_http_response(self) -> Response:
        """Return error as aiohttp response."""
        return Response(status=self.get_code(), text=self.as_http_json())

    # Returns the error as a string
    def __str__(self) -> str:
        """Return error as a string."""
        return self.as_http_json()


# Bad request error constant.
ERROR_BAD_REQUEST = Error(400, "Bad Request")

# Unauthorized error constant.
ERROR_UNAUTHORIZED = Error(401, "Unauthorized")

# Forbidden error constant.
ERROR_FORBIDDEN = Error(403, "Forbidden")

# Not found error constant.
ERROR_NOT_FOUND = Error(404, "Not Found")

# Method not allowed error constant.
ERROR_METHOD_NOT_ALLOWED = Error(405, "Method Not Allowed")

# Method not allowed error constant (for when the component is disabled).
ERROR_METHOD_NOT_ALLOWED_DISABLED = Error(
    405, "Devices API Component is disabled in the configuration"
)

# Internal server error constant.
ERROR_INTERNAL_SERVER_ERROR = Error(500, "Internal Server Error")

# Not implemented error constant.
ERROR_NOT_IMPLEMENTED = Error(501, "Not Implemented")

# Service unavailable error constant.
ERROR_SERVICE_UNAVAILABLE = Error(503, "Service Unavailable")

# Gateway timeout error constant.
ERROR_GATEWAY_TIMEOUT = Error(504, "Gateway Timeout")

# Unsupported HTTP version error constant.
ERROR_HTTP_VERSION_NOT_SUPPORTED = Error(505, "HTTP Version Not Supported")

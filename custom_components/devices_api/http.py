"""Http helpers for the Devices API component."""

from __future__ import annotations
from time import time
from json import dumps, loads, JSONDecodeError
from typing import List, Dict, Any
from aiohttp.web import Request, Response
from inspect import isclass
from .errors import ERROR_NOT_FOUND


def respond(data: Any, none_is_error: bool = True) -> Response:
    if data is None and none_is_error:
        data = ERROR_NOT_FOUND.as_http_json()

    response_data = _generate_response_text(data)
    response_data["request_time"] = time()

    if "error" in response_data:
        return Response(
            body=dumps(response_data, indent=4),
            status=response_data["error"]["code"],
            content_type="application/json",
        )
    else:
        return Response(
            body=dumps(response_data, indent=4),
            status=200,
            content_type="application/json",
        )


# Generates the response text from the data
def _generate_response_text(data: Any) -> Dict[str, Any]:
    """Generate the response text from the data."""
    if hasattr(data, "as_dict") and callable(getattr(data, "as_dict")):
        return {"data": data.as_dict()}
    elif isinstance(data, (dict, list)):
        return {"data": data}
    elif isinstance(data, (int, float, bool)):
        return {"data": str(data).lower()}
    elif isinstance(data, str):
        return _process_string_data(data)
    elif data is None:
        return {"data": "null"}
    else:
        return {"data": "Unknown data type"}


# Checks if a string is valid JSON and processes it accordingly
def _process_string_data(string: str):
    """Check if a string is valid JSON and process it accordingly."""
    try:
        return loads(string)
    except JSONDecodeError:
        return {"data": string}

"""Shared test fixtures for lolzpy."""

from __future__ import annotations

import json
from typing import Any
from unittest.mock import MagicMock

from curl_cffi.requests import Response
from curl_cffi.requests.headers import Headers


def make_response(
    status_code: int = 200,
    json_data: Any = None,
    body: bytes | None = None,
    headers: dict[str, str] | None = None,
) -> Response:
    """Create a fake curl_cffi Response for testing."""
    resp = Response()
    resp.status_code = status_code
    if json_data is not None:
        resp.content = json.dumps(json_data).encode()
    elif body is not None:
        resp.content = body
    else:
        resp.content = b""
    resp.headers = Headers(headers or {})
    return resp


def make_session(responses: list[Response]) -> MagicMock:
    """Create a mock Session whose .request() returns responses in order."""
    session = MagicMock()
    session.request = MagicMock(side_effect=responses)
    return session


def make_async_session(responses: list[Response]) -> MagicMock:
    """Create a mock AsyncSession whose .request() returns responses in order."""
    from unittest.mock import AsyncMock

    session = MagicMock()
    session.request = AsyncMock(side_effect=responses)
    return session

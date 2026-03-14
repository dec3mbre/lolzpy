"""Exception hierarchy for lolzpy."""

from __future__ import annotations

import contextlib
from collections.abc import Mapping
from typing import Any


class LolzError(Exception):
    """Base exception for all lolzpy errors."""

    def __init__(self, message: str, *, status_code: int | None = None, response_data: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data


class AuthError(LolzError):
    """Authentication or authorization failure (401/403)."""


class NotFoundError(LolzError):
    """Requested resource was not found (404)."""


class RateLimitError(LolzError):
    """Rate limit exceeded (429). The request can be retried after a delay."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = 429,
        response_data: Any = None,
        retry_after: float | None = None,
    ) -> None:
        super().__init__(message, status_code=status_code, response_data=response_data)
        self.retry_after = retry_after


class ServerError(LolzError):
    """Server-side error (5xx)."""


class ValidationError(LolzError):
    """Response validation error — the API returned data that doesn't match the expected schema."""


def raise_for_status(
    status_code: int,
    response_data: Any = None,
    headers: Mapping[str, str | None] | None = None,
) -> None:
    """Raise an appropriate LolzError subclass based on the HTTP status code."""
    if 200 <= status_code < 400:
        return

    message = f"HTTP {status_code}"
    if isinstance(response_data, dict):
        message = response_data.get("error", response_data.get("message", message))

    if status_code == 401 or status_code == 403:
        raise AuthError(message, status_code=status_code, response_data=response_data)

    if status_code == 404:
        raise NotFoundError(message, status_code=status_code, response_data=response_data)

    if status_code == 429:
        retry_after: float | None = None
        if headers:
            raw = headers.get("retry-after") or headers.get("Retry-After")
            if raw:
                with contextlib.suppress(ValueError, TypeError):
                    retry_after = float(raw)
        raise RateLimitError(
            message, status_code=status_code, response_data=response_data, retry_after=retry_after
        )

    if status_code >= 500:
        raise ServerError(message, status_code=status_code, response_data=response_data)

    raise LolzError(message, status_code=status_code, response_data=response_data)

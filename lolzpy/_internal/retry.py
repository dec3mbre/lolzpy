"""Retry logic: exponential backoff, delay calculation, and retry-aware request helpers."""

from __future__ import annotations

import asyncio
import random
import time
from typing import TYPE_CHECKING, Any, cast

from curl_cffi.requests import AsyncSession, Response, Session
from curl_cffi.requests.exceptions import RequestException, SessionClosed

from lolzpy.core.config import RetryConfig

if TYPE_CHECKING:
    from curl_cffi.requests.session import HttpMethod

_RETRYABLE_EXCEPTIONS = (ConnectionError, TimeoutError, OSError)


# ---------------------------------------------------------------------------
# Delay calculation
# ---------------------------------------------------------------------------


def _parse_retry_after(headers: Any) -> float | None:
    """Extract Retry-After value (seconds) from response headers."""
    raw = None
    if hasattr(headers, "get"):
        raw = headers.get("retry-after") or headers.get("Retry-After")
    if raw is None:
        return None
    try:
        val = float(raw)
        return val if val > 0 else None
    except (ValueError, TypeError):
        return None


def _calculate_delay(attempt: int, retry_after: float | None, config: RetryConfig) -> float:
    """Compute sleep duration for a retry attempt.

    Uses exponential backoff with ±25 % jitter, respecting Retry-After if present and reasonable.
    """
    if retry_after is not None and 0 < retry_after <= config.max_retry_after:
        return retry_after

    delay = min(config.initial_delay * (2**attempt), config.max_delay)
    delay *= 0.75 + 0.25 * random.random()  # noqa: S311
    return max(config.initial_delay, delay)


def _should_retry(status_code: int, attempt: int, config: RetryConfig) -> bool:
    return attempt < config.max_retries and status_code in config.retryable_statuses


# ---------------------------------------------------------------------------
# Retry-aware request helpers
# ---------------------------------------------------------------------------


def request_with_retry_sync(
    session: Session,
    method: str,
    url: str,
    config: RetryConfig,
    **kwargs: Any,
) -> Response:
    """Execute an HTTP request with automatic retry on transient failures."""
    last_response: Response | None = None

    for attempt in range(config.max_retries + 1):
        try:
            response = session.request(cast("HttpMethod", method), url, **kwargs)
        except SessionClosed:
            raise
        except (*_RETRYABLE_EXCEPTIONS, RequestException):
            if attempt >= config.max_retries:
                raise
            delay = _calculate_delay(attempt, None, config)
            time.sleep(delay)
            continue

        if not _should_retry(response.status_code, attempt, config):
            return response

        last_response = response
        retry_after = _parse_retry_after(response.headers)
        delay = _calculate_delay(attempt, retry_after, config)
        time.sleep(delay)

    if last_response is None:
        raise RuntimeError("No response received after retries")
    return last_response


async def request_with_retry_async(
    session: AsyncSession,
    method: str,
    url: str,
    config: RetryConfig,
    **kwargs: Any,
) -> Response:
    """Execute an async HTTP request with automatic retry on transient failures."""
    last_response: Response | None = None

    for attempt in range(config.max_retries + 1):
        try:
            response = await session.request(cast("HttpMethod", method), url, **kwargs)
        except SessionClosed:
            raise
        except (*_RETRYABLE_EXCEPTIONS, RequestException):
            if attempt >= config.max_retries:
                raise
            delay = _calculate_delay(attempt, None, config)
            await asyncio.sleep(delay)
            continue

        if not _should_retry(response.status_code, attempt, config):
            return response

        last_response = response
        retry_after = _parse_retry_after(response.headers)
        delay = _calculate_delay(attempt, retry_after, config)
        await asyncio.sleep(delay)

    if last_response is None:
        raise RuntimeError("No response received after retries")
    return last_response

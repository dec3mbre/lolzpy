"""Transport layer: retry logic, rate limiting, and request helpers."""

from __future__ import annotations

import asyncio
import random
import threading
import time
from dataclasses import dataclass, field
from typing import Any

from curl_cffi.requests import AsyncSession, Response, Session
from curl_cffi.requests.exceptions import RequestException, SessionClosed

from lolz_sdk._exceptions import raise_for_status

RETRYABLE_STATUS_CODES: frozenset[int] = frozenset({429, 500, 502, 503, 504})


@dataclass(frozen=True, slots=True)
class RetryConfig:
    """Configuration for automatic request retries."""

    max_retries: int = 3
    initial_delay: float = 0.5
    max_delay: float = 8.0
    max_retry_after: float = 60.0
    retryable_statuses: frozenset[int] = field(default=RETRYABLE_STATUS_CODES)


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

    delay = min(config.initial_delay * (2 ** attempt), config.max_delay)
    delay *= 0.75 + 0.25 * random.random()  # noqa: S311
    return max(config.initial_delay, delay)


def _should_retry(status_code: int, attempt: int, config: RetryConfig) -> bool:
    return attempt < config.max_retries and status_code in config.retryable_statuses


# ---------------------------------------------------------------------------
# Token-bucket rate limiters
# ---------------------------------------------------------------------------

class TokenBucketSync:
    """Thread-safe synchronous token-bucket rate limiter."""

    __slots__ = ("_rate", "_max_tokens", "_tokens", "_last_refill", "_lock")

    def __init__(self, rate: float) -> None:
        self._rate = rate
        self._max_tokens = rate
        self._tokens = rate
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self) -> None:
        while True:
            with self._lock:
                self._refill()
                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    return
                wait = (1.0 - self._tokens) / self._rate
            time.sleep(wait)

    def _refill(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self._max_tokens, self._tokens + elapsed * self._rate)
        self._last_refill = now


class TokenBucketAsync:
    """Async-safe token-bucket rate limiter."""

    __slots__ = ("_rate", "_max_tokens", "_tokens", "_last_refill", "_lock")

    def __init__(self, rate: float) -> None:
        self._rate = rate
        self._max_tokens = rate
        self._tokens = rate
        self._last_refill: float | None = None
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        while True:
            async with self._lock:
                self._refill()
                if self._tokens >= 1.0:
                    self._tokens -= 1.0
                    return
                wait = (1.0 - self._tokens) / self._rate
            await asyncio.sleep(wait)

    def _refill(self) -> None:
        now = time.monotonic()
        if self._last_refill is None:
            self._last_refill = now
            return
        elapsed = now - self._last_refill
        self._tokens = min(self._max_tokens, self._tokens + elapsed * self._rate)
        self._last_refill = now


# ---------------------------------------------------------------------------
# Retry-aware request helpers
# ---------------------------------------------------------------------------

_RETRYABLE_EXCEPTIONS = (ConnectionError, TimeoutError, OSError)


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
            response = session.request(method, url, **kwargs)
        except SessionClosed:
            raise
        except (*_RETRYABLE_EXCEPTIONS, RequestException) as exc:
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

    assert last_response is not None  # noqa: S101
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
            response = await session.request(method, url, **kwargs)
        except SessionClosed:
            raise
        except (*_RETRYABLE_EXCEPTIONS, RequestException) as exc:
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

    assert last_response is not None  # noqa: S101
    return last_response

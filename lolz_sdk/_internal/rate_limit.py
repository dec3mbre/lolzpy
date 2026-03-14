"""Token-bucket rate limiters for sync and async contexts."""

from __future__ import annotations

import asyncio
import threading
import time


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

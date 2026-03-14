"""Tests for lolzpy._internal.rate_limit — token bucket rate limiters."""

from __future__ import annotations

import time

import pytest

from lolzpy._internal.rate_limit import TokenBucketAsync, TokenBucketSync

# ---------------------------------------------------------------------------
# TokenBucketSync
# ---------------------------------------------------------------------------


class TestTokenBucketSync:
    def test_acquire_immediate_within_rate(self):
        bucket = TokenBucketSync(10.0)  # 10 requests/sec
        start = time.monotonic()
        for _ in range(5):
            bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed < 1.0  # Should be nearly instant

    def test_acquire_throttles_at_capacity(self):
        bucket = TokenBucketSync(2.0)  # 2 requests/sec
        # Drain all tokens
        bucket.acquire()
        bucket.acquire()
        start = time.monotonic()
        bucket.acquire()  # Must wait for refill
        elapsed = time.monotonic() - start
        assert elapsed >= 0.3  # Should wait ~0.5s


# ---------------------------------------------------------------------------
# TokenBucketAsync
# ---------------------------------------------------------------------------


class TestTokenBucketAsync:
    @pytest.mark.asyncio
    async def test_acquire_immediate_within_rate(self):
        bucket = TokenBucketAsync(10.0)
        start = time.monotonic()
        for _ in range(5):
            await bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed < 1.0

    @pytest.mark.asyncio
    async def test_acquire_throttles_at_capacity(self):
        bucket = TokenBucketAsync(2.0)
        await bucket.acquire()
        await bucket.acquire()
        start = time.monotonic()
        await bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed >= 0.3

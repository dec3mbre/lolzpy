"""Tests for lolzpy._internal.rate_limit — token bucket rate limiters."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from lolzpy._internal.rate_limit import TokenBucketAsync, TokenBucketSync


def _make_advancing_monotonic(start: float = 1000.0, step: float = 0.0):
    """Create a monotonic mock that advances by `step` on each call after sleep."""
    state = {"now": start, "step": step}

    def monotonic():
        return state["now"]

    def advance(seconds):
        state["now"] += seconds

    return monotonic, advance


# ---------------------------------------------------------------------------
# TokenBucketSync
# ---------------------------------------------------------------------------


class TestTokenBucketSync:
    def test_acquire_immediate_within_rate(self):
        bucket = TokenBucketSync(10.0)  # 10 tokens available
        # Should not sleep — we have 10 tokens
        with patch("lolzpy._internal.rate_limit.time.sleep") as mock_sleep:
            for _ in range(5):
                bucket.acquire()
            mock_sleep.assert_not_called()

    def test_acquire_throttles_at_capacity(self):
        monotonic, advance = _make_advancing_monotonic()

        with (
            patch("lolzpy._internal.rate_limit.time.monotonic", side_effect=monotonic),
            patch("lolzpy._internal.rate_limit.time.sleep", side_effect=advance) as mock_sleep,
        ):
            bucket = TokenBucketSync(2.0)  # 2 tokens
            bucket.acquire()
            bucket.acquire()
            # Next acquire must sleep to refill
            bucket.acquire()
            mock_sleep.assert_called_once()
            delay = mock_sleep.call_args[0][0]
            assert delay > 0


# ---------------------------------------------------------------------------
# TokenBucketAsync
# ---------------------------------------------------------------------------


class TestTokenBucketAsync:
    @pytest.mark.asyncio
    async def test_acquire_immediate_within_rate(self):
        bucket = TokenBucketAsync(10.0)
        with patch("lolzpy._internal.rate_limit.asyncio.sleep") as mock_sleep:
            for _ in range(5):
                await bucket.acquire()
            mock_sleep.assert_not_called()

    @pytest.mark.asyncio
    async def test_acquire_throttles_at_capacity(self):
        monotonic, advance = _make_advancing_monotonic()

        with (
            patch("lolzpy._internal.rate_limit.time.monotonic", side_effect=monotonic),
            patch("lolzpy._internal.rate_limit.asyncio.sleep", side_effect=advance) as mock_sleep,
        ):
            bucket = TokenBucketAsync(2.0)
            await bucket.acquire()
            await bucket.acquire()
            await bucket.acquire()
            mock_sleep.assert_called_once()
            delay = mock_sleep.call_args[0][0]
            assert delay > 0

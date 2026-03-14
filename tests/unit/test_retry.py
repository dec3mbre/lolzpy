"""Tests for lolz_sdk._internal.retry — retry logic and delay calculation."""

from __future__ import annotations

import pytest

from lolz_sdk._internal.retry import _calculate_delay, _parse_retry_after, _should_retry
from lolz_sdk.core.config import RetryConfig

# ---------------------------------------------------------------------------
# RetryConfig
# ---------------------------------------------------------------------------


class TestRetryConfig:
    def test_defaults(self):
        cfg = RetryConfig()
        assert cfg.max_retries == 3
        assert cfg.initial_delay == 0.5
        assert cfg.max_delay == 8.0
        assert cfg.max_retry_after == 60.0
        assert 429 in cfg.retryable_statuses
        assert 502 in cfg.retryable_statuses

    def test_custom(self):
        cfg = RetryConfig(max_retries=5, initial_delay=1.0, max_delay=16.0)
        assert cfg.max_retries == 5
        assert cfg.initial_delay == 1.0
        assert cfg.max_delay == 16.0

    def test_frozen(self):
        cfg = RetryConfig()
        with pytest.raises(Exception, match="cannot assign|frozen"):
            cfg.max_retries = 10  # type: ignore[misc]


# ---------------------------------------------------------------------------
# _parse_retry_after
# ---------------------------------------------------------------------------


class TestParseRetryAfter:
    def test_valid_number(self):
        assert _parse_retry_after({"Retry-After": "5"}) == 5.0

    def test_float_value(self):
        assert _parse_retry_after({"retry-after": "2.5"}) == 2.5

    def test_zero_returns_none(self):
        assert _parse_retry_after({"Retry-After": "0"}) is None

    def test_negative_returns_none(self):
        assert _parse_retry_after({"Retry-After": "-1"}) is None

    def test_non_numeric(self):
        assert _parse_retry_after({"Retry-After": "abc"}) is None

    def test_missing_header(self):
        assert _parse_retry_after({}) is None

    def test_none_headers(self):
        assert _parse_retry_after(None) is None

    def test_no_get_method(self):
        assert _parse_retry_after(42) is None


# ---------------------------------------------------------------------------
# _calculate_delay
# ---------------------------------------------------------------------------


class TestCalculateDelay:
    def test_respects_retry_after_within_limit(self):
        cfg = RetryConfig(max_retry_after=60.0)
        assert _calculate_delay(0, 5.0, cfg) == 5.0

    def test_ignores_retry_after_above_limit(self):
        cfg = RetryConfig(max_retry_after=10.0, initial_delay=0.5)
        delay = _calculate_delay(0, 100.0, cfg)
        assert delay != 100.0
        assert delay >= cfg.initial_delay

    def test_exponential_backoff(self):
        cfg = RetryConfig(initial_delay=1.0, max_delay=32.0)
        d0 = _calculate_delay(0, None, cfg)
        d1 = _calculate_delay(1, None, cfg)
        d2 = _calculate_delay(2, None, cfg)
        # Each attempt roughly doubles (with jitter), but stays >= initial_delay
        assert d0 >= cfg.initial_delay
        assert d1 >= cfg.initial_delay
        assert d2 >= cfg.initial_delay

    def test_capped_at_max_delay(self):
        cfg = RetryConfig(initial_delay=1.0, max_delay=4.0)
        delay = _calculate_delay(10, None, cfg)  # 2^10 = 1024, should cap to 4
        assert delay <= cfg.max_delay * 1.01  # tiny tolerance for float

    def test_never_below_initial_delay(self):
        cfg = RetryConfig(initial_delay=2.0)
        for attempt in range(5):
            assert _calculate_delay(attempt, None, cfg) >= cfg.initial_delay


# ---------------------------------------------------------------------------
# _should_retry
# ---------------------------------------------------------------------------


class TestShouldRetry:
    def test_retryable_status_first_attempt(self):
        cfg = RetryConfig(max_retries=3)
        assert _should_retry(429, 0, cfg) is True

    def test_non_retryable_status(self):
        cfg = RetryConfig(max_retries=3)
        assert _should_retry(400, 0, cfg) is False

    def test_exhausted_attempts(self):
        cfg = RetryConfig(max_retries=3)
        assert _should_retry(429, 3, cfg) is False

    def test_last_valid_attempt(self):
        cfg = RetryConfig(max_retries=3)
        assert _should_retry(502, 2, cfg) is True

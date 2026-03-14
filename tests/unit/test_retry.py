"""Tests for lolzpy._internal.retry — retry logic and delay calculation."""

from __future__ import annotations

import pytest

from lolzpy._internal.retry import _calculate_delay, _notify_retry, _parse_retry_after, _should_retry
from lolzpy.core.config import DEFAULT_RETRY_ON, DEFAULT_RETRY_ON_EXCEPTIONS, RetryConfig

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
        assert cfg.retry_on == DEFAULT_RETRY_ON
        assert 429 in cfg.retry_on
        assert 502 in cfg.retry_on

    def test_custom(self):
        cfg = RetryConfig(max_retries=5, initial_delay=1.0, max_delay=16.0)
        assert cfg.max_retries == 5
        assert cfg.initial_delay == 1.0
        assert cfg.max_delay == 16.0

    def test_frozen(self):
        cfg = RetryConfig()
        with pytest.raises(Exception, match="cannot assign|frozen"):
            cfg.max_retries = 10  # type: ignore[misc]

    def test_retry_on_custom_list(self):
        cfg = RetryConfig(retry_on=[408, 429, 520])
        assert cfg.retry_on == frozenset({408, 429, 520})
        assert 500 not in cfg.retry_on

    def test_retry_on_accepts_set(self):
        cfg = RetryConfig(retry_on=frozenset({429, 503}))
        assert cfg.retry_on == frozenset({429, 503})

    def test_retry_on_exceptions_default(self):
        cfg = RetryConfig()
        assert cfg.retry_on_exceptions == DEFAULT_RETRY_ON_EXCEPTIONS
        assert ConnectionError in cfg.retry_on_exceptions
        assert TimeoutError in cfg.retry_on_exceptions
        assert OSError in cfg.retry_on_exceptions

    def test_retry_on_exceptions_custom_list(self):
        cfg = RetryConfig(retry_on_exceptions=[ConnectionError, ValueError])
        assert cfg.retry_on_exceptions == (ConnectionError, ValueError)
        assert isinstance(cfg.retry_on_exceptions, tuple)

    def test_retry_on_exceptions_accepts_tuple(self):
        exc = (IOError, RuntimeError)
        cfg = RetryConfig(retry_on_exceptions=exc)
        assert cfg.retry_on_exceptions == exc

    def test_on_retry_default_none(self):
        cfg = RetryConfig()
        assert cfg.on_retry is None

    def test_on_retry_accepts_callable(self):
        calls = []
        cb = lambda attempt, delay: calls.append((attempt, delay))
        cfg = RetryConfig(on_retry=cb)
        assert cfg.on_retry is cb

    def test_on_retry_excluded_from_eq(self):
        cb = lambda a, d: None
        cfg1 = RetryConfig(on_retry=cb)
        cfg2 = RetryConfig(on_retry=None)
        assert cfg1 == cfg2

    def test_frozen_with_on_retry(self):
        cb = lambda a, d: None
        cfg = RetryConfig(on_retry=cb)
        with pytest.raises(Exception, match="cannot assign|frozen"):
            cfg.on_retry = None  # type: ignore[misc]


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

    def test_custom_retry_on_includes_code(self):
        cfg = RetryConfig(max_retries=3, retry_on=[408, 520])
        assert _should_retry(408, 0, cfg) is True
        assert _should_retry(520, 0, cfg) is True

    def test_custom_retry_on_excludes_code(self):
        cfg = RetryConfig(max_retries=3, retry_on=[429])
        assert _should_retry(500, 0, cfg) is False


# ---------------------------------------------------------------------------
# _notify_retry
# ---------------------------------------------------------------------------


class TestNotifyRetry:
    def test_calls_on_retry_callback(self):
        calls: list[tuple[int, float]] = []
        cfg = RetryConfig(on_retry=lambda a, d: calls.append((a, d)))
        _notify_retry(cfg, 0, 1.5)
        _notify_retry(cfg, 1, 3.0)
        assert calls == [(0, 1.5), (1, 3.0)]

    def test_no_callback_is_noop(self):
        cfg = RetryConfig()
        _notify_retry(cfg, 0, 1.0)  # should not raise

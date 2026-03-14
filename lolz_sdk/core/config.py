"""Configuration dataclasses for lolz-sdk."""

from __future__ import annotations

from dataclasses import dataclass, field

RETRYABLE_STATUS_CODES: frozenset[int] = frozenset({429, 500, 502, 503, 504})


@dataclass(frozen=True, slots=True)
class RetryConfig:
    """Configuration for automatic request retries."""

    max_retries: int = 3
    initial_delay: float = 0.5
    max_delay: float = 8.0
    max_retry_after: float = 60.0
    retryable_statuses: frozenset[int] = field(default=RETRYABLE_STATUS_CODES)

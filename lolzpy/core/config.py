"""Configuration dataclasses for lolzpy."""

from __future__ import annotations

from dataclasses import dataclass, field

DEFAULT_RETRY_ON: frozenset[int] = frozenset({429, 500, 502, 503, 504})


@dataclass(frozen=True, slots=True)
class RetryConfig:
    """Configuration for automatic request retries."""

    max_retries: int = 3
    initial_delay: float = 0.5
    max_delay: float = 8.0
    max_retry_after: float = 60.0
    retry_on: frozenset[int] = field(default=DEFAULT_RETRY_ON)

    def __post_init__(self) -> None:
        if not isinstance(self.retry_on, frozenset):
            object.__setattr__(self, "retry_on", frozenset(self.retry_on))

"""lolzpy.core — public configuration and exception types."""

from lolzpy.core.config import RetryConfig
from lolzpy.core.exceptions import (
    AuthError,
    LolzError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    raise_for_status,
)
from lolzpy.core.types import T

__all__ = [
    "RetryConfig",
    "LolzError",
    "AuthError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "ValidationError",
    "raise_for_status",
    "T",
]

"""Type aliases and shared type definitions for lolz-sdk."""

from __future__ import annotations

from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

"""Type aliases and shared type definitions for lolzpy."""

from __future__ import annotations

from typing import Literal, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

BrowserType = Literal["chrome", "firefox", "safari", "edge"]

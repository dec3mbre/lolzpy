"""Shared fixtures for live API tests.

Set the LOLZ_TOKEN env var to run these tests:

    LOLZ_TOKEN=your_token pytest tests/live/ -v

Without the token all tests in this directory are skipped automatically.
"""

from __future__ import annotations

import os

import pytest

from lolzpy import LolzAsync, LolzSync

_TOKEN = os.environ.get("LOLZ_TOKEN")

pytestmark = pytest.mark.live

collect_ignore_glob: list[str] = []
if not _TOKEN:
    collect_ignore_glob.append("test_*.py")


@pytest.fixture(scope="session")
def token() -> str:
    assert _TOKEN, "LOLZ_TOKEN must be set"
    return _TOKEN


@pytest.fixture(scope="session")
def sync_client(token: str) -> LolzSync:
    client = LolzSync(token=token, rate_limit=3.0)
    yield client  # type: ignore[misc]
    client.close()


@pytest.fixture
def async_client(token: str) -> LolzAsync:
    return LolzAsync(token=token, rate_limit=3.0)

"""Tests for lolz_sdk._internal.base_client — BaseClient helpers and client construction."""

from __future__ import annotations

import pytest

from lolz_sdk._internal.base_client import AsyncAPIClient, BaseClient, SyncAPIClient, _clean_params
from lolz_sdk.core.config import RetryConfig

# ---------------------------------------------------------------------------
# _clean_params
# ---------------------------------------------------------------------------


class TestCleanParams:
    def test_removes_none_values(self):
        assert _clean_params({"a": 1, "b": None, "c": "x"}) == {"a": 1, "c": "x"}

    def test_returns_none_for_none_input(self):
        assert _clean_params(None) is None

    def test_empty_dict(self):
        assert _clean_params({}) == {}

    def test_all_none_values(self):
        assert _clean_params({"a": None, "b": None}) == {}


# ---------------------------------------------------------------------------
# BaseClient
# ---------------------------------------------------------------------------


class TestBaseClient:
    def test_url_building(self):
        client = BaseClient("https://api.example.com", "token123")
        assert client._url("/users/1") == "https://api.example.com/users/1"
        assert client._url("users/1") == "https://api.example.com/users/1"

    def test_url_strips_trailing_slash(self):
        client = BaseClient("https://api.example.com/", "token123")
        assert client._url("/test") == "https://api.example.com/test"

    def test_headers_contain_bearer_token(self):
        client = BaseClient("https://api.example.com", "my-secret-token")
        headers = client._headers()
        assert headers == {"Authorization": "Bearer my-secret-token"}

    def test_default_retry_config(self):
        client = BaseClient("https://api.example.com", "t")
        assert client._retry.max_retries == 3

    def test_custom_retry_config(self):
        cfg = RetryConfig(max_retries=5)
        client = BaseClient("https://api.example.com", "t", retry=cfg)
        assert client._retry.max_retries == 5


# ---------------------------------------------------------------------------
# SyncAPIClient
# ---------------------------------------------------------------------------


class TestSyncAPIClient:
    def test_construction(self):
        client = SyncAPIClient("https://api.example.com", "token")
        assert client._base_url == "https://api.example.com"
        client.close()

    def test_context_manager(self):
        with SyncAPIClient("https://api.example.com", "token") as client:
            assert client._base_url == "https://api.example.com"

    def test_proxy_passthrough(self):
        client = SyncAPIClient("https://api.example.com", "t", proxy="http://proxy:8080")
        assert client._proxy == "http://proxy:8080"
        client.close()

    def test_rate_limit_creates_limiter(self):
        client = SyncAPIClient("https://api.example.com", "t", rate_limit=5.0)
        assert client._limiter is not None
        client.close()

    def test_no_rate_limit_no_limiter(self):
        client = SyncAPIClient("https://api.example.com", "t", rate_limit=0.0)
        assert client._limiter is None
        client.close()


# ---------------------------------------------------------------------------
# AsyncAPIClient
# ---------------------------------------------------------------------------


class TestAsyncAPIClient:
    def test_construction(self):
        client = AsyncAPIClient("https://api.example.com", "token")
        assert client._base_url == "https://api.example.com"

    @pytest.mark.asyncio
    async def test_context_manager(self):
        async with AsyncAPIClient("https://api.example.com", "token") as client:
            assert client._base_url == "https://api.example.com"

    def test_rate_limit_creates_limiter(self):
        client = AsyncAPIClient("https://api.example.com", "t", rate_limit=5.0)
        assert client._limiter is not None

    def test_no_rate_limit_no_limiter(self):
        client = AsyncAPIClient("https://api.example.com", "t", rate_limit=0.0)
        assert client._limiter is None

"""Tests for the public API facade — LolzSync / LolzAsync."""

from __future__ import annotations

import inspect

import pytest

from lolz_sdk import LolzAsync, LolzSync, RetryConfig

# ---------------------------------------------------------------------------
# LolzSync
# ---------------------------------------------------------------------------


class TestLolzSync:
    def test_construction_defaults(self):
        client = LolzSync(token="t")
        assert client._forum_client._base_url == "https://prod-api.lolz.live"
        assert client._market_client._base_url == "https://prod-api.lzt.market"
        client.close()

    def test_construction_custom_urls(self):
        client = LolzSync(token="t", forum_base_url="https://f.test", market_base_url="https://m.test")
        assert client._forum_client._base_url == "https://f.test"
        assert client._market_client._base_url == "https://m.test"
        client.close()

    def test_forum_groups_exist(self):
        with LolzSync(token="t") as c:
            groups = [a for a in dir(c.forum) if not a.startswith("_")]
            assert "threads" in groups
            assert "posts" in groups
            assert "users" in groups
            assert len(groups) >= 15

    def test_market_groups_exist(self):
        with LolzSync(token="t") as c:
            groups = [a for a in dir(c.market) if not a.startswith("_")]
            assert "category" in groups
            assert "purchasing" in groups
            assert "managing" in groups
            assert len(groups) >= 10

    def test_context_manager(self):
        with LolzSync(token="t") as c:
            assert c.forum is not None
            assert c.market is not None

    def test_retry_config_forwarded(self):
        cfg = RetryConfig(max_retries=7)
        client = LolzSync(token="t", retry=cfg)
        assert client._forum_client._retry.max_retries == 7
        assert client._market_client._retry.max_retries == 7
        client.close()


# ---------------------------------------------------------------------------
# LolzAsync
# ---------------------------------------------------------------------------


class TestLolzAsync:
    def test_construction_defaults(self):
        client = LolzAsync(token="t")
        assert client._forum_client._base_url == "https://prod-api.lolz.live"
        assert client._market_client._base_url == "https://prod-api.lzt.market"

    @pytest.mark.asyncio
    async def test_context_manager(self):
        async with LolzAsync(token="t") as c:
            assert c.forum is not None
            assert c.market is not None

    def test_forum_groups_exist(self):
        client = LolzAsync(token="t")
        groups = [a for a in dir(client.forum) if not a.startswith("_")]
        assert "threads" in groups
        assert len(groups) >= 15

    def test_async_methods_are_coroutines(self):
        client = LolzAsync(token="t")
        assert inspect.iscoroutinefunction(client.forum.threads.list)
        assert inspect.iscoroutinefunction(client.market.purchasing.fast_buy)

    def test_sync_methods_are_not_coroutines(self):
        client = LolzSync(token="t")
        assert not inspect.iscoroutinefunction(client.forum.threads.list)
        assert not inspect.iscoroutinefunction(client.market.purchasing.fast_buy)
        client.close()


# ---------------------------------------------------------------------------
# Method signature checks
# ---------------------------------------------------------------------------


class TestMethodSignatures:
    def test_threads_create_params(self):
        with LolzSync(token="t") as c:
            sig = inspect.signature(c.forum.threads.create)
            params = list(sig.parameters.keys())
            assert "post_body" in params
            assert "forum_id" in params

    def test_purchasing_fast_buy_params(self):
        with LolzSync(token="t") as c:
            sig = inspect.signature(c.market.purchasing.fast_buy)
            params = list(sig.parameters.keys())
            assert "item_id" in params

    def test_bulk_get_item_id_is_list_int(self):
        """Verify the ItemIDModel $ref was resolved to int."""
        with LolzSync(token="t") as c:
            sig = inspect.signature(c.market.managing.bulk_get)
            annotation = str(sig.parameters["item_id"].annotation)
            assert "int" in annotation

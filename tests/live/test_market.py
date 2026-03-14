"""Live tests for Market API endpoints.

Run with: LOLZ_TOKEN=your_token pytest tests/live/test_market.py -v
"""

from __future__ import annotations

from lolzpy import LolzAsync, LolzSync
from lolzpy.market._models import UserModel

# ---------------------------------------------------------------------------
# Profile
# ---------------------------------------------------------------------------


class TestMarketProfile:
    def test_get_returns_user_model(self, sync_client: LolzSync):
        profile = sync_client.market.profile.get()
        assert isinstance(profile, UserModel)
        assert profile.user_id > 0
        assert isinstance(profile.username, str)

    def test_get_has_balance(self, sync_client: LolzSync):
        profile = sync_client.market.profile.get()
        assert profile.balance is not None

    async def test_async_get_returns_user_model(self, async_client: LolzAsync):
        profile = await async_client.market.profile.get()
        assert isinstance(profile, UserModel)
        assert profile.user_id > 0


# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------


class TestMarketCategory:
    def test_list_returns_categories(self, sync_client: LolzSync):
        result = sync_client.market.category.list()
        assert "categories" in result
        assert isinstance(result["categories"], list)
        assert len(result["categories"]) > 0

    def test_category_has_required_fields(self, sync_client: LolzSync):
        result = sync_client.market.category.list()
        cat = result["categories"][0]
        assert "category_id" in cat
        assert "category_name" in cat
        assert "category_title" in cat

    def test_params_returns_dict(self, sync_client: LolzSync):
        result = sync_client.market.category.params("steam")
        assert isinstance(result, dict)

    def test_steam_search(self, sync_client: LolzSync):
        result = sync_client.market.category.steam(pmax=50)
        assert "items" in result
        assert isinstance(result["items"], list)
        assert "totalItems" in result

    async def test_async_list(self, async_client: LolzAsync):
        result = await async_client.market.category.list()
        assert "categories" in result
        assert len(result["categories"]) > 0


# ---------------------------------------------------------------------------
# List
# ---------------------------------------------------------------------------


class TestMarketList:
    def test_user_items(self, sync_client: LolzSync):
        result = sync_client.market.list.user()
        assert "items" in result
        assert isinstance(result["items"], list)
        assert "totalItems" in result

    def test_states(self, sync_client: LolzSync):
        result = sync_client.market.list.states()
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Payments
# ---------------------------------------------------------------------------


class TestMarketPayments:
    def test_history_returns_dict(self, sync_client: LolzSync):
        result = sync_client.market.payments.history()
        assert "payments" in result

    def test_currency(self, sync_client: LolzSync):
        result = sync_client.market.payments.currency()
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Proxy
# ---------------------------------------------------------------------------


class TestMarketProxy:
    def test_get_returns_dict(self, sync_client: LolzSync):
        result = sync_client.market.proxy.get()
        assert isinstance(result, dict)

"""Live tests for Market API endpoints.

Run with: LOLZ_TOKEN=your_token pytest tests/live/test_market.py -v -s
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
        print(f"\n  user_id={profile.user_id}  username={profile.username}")
        assert isinstance(profile, UserModel)
        assert profile.user_id > 0
        assert isinstance(profile.username, str)

    def test_get_has_balance(self, sync_client: LolzSync):
        profile = sync_client.market.profile.get()
        print(f"\n  balance={profile.balance}")
        assert profile.balance is not None

    async def test_async_get_returns_user_model(self, async_client: LolzAsync):
        profile = await async_client.market.profile.get()
        print(f"\n  user_id={profile.user_id}  username={profile.username}")
        assert isinstance(profile, UserModel)
        assert profile.user_id > 0


# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------


class TestMarketCategory:
    def test_list_returns_categories(self, sync_client: LolzSync):
        result = sync_client.market.category.list()
        cats = result["categories"]
        print(f"\n  Categories count: {len(cats)}")
        print(f"  First 5: {[c.get('category_title', c.get('category_name')) for c in cats[:5]]}")
        assert "categories" in result
        assert isinstance(result["categories"], list)
        assert len(result["categories"]) > 0

    def test_category_has_required_fields(self, sync_client: LolzSync):
        result = sync_client.market.category.list()
        cat = result["categories"][0]
        print(f"\n  First category: id={cat['category_id']} name={cat['category_name']} title={cat['category_title']}")
        assert "category_id" in cat
        assert "category_name" in cat
        assert "category_title" in cat

    def test_params_returns_dict(self, sync_client: LolzSync):
        result = sync_client.market.category.params("steam")
        print(f"\n  Keys: {list(result.keys())}")
        assert isinstance(result, dict)

    def test_steam_search(self, sync_client: LolzSync):
        result = sync_client.market.category.steam(pmax=50)
        print(f"\n  totalItems={result.get('totalItems')}  items returned={len(result['items'])}")
        if result["items"]:
            first = result["items"][0]
            print(f"  First item keys: {list(first.keys())[:8]}")
        assert "items" in result
        assert isinstance(result["items"], list)
        assert "totalItems" in result

    async def test_async_list(self, async_client: LolzAsync):
        result = await async_client.market.category.list()
        print(f"\n  Categories count: {len(result['categories'])}")
        assert "categories" in result
        assert len(result["categories"]) > 0


# ---------------------------------------------------------------------------
# List
# ---------------------------------------------------------------------------


class TestMarketList:
    def test_user_items(self, sync_client: LolzSync):
        result = sync_client.market.list.user()
        print(f"\n  totalItems={result.get('totalItems')}  items returned={len(result['items'])}")
        assert "items" in result
        assert isinstance(result["items"], list)
        assert "totalItems" in result

    def test_states(self, sync_client: LolzSync):
        result = sync_client.market.list.states()
        print(f"\n  Keys: {list(result.keys())}")
        for k, v in result.items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)} items")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Payments
# ---------------------------------------------------------------------------


class TestMarketPayments:
    def test_history_returns_dict(self, sync_client: LolzSync):
        result = sync_client.market.payments.history()
        payments = result["payments"]
        print(f"\n  Payments count: {len(payments) if isinstance(payments, list) else type(payments).__name__}")
        if isinstance(payments, list) and payments:
            print(f"  First payment keys: {list(payments[0].keys())[:6]}")
        assert "payments" in result

    def test_currency(self, sync_client: LolzSync):
        result = sync_client.market.payments.currency()
        print(f"\n  Keys: {list(result.keys())}")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Proxy
# ---------------------------------------------------------------------------


class TestMarketProxy:
    def test_get_returns_dict(self, sync_client: LolzSync):
        result = sync_client.market.proxy.get()
        print(f"\n  Keys: {list(result.keys())}")
        for k, v in result.items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)} items")
            elif isinstance(v, dict):
                print(f"  {k}: {list(v.keys())[:5]}")
        assert isinstance(result, dict)

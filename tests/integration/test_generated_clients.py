"""Smoke tests for generated API client methods — verify correct HTTP method, path, and params."""

from __future__ import annotations

from unittest.mock import MagicMock

from lolzpy.forum._client import SyncConversations, SyncPosts, SyncThreads, SyncUsers
from lolzpy.market._client import SyncCategory, SyncManaging, SyncProfile, SyncPurchasing


def _mock_client() -> MagicMock:
    """Create a mock SyncAPIClient that captures _request calls."""
    client = MagicMock()
    client._request = MagicMock(return_value={"ok": True})
    return client


# ---------------------------------------------------------------------------
# Forum
# ---------------------------------------------------------------------------


class TestForumThreads:
    def test_list_passes_correct_args(self):
        client = _mock_client()
        threads = SyncThreads(client)
        threads.list(forum_id=5, page=2, title="test")

        client._request.assert_called_once()
        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/threads"
        params = kwargs["params"]
        assert params["forum_id"] == 5
        assert params["page"] == 2
        assert params["title"] == "test"

    def test_create_sends_json_body(self):
        client = _mock_client()
        threads = SyncThreads(client)
        threads.create(post_body="Hello world", forum_id=10, title="My thread")

        args, kwargs = client._request.call_args
        assert args[0] == "POST"
        assert args[1] == "/threads"
        json_data = kwargs["json"]
        assert json_data["post_body"] == "Hello world"
        assert json_data["forum_id"] == 10
        assert json_data["title"] == "My thread"

    def test_get_uses_path_param(self):
        client = _mock_client()
        threads = SyncThreads(client)
        threads.get(thread_id=42)

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/threads/42"


class TestForumUsers:
    def test_get_user(self):
        client = _mock_client()
        users = SyncUsers(client)
        users.get(user_id=4565608)

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/users/4565608"


class TestForumPosts:
    def test_list_passes_thread_id(self):
        client = _mock_client()
        posts = SyncPosts(client)
        posts.list(thread_id=99, page=3)

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/posts"
        assert kwargs["params"]["thread_id"] == 99
        assert kwargs["params"]["page"] == 3


class TestForumConversations:
    def test_list_without_params(self):
        client = _mock_client()
        convos = SyncConversations(client)
        convos.list()

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/conversations"


# ---------------------------------------------------------------------------
# Market
# ---------------------------------------------------------------------------


class TestMarketCategory:
    def test_all_passes_filters(self):
        client = _mock_client()
        category = SyncCategory(client)
        category.all(page=1, pmin=100, pmax=500, currency="usd")

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/"
        params = kwargs["params"]
        assert params["page"] == 1
        assert params["pmin"] == 100
        assert params["pmax"] == 500
        assert params["currency"] == "usd"

    def test_steam_category_path(self):
        client = _mock_client()
        category = SyncCategory(client)
        category.steam(page=1)

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/steam"

    def test_optional_params_excluded_when_none(self):
        client = _mock_client()
        category = SyncCategory(client)
        category.all()

        args, kwargs = client._request.call_args
        params = kwargs["params"]
        assert len(params) == 0


class TestMarketPurchasing:
    def test_fast_buy_with_item_id(self):
        client = _mock_client()
        purchasing = SyncPurchasing(client)
        purchasing.fast_buy(item_id=12345, price=99.99)

        args, kwargs = client._request.call_args
        assert args[0] == "POST"
        assert args[1] == "/12345/fast-buy"
        assert kwargs["json"]["price"] == 99.99


class TestMarketManaging:
    def test_bump(self):
        client = _mock_client()
        managing = SyncManaging(client)
        managing.bump(item_id=777)

        args, kwargs = client._request.call_args
        assert args[0] == "POST"
        assert args[1] == "/777/bump"


class TestMarketProfile:
    def test_get_profile(self):
        client = _mock_client()
        profile = SyncProfile(client)
        profile.get()

        args, kwargs = client._request.call_args
        assert args[0] == "GET"
        assert args[1] == "/me"

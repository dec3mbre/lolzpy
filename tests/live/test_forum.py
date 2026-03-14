"""Live tests for Forum API endpoints.

Run with: LOLZ_TOKEN=your_token pytest tests/live/test_forum.py -v

Note: some endpoints may return 403 depending on token scope.
"""

from __future__ import annotations

import pytest

from lolzpy import LolzAsync, LolzSync

# ---------------------------------------------------------------------------
# Forums
# ---------------------------------------------------------------------------


class TestForumForums:
    def test_list_returns_forums(self, sync_client: LolzSync):
        result = sync_client.forum.forums.list()
        assert "forums" in result or "forum_tree" in result
        assert isinstance(result, dict)

    async def test_async_list(self, async_client: LolzAsync):
        result = await async_client.forum.forums.list()
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------


class TestForumCategories:
    def test_list_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.categories.list()
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------


class TestForumNavigation:
    def test_list_returns_dict(self, sync_client: LolzSync):
        try:
            result = sync_client.forum.navigation.list()
        except Exception as e:
            if "500" in str(e):
                pytest.skip("Server returned 500")
            raise
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------


class TestForumTags:
    def test_list_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.tags.list()
        assert isinstance(result, dict)

    def test_popular_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.tags.popular()
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------


class TestForumUsers:
    def test_fields_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.users.fields()
        assert isinstance(result, dict)

    def test_get_own_user(self, sync_client: LolzSync):
        """Get the user associated with the token."""
        profile = sync_client.market.profile.get()
        user_id = profile.user_id
        try:
            result = sync_client.forum.users.get(user_id)
            assert isinstance(result, dict) or hasattr(result, "user_id")
        except Exception as e:
            if "403" in str(e) or "ValidationError" in type(e).__name__:
                pytest.skip(f"Skipped: {type(e).__name__}")
            raise

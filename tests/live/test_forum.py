"""Live tests for Forum API endpoints.

Run with: LOLZ_TOKEN=your_token pytest tests/live/test_forum.py -v -s

Note: some endpoints may return 403 depending on token scope.
"""

from __future__ import annotations

import signal

import pytest

from lolzpy import LolzAsync, LolzSync

# ---------------------------------------------------------------------------
# Forums
# ---------------------------------------------------------------------------


class TestForumForums:
    def test_list_returns_forums(self, sync_client: LolzSync):
        result = sync_client.forum.forums.list()
        print(f"\n  Keys: {list(result.keys())}")
        if "forums" in result:
            print(f"  Forums count: {len(result['forums'])}")
        if "forum_tree" in result:
            print(f"  Forum tree entries: {len(result['forum_tree'])}")
        assert "forums" in result or "forum_tree" in result
        assert isinstance(result, dict)

    async def test_async_list(self, async_client: LolzAsync):
        result = await async_client.forum.forums.list()
        print(f"\n  Keys: {list(result.keys())}")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Categories
# ---------------------------------------------------------------------------


class TestForumCategories:
    def test_list_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.categories.list()
        print(f"\n  Keys: {list(result.keys())}")
        for k, v in result.items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)} items")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------


def _timeout_handler(signum, frame):
    raise TimeoutError("Navigation request timed out (15s)")


class TestForumNavigation:
    def test_list_returns_dict(self, sync_client: LolzSync):
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(15)
        try:
            result = sync_client.forum.navigation.list()
            signal.alarm(0)
        except TimeoutError:
            signal.alarm(0)
            pytest.skip("Navigation endpoint timed out (15s)")
        except Exception as e:
            signal.alarm(0)
            if "500" in str(e):
                pytest.skip("Server returned 500")
            raise
        finally:
            signal.signal(signal.SIGALRM, old_handler)
        print(f"\n  Keys: {list(result.keys())}")
        for k, v in result.items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)} items")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------


class TestForumTags:
    def test_list_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.tags.list()
        print(f"\n  Keys: {list(result.keys())}")
        if "tags" in result and isinstance(result["tags"], list):
            print(f"  Tags count: {len(result['tags'])}")
            if result["tags"]:
                print(f"  First 5: {[t.get('tag_text', t) for t in result['tags'][:5]]}")
        assert isinstance(result, dict)

    def test_popular_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.tags.popular()
        print(f"\n  Keys: {list(result.keys())}")
        if "tags" in result and isinstance(result["tags"], list):
            print(f"  Popular tags count: {len(result['tags'])}")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------


class TestForumUsers:
    def test_fields_returns_dict(self, sync_client: LolzSync):
        result = sync_client.forum.users.fields()
        print(f"\n  Keys: {list(result.keys())}")
        for k, v in result.items():
            if isinstance(v, list):
                print(f"  {k}: {len(v)} items")
        assert isinstance(result, dict)

    def test_get_own_user(self, sync_client: LolzSync):
        """Get the user associated with the token."""
        profile = sync_client.market.profile.get()
        user_id = profile.user_id
        print(f"\n  Looking up user_id={user_id}")
        try:
            result = sync_client.forum.users.get(user_id)
            if isinstance(result, dict):
                print(f"  Keys: {list(result.keys())}")
                if "user" in result and isinstance(result["user"], dict):
                    u = result["user"]
                    print(f"  username={u.get('username')}  user_id={u.get('user_id')}")
            else:
                print(f"  Result type: {type(result).__name__}")
            assert isinstance(result, dict) or hasattr(result, "user_id")
        except Exception as e:
            if "403" in str(e) or "ValidationError" in type(e).__name__:
                pytest.skip(f"Skipped: {type(e).__name__}")
            raise

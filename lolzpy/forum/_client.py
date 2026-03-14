"""forum API client methods.

Auto-generated from OpenAPI spec — do not edit manually.
Regenerate with: python -m codegen.generate
"""

from __future__ import annotations

from typing import Any, Literal

from lolzpy._internal.base_client import AsyncAPIClient, SyncAPIClient
from lolzpy.forum._models import (
    RespChatboxMessageModel,
    RespConversationMessageModel,
    RespConversationModel,
    RespLinkModel,
    RespNotificationModel,
    RespPostCommentModel,
    RespPostModel,
    RespProfilePostCommentModel,
    RespProfilePostModel,
    RespThreadModel,
    RespUserModel,
)

# ===========================================================================
# O auth
# ===========================================================================


class SyncOAuth:
    """Synchronous O auth API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def token(
        self,
        *,
        grant_type: Literal["client_credentials"] | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        scope: list[Literal["basic", "read", "post", "conversate", "market", "payment", "invoice"]] | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        refresh_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Access Token"""
        data: dict[str, Any] = {}
        if grant_type is not None:
            data["grant_type"] = grant_type
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if scope is not None:
            data["scope"] = scope
        if code is not None:
            data["code"] = code
        if redirect_uri is not None:
            data["redirect_uri"] = redirect_uri
        if refresh_token is not None:
            data["refresh_token"] = refresh_token
        if username is not None:
            data["username"] = username
        if password is not None:
            data["password"] = password
        return self._client._request(
            "POST",
            "/oauth/token",
            data=data,
            **kwargs,
        )


class AsyncOAuth:
    """Asynchronous O auth API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def token(
        self,
        *,
        grant_type: Literal["client_credentials"] | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        scope: list[Literal["basic", "read", "post", "conversate", "market", "payment", "invoice"]] | None = None,
        code: str | None = None,
        redirect_uri: str | None = None,
        refresh_token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Access Token"""
        data: dict[str, Any] = {}
        if grant_type is not None:
            data["grant_type"] = grant_type
        if client_id is not None:
            data["client_id"] = client_id
        if client_secret is not None:
            data["client_secret"] = client_secret
        if scope is not None:
            data["scope"] = scope
        if code is not None:
            data["code"] = code
        if redirect_uri is not None:
            data["redirect_uri"] = redirect_uri
        if refresh_token is not None:
            data["refresh_token"] = refresh_token
        if username is not None:
            data["username"] = username
        if password is not None:
            data["password"] = password
        return await self._client._request(
            "POST",
            "/oauth/token",
            data=data,
            **kwargs,
        )


# ===========================================================================
# Assets
# ===========================================================================


class SyncAssets:
    """Synchronous Assets API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def css(
        self,
        *,
        css: list[str] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get CSS"""
        params: dict[str, Any] = {}
        if css is not None:
            params["css"] = css
        return self._client._request(
            "GET",
            "/css",
            params=params,
            **kwargs,
        )


class AsyncAssets:
    """Asynchronous Assets API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def css(
        self,
        *,
        css: list[str] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get CSS"""
        params: dict[str, Any] = {}
        if css is not None:
            params["css"] = css
        return await self._client._request(
            "GET",
            "/css",
            params=params,
            **kwargs,
        )


# ===========================================================================
# Categories
# ===========================================================================


class SyncCategories:
    """Synchronous Categories API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: Literal["natural", "list"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Categories"""
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        return self._client._request(
            "GET",
            "/categories",
            params=params,
            **kwargs,
        )

    def get(
        self,
        category_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Category"""
        return self._client._request(
            "GET",
            f"/categories/{category_id}",
            **kwargs,
        )


class AsyncCategories:
    """Asynchronous Categories API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: Literal["natural", "list"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Categories"""
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        return await self._client._request(
            "GET",
            "/categories",
            params=params,
            **kwargs,
        )

    async def get(
        self,
        category_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Category"""
        return await self._client._request(
            "GET",
            f"/categories/{category_id}",
            **kwargs,
        )


# ===========================================================================
# Forums
# ===========================================================================


class SyncForums:
    """Synchronous Forums API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: Literal["natural", "list"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forums"""
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        return self._client._request(
            "GET",
            "/forums",
            params=params,
            **kwargs,
        )

    def grouped(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forums Tree"""
        return self._client._request(
            "GET",
            "/forums/grouped",
            **kwargs,
        )

    def get(
        self,
        forum_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forum"""
        return self._client._request(
            "GET",
            f"/forums/{forum_id}",
            **kwargs,
        )

    def followers(
        self,
        forum_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followers"""
        return self._client._request(
            "GET",
            f"/forums/{forum_id}/followers",
            **kwargs,
        )

    def follow(
        self,
        forum_id: int,
        *,
        post: bool | None = None,
        alert: bool | None = None,
        email: bool | None = None,
        prefix_ids: list[int] | None = None,
        minimal_contest_amount: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Follow Forum"""
        json_data: dict[str, Any] = {}
        if post is not None:
            json_data["post"] = post
        if alert is not None:
            json_data["alert"] = alert
        if email is not None:
            json_data["email"] = email
        if prefix_ids is not None:
            json_data["prefix_ids"] = prefix_ids
        if minimal_contest_amount is not None:
            json_data["minimal_contest_amount"] = minimal_contest_amount
        return self._client._request(
            "POST",
            f"/forums/{forum_id}/followers",
            json=json_data,
            **kwargs,
        )

    def unfollow(
        self,
        forum_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unfollow Forum"""
        return self._client._request(
            "DELETE",
            f"/forums/{forum_id}/followers",
            **kwargs,
        )

    def followed(
        self,
        *,
        total: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followed Forums"""
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        return self._client._request(
            "GET",
            "/forums/followed",
            params=params,
            **kwargs,
        )

    def get_feed_options(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Feed Options"""
        return self._client._request(
            "GET",
            "/forums/feed/options",
            **kwargs,
        )

    def edit_feed_options(
        self,
        *,
        node_ids: list[int] | None = None,
        keywords: list[str] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Feed Options"""
        json_data: dict[str, Any] = {}
        if node_ids is not None:
            json_data["node_ids"] = node_ids
        if keywords is not None:
            json_data["keywords"] = keywords
        return self._client._request(
            "PUT",
            "/forums/feed/options",
            json=json_data,
            **kwargs,
        )


class AsyncForums:
    """Asynchronous Forums API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        parent_category_id: int | None = None,
        parent_forum_id: int | None = None,
        order: Literal["natural", "list"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forums"""
        params: dict[str, Any] = {}
        if parent_category_id is not None:
            params["parent_category_id"] = parent_category_id
        if parent_forum_id is not None:
            params["parent_forum_id"] = parent_forum_id
        if order is not None:
            params["order"] = order
        return await self._client._request(
            "GET",
            "/forums",
            params=params,
            **kwargs,
        )

    async def grouped(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forums Tree"""
        return await self._client._request(
            "GET",
            "/forums/grouped",
            **kwargs,
        )

    async def get(
        self,
        forum_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forum"""
        return await self._client._request(
            "GET",
            f"/forums/{forum_id}",
            **kwargs,
        )

    async def followers(
        self,
        forum_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followers"""
        return await self._client._request(
            "GET",
            f"/forums/{forum_id}/followers",
            **kwargs,
        )

    async def follow(
        self,
        forum_id: int,
        *,
        post: bool | None = None,
        alert: bool | None = None,
        email: bool | None = None,
        prefix_ids: list[int] | None = None,
        minimal_contest_amount: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Follow Forum"""
        json_data: dict[str, Any] = {}
        if post is not None:
            json_data["post"] = post
        if alert is not None:
            json_data["alert"] = alert
        if email is not None:
            json_data["email"] = email
        if prefix_ids is not None:
            json_data["prefix_ids"] = prefix_ids
        if minimal_contest_amount is not None:
            json_data["minimal_contest_amount"] = minimal_contest_amount
        return await self._client._request(
            "POST",
            f"/forums/{forum_id}/followers",
            json=json_data,
            **kwargs,
        )

    async def unfollow(
        self,
        forum_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unfollow Forum"""
        return await self._client._request(
            "DELETE",
            f"/forums/{forum_id}/followers",
            **kwargs,
        )

    async def followed(
        self,
        *,
        total: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followed Forums"""
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        return await self._client._request(
            "GET",
            "/forums/followed",
            params=params,
            **kwargs,
        )

    async def get_feed_options(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Feed Options"""
        return await self._client._request(
            "GET",
            "/forums/feed/options",
            **kwargs,
        )

    async def edit_feed_options(
        self,
        *,
        node_ids: list[int] | None = None,
        keywords: list[str] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Feed Options"""
        json_data: dict[str, Any] = {}
        if node_ids is not None:
            json_data["node_ids"] = node_ids
        if keywords is not None:
            json_data["keywords"] = keywords
        return await self._client._request(
            "PUT",
            "/forums/feed/options",
            json=json_data,
            **kwargs,
        )


# ===========================================================================
# Links
# ===========================================================================


class SyncLinks:
    """Synchronous Links API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        **kwargs: Any,
    ) -> list[RespLinkModel]:
        """Get Links Forum"""
        return self._client._request(
            "GET",
            "/link-forums",
            model=RespLinkModel,
            wrapper_key="link-forums",
            is_list=True,
            **kwargs,
        )

    def get(
        self,
        link_id: int,
        **kwargs: Any,
    ) -> RespLinkModel:
        """Get Link Forum"""
        return self._client._request(
            "GET",
            f"/link-forums/{link_id}",
            model=RespLinkModel,
            wrapper_key="link-forum",
            **kwargs,
        )


class AsyncLinks:
    """Asynchronous Links API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        **kwargs: Any,
    ) -> list[RespLinkModel]:
        """Get Links Forum"""
        return await self._client._request(
            "GET",
            "/link-forums",
            model=RespLinkModel,
            wrapper_key="link-forums",
            is_list=True,
            **kwargs,
        )

    async def get(
        self,
        link_id: int,
        **kwargs: Any,
    ) -> RespLinkModel:
        """Get Link Forum"""
        return await self._client._request(
            "GET",
            f"/link-forums/{link_id}",
            model=RespLinkModel,
            wrapper_key="link-forum",
            **kwargs,
        )


# ===========================================================================
# Pages
# ===========================================================================


class SyncPages:
    """Synchronous Pages API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        parent_page_id: int | None = None,
        order: Literal["natural", "list"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Pages"""
        params: dict[str, Any] = {}
        if parent_page_id is not None:
            params["parent_page_id"] = parent_page_id
        if order is not None:
            params["order"] = order
        return self._client._request(
            "GET",
            "/pages",
            params=params,
            **kwargs,
        )

    def get(
        self,
        page_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Page"""
        return self._client._request(
            "GET",
            f"/pages/{page_id}",
            **kwargs,
        )


class AsyncPages:
    """Asynchronous Pages API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        parent_page_id: int | None = None,
        order: Literal["natural", "list"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Pages"""
        params: dict[str, Any] = {}
        if parent_page_id is not None:
            params["parent_page_id"] = parent_page_id
        if order is not None:
            params["order"] = order
        return await self._client._request(
            "GET",
            "/pages",
            params=params,
            **kwargs,
        )

    async def get(
        self,
        page_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Page"""
        return await self._client._request(
            "GET",
            f"/pages/{page_id}",
            **kwargs,
        )


# ===========================================================================
# Navigation
# ===========================================================================


class SyncNavigation:
    """Synchronous Navigation API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        parent: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Navigation"""
        params: dict[str, Any] = {}
        if parent is not None:
            params["parent"] = parent
        return self._client._request(
            "GET",
            "/navigation",
            params=params,
            **kwargs,
        )


class AsyncNavigation:
    """Asynchronous Navigation API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        parent: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Navigation"""
        params: dict[str, Any] = {}
        if parent is not None:
            params["parent"] = parent
        return await self._client._request(
            "GET",
            "/navigation",
            params=params,
            **kwargs,
        )


# ===========================================================================
# Threads
# ===========================================================================


class SyncThreads:
    """Synchronous Threads API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        forum_id: int | None = None,
        tab: str | None = None,
        state: Literal["active", "closed"] | None = None,
        period: Literal["day", "week", "month", "year"] | None = None,
        title: str | None = None,
        title_only: bool | None = None,
        creator_user_id: int | None = None,
        sticky: bool | None = None,
        prefix_ids: list[int] | None = None,
        prefix_ids_not: list[int] | None = None,
        thread_tag_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: Literal[
            "post_date", "last_post_date", "reply_count", "reply_count_asc", "first_post_likes", "vote_count"
        ]
        | None = None,
        direction: Literal["asc", "desc"] | None = None,
        thread_create_date: int | None = None,
        thread_update_date: int | None = None,
        fields_include: list[Literal["*", "latest_posts"]] | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Threads"""
        params: dict[str, Any] = {}
        if forum_id is not None:
            params["forum_id"] = forum_id
        if tab is not None:
            params["tab"] = tab
        if state is not None:
            params["state"] = state
        if period is not None:
            params["period"] = period
        if title is not None:
            params["title"] = title
        if title_only is not None:
            params["title_only"] = title_only
        if creator_user_id is not None:
            params["creator_user_id"] = creator_user_id
        if sticky is not None:
            params["sticky"] = sticky
        if prefix_ids is not None:
            params["prefix_ids[]"] = prefix_ids
        if prefix_ids_not is not None:
            params["prefix_ids_not[]"] = prefix_ids_not
        if thread_tag_id is not None:
            params["thread_tag_id"] = thread_tag_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if direction is not None:
            params["direction"] = direction
        if thread_create_date is not None:
            params["thread_create_date"] = thread_create_date
        if thread_update_date is not None:
            params["thread_update_date"] = thread_update_date
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            "/threads",
            params=params,
            model=RespThreadModel,
            wrapper_key="threads",
            is_list=True,
            **kwargs,
        )

    def create(
        self,
        post_body: str,
        forum_id: int,
        *,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Create Thread"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if prefix_id is not None:
            json_data["prefix_id"] = prefix_id
        if tags is not None:
            json_data["tags"] = tags
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            json_data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            json_data["schedule_date"] = schedule_date
        if schedule_time is not None:
            json_data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            json_data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            json_data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            json_data["watch_thread_email"] = watch_thread_email
        return self._client._request(
            "POST",
            "/threads",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    def create_contest(
        self,
        post_body: str,
        contest_type: Literal["by_finish_date"],
        prize_type: Literal["money", "upgrades"],
        require_like_count: int,
        require_total_like_count: int,
        *,
        title: str | None = None,
        title_en: str | None = None,
        length_value: int | None = None,
        length_option: Literal["minutes", "hours", "days"] | None = None,
        count_winners: int | None = None,
        prize_data_money: float | None = None,
        is_money_places: bool | None = None,
        prize_data_places: list[float] | None = None,
        prize_data_upgrade: int | None = None,
        secret_answer: str | None = None,
        tags: list[str] | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Create Contest"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if contest_type is not None:
            json_data["contest_type"] = contest_type
        if length_value is not None:
            json_data["length_value"] = length_value
        if length_option is not None:
            json_data["length_option"] = length_option
        if prize_type is not None:
            json_data["prize_type"] = prize_type
        if count_winners is not None:
            json_data["count_winners"] = count_winners
        if prize_data_money is not None:
            json_data["prize_data_money"] = prize_data_money
        if is_money_places is not None:
            json_data["is_money_places"] = is_money_places
        if prize_data_places is not None:
            json_data["prize_data_places"] = prize_data_places
        if prize_data_upgrade is not None:
            json_data["prize_data_upgrade"] = prize_data_upgrade
        if require_like_count is not None:
            json_data["require_like_count"] = require_like_count
        if require_total_like_count is not None:
            json_data["require_total_like_count"] = require_total_like_count
        if secret_answer is not None:
            json_data["secret_answer"] = secret_answer
        if tags is not None:
            json_data["tags"] = tags
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            json_data["dont_alert_followers"] = dont_alert_followers
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if schedule_date is not None:
            json_data["schedule_date"] = schedule_date
        if schedule_time is not None:
            json_data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            json_data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            json_data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            json_data["watch_thread_email"] = watch_thread_email
        return self._client._request(
            "POST",
            "/contests",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    def claim(
        self,
        as_responder: str,
        as_is_market_deal: bool,
        as_amount: float,
        transfer_type: Literal["guarantor", "safe", "notsafe"],
        post_body: str,
        *,
        as_market_item_id: int | None = None,
        as_data: str | None = None,
        currency: Literal["rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try"] | None = None,
        pay_claim: Literal["now", "later"] | None = None,
        as_funds_receipt: str | None = None,
        as_tg_login_screenshot: str | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Create Claim"""
        json_data: dict[str, Any] = {}
        if as_responder is not None:
            json_data["as_responder"] = as_responder
        if as_is_market_deal is not None:
            json_data["as_is_market_deal"] = as_is_market_deal
        if as_market_item_id is not None:
            json_data["as_market_item_id"] = as_market_item_id
        if as_data is not None:
            json_data["as_data"] = as_data
        if as_amount is not None:
            json_data["as_amount"] = as_amount
        if currency is not None:
            json_data["currency"] = currency
        if transfer_type is not None:
            json_data["transfer_type"] = transfer_type
        if pay_claim is not None:
            json_data["pay_claim"] = pay_claim
        if as_funds_receipt is not None:
            json_data["as_funds_receipt"] = as_funds_receipt
        if as_tg_login_screenshot is not None:
            json_data["as_tg_login_screenshot"] = as_tg_login_screenshot
        if tags is not None:
            json_data["tags"] = tags
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            json_data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            json_data["schedule_date"] = schedule_date
        if schedule_time is not None:
            json_data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            json_data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            json_data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            json_data["watch_thread_email"] = watch_thread_email
        if post_body is not None:
            json_data["post_body"] = post_body
        return self._client._request(
            "POST",
            "/claims",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    def get(
        self,
        thread_id: int,
        *,
        fields_include: list[Literal["*", "latest_posts"]] | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Get Thread"""
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            f"/threads/{thread_id}",
            params=params,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    def edit(
        self,
        thread_id: int,
        *,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        discussion_open: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = None,
        comment_ignore_group: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Edit thread"""
        json_data: dict[str, Any] = {}
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if prefix_id is not None:
            json_data["prefix_id"] = prefix_id
        if tags is not None:
            json_data["tags"] = tags
        if discussion_open is not None:
            json_data["discussion_open"] = discussion_open
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        return self._client._request(
            "PUT",
            f"/threads/{thread_id}",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    def delete(
        self,
        thread_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Thread"""
        json_data: dict[str, Any] = {}
        if reason is not None:
            json_data["reason"] = reason
        return self._client._request(
            "DELETE",
            f"/threads/{thread_id}",
            json=json_data,
            **kwargs,
        )

    def move(
        self,
        thread_id: int,
        node_id: str,
        *,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        apply_thread_prefix: bool | None = None,
        send_alert: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Move Thread"""
        json_data: dict[str, Any] = {}
        if node_id is not None:
            json_data["node_id"] = node_id
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if prefix_id is not None:
            json_data["prefix_id"] = prefix_id
        if apply_thread_prefix is not None:
            json_data["apply_thread_prefix"] = apply_thread_prefix
        if send_alert is not None:
            json_data["send_alert"] = send_alert
        return self._client._request(
            "POST",
            f"/threads/{thread_id}/move",
            json=json_data,
            **kwargs,
        )

    def bump(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Bump Thread"""
        return self._client._request(
            "POST",
            f"/threads/{thread_id}/bump",
            **kwargs,
        )

    def hide(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Hide Thread"""
        return self._client._request(
            "POST",
            f"/threads/{thread_id}/hide",
            **kwargs,
        )

    def star(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Bookmark Thread"""
        return self._client._request(
            "POST",
            f"/threads/{thread_id}/star",
            **kwargs,
        )

    def unstar(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unbookmark Thread"""
        return self._client._request(
            "DELETE",
            f"/threads/{thread_id}/star",
            **kwargs,
        )

    def followers(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Thread Followers"""
        return self._client._request(
            "GET",
            f"/threads/{thread_id}/followers",
            **kwargs,
        )

    def follow(
        self,
        thread_id: int,
        *,
        email: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Follow Thread"""
        json_data: dict[str, Any] = {}
        if email is not None:
            json_data["email"] = email
        return self._client._request(
            "POST",
            f"/threads/{thread_id}/followers",
            json=json_data,
            **kwargs,
        )

    def unfollow(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unfollow Thread"""
        return self._client._request(
            "DELETE",
            f"/threads/{thread_id}/followers",
            **kwargs,
        )

    def followed(
        self,
        *,
        total: bool | None = None,
        fields_include: list[Literal["*", "latest_posts"]] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followed Threads"""
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            "/threads/followed",
            params=params,
            **kwargs,
        )

    def navigation(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Navigation Elements"""
        return self._client._request(
            "GET",
            f"/threads/{thread_id}/navigation",
            **kwargs,
        )

    def get_poll(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Poll"""
        return self._client._request(
            "GET",
            f"/threads/{thread_id}/poll",
            **kwargs,
        )

    def vote(
        self,
        thread_id: int,
        *,
        response_id: int | None = None,
        response_ids: list[int] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Vote Poll"""
        json_data: dict[str, Any] = {}
        if response_id is not None:
            json_data["response_id"] = response_id
        if response_ids is not None:
            json_data["response_ids"] = response_ids
        return self._client._request(
            "POST",
            f"/threads/{thread_id}/poll/votes",
            json=json_data,
            **kwargs,
        )

    def unread(
        self,
        *,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Unread Threads"""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        return self._client._request(
            "GET",
            "/threads/new",
            params=params,
            model=RespThreadModel,
            wrapper_key="threads",
            is_list=True,
            **kwargs,
        )

    def recent(
        self,
        *,
        days: int | None = None,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Recent Threads"""
        params: dict[str, Any] = {}
        if days is not None:
            params["days"] = days
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        return self._client._request(
            "GET",
            "/threads/recent",
            params=params,
            model=RespThreadModel,
            wrapper_key="threads",
            is_list=True,
            **kwargs,
        )

    def finish(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Finish Contest"""
        return self._client._request(
            "POST",
            f"/contests/{thread_id}/finish",
            **kwargs,
        )


class AsyncThreads:
    """Asynchronous Threads API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        forum_id: int | None = None,
        tab: str | None = None,
        state: Literal["active", "closed"] | None = None,
        period: Literal["day", "week", "month", "year"] | None = None,
        title: str | None = None,
        title_only: bool | None = None,
        creator_user_id: int | None = None,
        sticky: bool | None = None,
        prefix_ids: list[int] | None = None,
        prefix_ids_not: list[int] | None = None,
        thread_tag_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: Literal[
            "post_date", "last_post_date", "reply_count", "reply_count_asc", "first_post_likes", "vote_count"
        ]
        | None = None,
        direction: Literal["asc", "desc"] | None = None,
        thread_create_date: int | None = None,
        thread_update_date: int | None = None,
        fields_include: list[Literal["*", "latest_posts"]] | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Threads"""
        params: dict[str, Any] = {}
        if forum_id is not None:
            params["forum_id"] = forum_id
        if tab is not None:
            params["tab"] = tab
        if state is not None:
            params["state"] = state
        if period is not None:
            params["period"] = period
        if title is not None:
            params["title"] = title
        if title_only is not None:
            params["title_only"] = title_only
        if creator_user_id is not None:
            params["creator_user_id"] = creator_user_id
        if sticky is not None:
            params["sticky"] = sticky
        if prefix_ids is not None:
            params["prefix_ids[]"] = prefix_ids
        if prefix_ids_not is not None:
            params["prefix_ids_not[]"] = prefix_ids_not
        if thread_tag_id is not None:
            params["thread_tag_id"] = thread_tag_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if direction is not None:
            params["direction"] = direction
        if thread_create_date is not None:
            params["thread_create_date"] = thread_create_date
        if thread_update_date is not None:
            params["thread_update_date"] = thread_update_date
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            "/threads",
            params=params,
            model=RespThreadModel,
            wrapper_key="threads",
            is_list=True,
            **kwargs,
        )

    async def create(
        self,
        post_body: str,
        forum_id: int,
        *,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Create Thread"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if prefix_id is not None:
            json_data["prefix_id"] = prefix_id
        if tags is not None:
            json_data["tags"] = tags
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            json_data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            json_data["schedule_date"] = schedule_date
        if schedule_time is not None:
            json_data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            json_data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            json_data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            json_data["watch_thread_email"] = watch_thread_email
        return await self._client._request(
            "POST",
            "/threads",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    async def create_contest(
        self,
        post_body: str,
        contest_type: Literal["by_finish_date"],
        prize_type: Literal["money", "upgrades"],
        require_like_count: int,
        require_total_like_count: int,
        *,
        title: str | None = None,
        title_en: str | None = None,
        length_value: int | None = None,
        length_option: Literal["minutes", "hours", "days"] | None = None,
        count_winners: int | None = None,
        prize_data_money: float | None = None,
        is_money_places: bool | None = None,
        prize_data_places: list[float] | None = None,
        prize_data_upgrade: int | None = None,
        secret_answer: str | None = None,
        tags: list[str] | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Create Contest"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if contest_type is not None:
            json_data["contest_type"] = contest_type
        if length_value is not None:
            json_data["length_value"] = length_value
        if length_option is not None:
            json_data["length_option"] = length_option
        if prize_type is not None:
            json_data["prize_type"] = prize_type
        if count_winners is not None:
            json_data["count_winners"] = count_winners
        if prize_data_money is not None:
            json_data["prize_data_money"] = prize_data_money
        if is_money_places is not None:
            json_data["is_money_places"] = is_money_places
        if prize_data_places is not None:
            json_data["prize_data_places"] = prize_data_places
        if prize_data_upgrade is not None:
            json_data["prize_data_upgrade"] = prize_data_upgrade
        if require_like_count is not None:
            json_data["require_like_count"] = require_like_count
        if require_total_like_count is not None:
            json_data["require_total_like_count"] = require_total_like_count
        if secret_answer is not None:
            json_data["secret_answer"] = secret_answer
        if tags is not None:
            json_data["tags"] = tags
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            json_data["dont_alert_followers"] = dont_alert_followers
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if schedule_date is not None:
            json_data["schedule_date"] = schedule_date
        if schedule_time is not None:
            json_data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            json_data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            json_data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            json_data["watch_thread_email"] = watch_thread_email
        return await self._client._request(
            "POST",
            "/contests",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    async def claim(
        self,
        as_responder: str,
        as_is_market_deal: bool,
        as_amount: float,
        transfer_type: Literal["guarantor", "safe", "notsafe"],
        post_body: str,
        *,
        as_market_item_id: int | None = None,
        as_data: str | None = None,
        currency: Literal["rub", "uah", "kzt", "byn", "usd", "eur", "gbp", "cny", "try"] | None = None,
        pay_claim: Literal["now", "later"] | None = None,
        as_funds_receipt: str | None = None,
        as_tg_login_screenshot: str | None = None,
        tags: list[str] | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = 2,
        comment_ignore_group: bool | None = None,
        dont_alert_followers: bool | None = None,
        schedule_date: str | None = None,
        schedule_time: str | None = None,
        watch_thread_state: bool | None = None,
        watch_thread: bool | None = None,
        watch_thread_email: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Create Claim"""
        json_data: dict[str, Any] = {}
        if as_responder is not None:
            json_data["as_responder"] = as_responder
        if as_is_market_deal is not None:
            json_data["as_is_market_deal"] = as_is_market_deal
        if as_market_item_id is not None:
            json_data["as_market_item_id"] = as_market_item_id
        if as_data is not None:
            json_data["as_data"] = as_data
        if as_amount is not None:
            json_data["as_amount"] = as_amount
        if currency is not None:
            json_data["currency"] = currency
        if transfer_type is not None:
            json_data["transfer_type"] = transfer_type
        if pay_claim is not None:
            json_data["pay_claim"] = pay_claim
        if as_funds_receipt is not None:
            json_data["as_funds_receipt"] = as_funds_receipt
        if as_tg_login_screenshot is not None:
            json_data["as_tg_login_screenshot"] = as_tg_login_screenshot
        if tags is not None:
            json_data["tags"] = tags
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        if dont_alert_followers is not None:
            json_data["dont_alert_followers"] = dont_alert_followers
        if schedule_date is not None:
            json_data["schedule_date"] = schedule_date
        if schedule_time is not None:
            json_data["schedule_time"] = schedule_time
        if watch_thread_state is not None:
            json_data["watch_thread_state"] = watch_thread_state
        if watch_thread is not None:
            json_data["watch_thread"] = watch_thread
        if watch_thread_email is not None:
            json_data["watch_thread_email"] = watch_thread_email
        if post_body is not None:
            json_data["post_body"] = post_body
        return await self._client._request(
            "POST",
            "/claims",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    async def get(
        self,
        thread_id: int,
        *,
        fields_include: list[Literal["*", "latest_posts"]] | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Get Thread"""
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            f"/threads/{thread_id}",
            params=params,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    async def edit(
        self,
        thread_id: int,
        *,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        tags: list[str] | None = None,
        discussion_open: bool | None = None,
        hide_contacts: bool | None = None,
        allow_ask_hidden_content: bool | None = None,
        reply_group: int | None = None,
        comment_ignore_group: bool | None = None,
        **kwargs: Any,
    ) -> RespThreadModel:
        """Edit thread"""
        json_data: dict[str, Any] = {}
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if prefix_id is not None:
            json_data["prefix_id"] = prefix_id
        if tags is not None:
            json_data["tags"] = tags
        if discussion_open is not None:
            json_data["discussion_open"] = discussion_open
        if hide_contacts is not None:
            json_data["hide_contacts"] = hide_contacts
        if allow_ask_hidden_content is not None:
            json_data["allow_ask_hidden_content"] = allow_ask_hidden_content
        if reply_group is not None:
            json_data["reply_group"] = reply_group
        if comment_ignore_group is not None:
            json_data["comment_ignore_group"] = comment_ignore_group
        return await self._client._request(
            "PUT",
            f"/threads/{thread_id}",
            json=json_data,
            model=RespThreadModel,
            wrapper_key="thread",
            **kwargs,
        )

    async def delete(
        self,
        thread_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Thread"""
        json_data: dict[str, Any] = {}
        if reason is not None:
            json_data["reason"] = reason
        return await self._client._request(
            "DELETE",
            f"/threads/{thread_id}",
            json=json_data,
            **kwargs,
        )

    async def move(
        self,
        thread_id: int,
        node_id: str,
        *,
        title: str | None = None,
        title_en: str | None = None,
        prefix_id: list[int] | None = None,
        apply_thread_prefix: bool | None = None,
        send_alert: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Move Thread"""
        json_data: dict[str, Any] = {}
        if node_id is not None:
            json_data["node_id"] = node_id
        if title is not None:
            json_data["title"] = title
        if title_en is not None:
            json_data["title_en"] = title_en
        if prefix_id is not None:
            json_data["prefix_id"] = prefix_id
        if apply_thread_prefix is not None:
            json_data["apply_thread_prefix"] = apply_thread_prefix
        if send_alert is not None:
            json_data["send_alert"] = send_alert
        return await self._client._request(
            "POST",
            f"/threads/{thread_id}/move",
            json=json_data,
            **kwargs,
        )

    async def bump(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Bump Thread"""
        return await self._client._request(
            "POST",
            f"/threads/{thread_id}/bump",
            **kwargs,
        )

    async def hide(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Hide Thread"""
        return await self._client._request(
            "POST",
            f"/threads/{thread_id}/hide",
            **kwargs,
        )

    async def star(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Bookmark Thread"""
        return await self._client._request(
            "POST",
            f"/threads/{thread_id}/star",
            **kwargs,
        )

    async def unstar(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unbookmark Thread"""
        return await self._client._request(
            "DELETE",
            f"/threads/{thread_id}/star",
            **kwargs,
        )

    async def followers(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Thread Followers"""
        return await self._client._request(
            "GET",
            f"/threads/{thread_id}/followers",
            **kwargs,
        )

    async def follow(
        self,
        thread_id: int,
        *,
        email: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Follow Thread"""
        json_data: dict[str, Any] = {}
        if email is not None:
            json_data["email"] = email
        return await self._client._request(
            "POST",
            f"/threads/{thread_id}/followers",
            json=json_data,
            **kwargs,
        )

    async def unfollow(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unfollow Thread"""
        return await self._client._request(
            "DELETE",
            f"/threads/{thread_id}/followers",
            **kwargs,
        )

    async def followed(
        self,
        *,
        total: bool | None = None,
        fields_include: list[Literal["*", "latest_posts"]] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followed Threads"""
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            "/threads/followed",
            params=params,
            **kwargs,
        )

    async def navigation(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Navigation Elements"""
        return await self._client._request(
            "GET",
            f"/threads/{thread_id}/navigation",
            **kwargs,
        )

    async def get_poll(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Poll"""
        return await self._client._request(
            "GET",
            f"/threads/{thread_id}/poll",
            **kwargs,
        )

    async def vote(
        self,
        thread_id: int,
        *,
        response_id: int | None = None,
        response_ids: list[int] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Vote Poll"""
        json_data: dict[str, Any] = {}
        if response_id is not None:
            json_data["response_id"] = response_id
        if response_ids is not None:
            json_data["response_ids"] = response_ids
        return await self._client._request(
            "POST",
            f"/threads/{thread_id}/poll/votes",
            json=json_data,
            **kwargs,
        )

    async def unread(
        self,
        *,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Unread Threads"""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        return await self._client._request(
            "GET",
            "/threads/new",
            params=params,
            model=RespThreadModel,
            wrapper_key="threads",
            is_list=True,
            **kwargs,
        )

    async def recent(
        self,
        *,
        days: int | None = None,
        limit: int | None = None,
        forum_id: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Recent Threads"""
        params: dict[str, Any] = {}
        if days is not None:
            params["days"] = days
        if limit is not None:
            params["limit"] = limit
        if forum_id is not None:
            params["forum_id"] = forum_id
        if data_limit is not None:
            params["data_limit"] = data_limit
        return await self._client._request(
            "GET",
            "/threads/recent",
            params=params,
            model=RespThreadModel,
            wrapper_key="threads",
            is_list=True,
            **kwargs,
        )

    async def finish(
        self,
        thread_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Finish Contest"""
        return await self._client._request(
            "POST",
            f"/contests/{thread_id}/finish",
            **kwargs,
        )


# ===========================================================================
# Posts
# ===========================================================================


class SyncPosts:
    """Synchronous Posts API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        thread_id: int | None = None,
        page_of_post_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: Literal["natural", "natural_reverse", "post_likes", "post_likes_reverse"] | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Posts"""
        params: dict[str, Any] = {}
        if thread_id is not None:
            params["thread_id"] = thread_id
        if page_of_post_id is not None:
            params["page_of_post_id"] = page_of_post_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        return self._client._request(
            "GET",
            "/posts",
            params=params,
            model=RespThreadModel,
            wrapper_key="posts",
            is_list=True,
            **kwargs,
        )

    def create(
        self,
        post_body: str,
        *,
        thread_id: int | None = None,
        quote_post_id: int | None = None,
        **kwargs: Any,
    ) -> RespPostModel:
        """Create Post"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if thread_id is not None:
            json_data["thread_id"] = thread_id
        if quote_post_id is not None:
            json_data["quote_post_id"] = quote_post_id
        return self._client._request(
            "POST",
            "/posts",
            json=json_data,
            model=RespPostModel,
            wrapper_key="post",
            **kwargs,
        )

    def get(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> RespPostModel:
        """Get Post"""
        return self._client._request(
            "GET",
            f"/posts/{post_id}",
            model=RespPostModel,
            wrapper_key="post",
            **kwargs,
        )

    def edit(
        self,
        post_id: int,
        *,
        post_body: str | None = None,
        **kwargs: Any,
    ) -> RespPostModel:
        """Edit Post"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        return self._client._request(
            "PUT",
            f"/posts/{post_id}",
            json=json_data,
            model=RespPostModel,
            wrapper_key="post",
            **kwargs,
        )

    def delete(
        self,
        post_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Post"""
        json_data: dict[str, Any] = {}
        if reason is not None:
            json_data["reason"] = reason
        return self._client._request(
            "DELETE",
            f"/posts/{post_id}",
            json=json_data,
            **kwargs,
        )

    def likes(
        self,
        post_id: int,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Post Likes"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            f"/posts/{post_id}/likes",
            params=params,
            **kwargs,
        )

    def like(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Like Post"""
        return self._client._request(
            "POST",
            f"/posts/{post_id}/likes",
            **kwargs,
        )

    def unlike(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unlike Post"""
        return self._client._request(
            "DELETE",
            f"/posts/{post_id}/likes",
            **kwargs,
        )

    def report_reasons(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Post Report Reasons"""
        return self._client._request(
            "GET",
            f"/posts/{post_id}/report",
            **kwargs,
        )

    def report(
        self,
        post_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report Post"""
        json_data: dict[str, Any] = {}
        if message is not None:
            json_data["message"] = message
        return self._client._request(
            "POST",
            f"/posts/{post_id}/report",
            json=json_data,
            **kwargs,
        )

    def get_comments(
        self,
        post_id: int,
        *,
        before: int | None = None,
        before_comment: int | None = None,
        **kwargs: Any,
    ) -> list[RespPostCommentModel]:
        """Get Post Comments"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if before is not None:
            params["before"] = before
        if before_comment is not None:
            params["before_comment"] = before_comment
        return self._client._request(
            "GET",
            "/posts/comments",
            params=params,
            model=RespPostCommentModel,
            wrapper_key="comments",
            is_list=True,
            **kwargs,
        )

    def create_comments(
        self,
        post_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Post Comment"""
        json_data: dict[str, Any] = {}
        if post_id is not None:
            json_data["post_id"] = post_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return self._client._request(
            "POST",
            "/posts/comments",
            json=json_data,
            **kwargs,
        )

    def edit_comments(
        self,
        post_comment_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Post Comment"""
        json_data: dict[str, Any] = {}
        if post_comment_id is not None:
            json_data["post_comment_id"] = post_comment_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return self._client._request(
            "PUT",
            "/posts/comments",
            json=json_data,
            **kwargs,
        )

    def delete_comments(
        self,
        post_comment_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Post Comment"""
        json_data: dict[str, Any] = {}
        if post_comment_id is not None:
            json_data["post_comment_id"] = post_comment_id
        if reason is not None:
            json_data["reason"] = reason
        return self._client._request(
            "DELETE",
            "/posts/comments",
            json=json_data,
            **kwargs,
        )

    def report_comments(
        self,
        post_comment_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report Post Comment"""
        json_data: dict[str, Any] = {}
        if post_comment_id is not None:
            json_data["post_comment_id"] = post_comment_id
        if message is not None:
            json_data["message"] = message
        return self._client._request(
            "POST",
            "/posts/comments/report",
            json=json_data,
            **kwargs,
        )


class AsyncPosts:
    """Asynchronous Posts API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        thread_id: int | None = None,
        page_of_post_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        order: Literal["natural", "natural_reverse", "post_likes", "post_likes_reverse"] | None = None,
        **kwargs: Any,
    ) -> list[RespThreadModel]:
        """Get Posts"""
        params: dict[str, Any] = {}
        if thread_id is not None:
            params["thread_id"] = thread_id
        if page_of_post_id is not None:
            params["page_of_post_id"] = page_of_post_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        return await self._client._request(
            "GET",
            "/posts",
            params=params,
            model=RespThreadModel,
            wrapper_key="posts",
            is_list=True,
            **kwargs,
        )

    async def create(
        self,
        post_body: str,
        *,
        thread_id: int | None = None,
        quote_post_id: int | None = None,
        **kwargs: Any,
    ) -> RespPostModel:
        """Create Post"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if thread_id is not None:
            json_data["thread_id"] = thread_id
        if quote_post_id is not None:
            json_data["quote_post_id"] = quote_post_id
        return await self._client._request(
            "POST",
            "/posts",
            json=json_data,
            model=RespPostModel,
            wrapper_key="post",
            **kwargs,
        )

    async def get(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> RespPostModel:
        """Get Post"""
        return await self._client._request(
            "GET",
            f"/posts/{post_id}",
            model=RespPostModel,
            wrapper_key="post",
            **kwargs,
        )

    async def edit(
        self,
        post_id: int,
        *,
        post_body: str | None = None,
        **kwargs: Any,
    ) -> RespPostModel:
        """Edit Post"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        return await self._client._request(
            "PUT",
            f"/posts/{post_id}",
            json=json_data,
            model=RespPostModel,
            wrapper_key="post",
            **kwargs,
        )

    async def delete(
        self,
        post_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Post"""
        json_data: dict[str, Any] = {}
        if reason is not None:
            json_data["reason"] = reason
        return await self._client._request(
            "DELETE",
            f"/posts/{post_id}",
            json=json_data,
            **kwargs,
        )

    async def likes(
        self,
        post_id: int,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Post Likes"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            f"/posts/{post_id}/likes",
            params=params,
            **kwargs,
        )

    async def like(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Like Post"""
        return await self._client._request(
            "POST",
            f"/posts/{post_id}/likes",
            **kwargs,
        )

    async def unlike(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unlike Post"""
        return await self._client._request(
            "DELETE",
            f"/posts/{post_id}/likes",
            **kwargs,
        )

    async def report_reasons(
        self,
        post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Post Report Reasons"""
        return await self._client._request(
            "GET",
            f"/posts/{post_id}/report",
            **kwargs,
        )

    async def report(
        self,
        post_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report Post"""
        json_data: dict[str, Any] = {}
        if message is not None:
            json_data["message"] = message
        return await self._client._request(
            "POST",
            f"/posts/{post_id}/report",
            json=json_data,
            **kwargs,
        )

    async def get_comments(
        self,
        post_id: int,
        *,
        before: int | None = None,
        before_comment: int | None = None,
        **kwargs: Any,
    ) -> list[RespPostCommentModel]:
        """Get Post Comments"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if before is not None:
            params["before"] = before
        if before_comment is not None:
            params["before_comment"] = before_comment
        return await self._client._request(
            "GET",
            "/posts/comments",
            params=params,
            model=RespPostCommentModel,
            wrapper_key="comments",
            is_list=True,
            **kwargs,
        )

    async def create_comments(
        self,
        post_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Post Comment"""
        json_data: dict[str, Any] = {}
        if post_id is not None:
            json_data["post_id"] = post_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return await self._client._request(
            "POST",
            "/posts/comments",
            json=json_data,
            **kwargs,
        )

    async def edit_comments(
        self,
        post_comment_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Post Comment"""
        json_data: dict[str, Any] = {}
        if post_comment_id is not None:
            json_data["post_comment_id"] = post_comment_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return await self._client._request(
            "PUT",
            "/posts/comments",
            json=json_data,
            **kwargs,
        )

    async def delete_comments(
        self,
        post_comment_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Post Comment"""
        json_data: dict[str, Any] = {}
        if post_comment_id is not None:
            json_data["post_comment_id"] = post_comment_id
        if reason is not None:
            json_data["reason"] = reason
        return await self._client._request(
            "DELETE",
            "/posts/comments",
            json=json_data,
            **kwargs,
        )

    async def report_comments(
        self,
        post_comment_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report Post Comment"""
        json_data: dict[str, Any] = {}
        if post_comment_id is not None:
            json_data["post_comment_id"] = post_comment_id
        if message is not None:
            json_data["message"] = message
        return await self._client._request(
            "POST",
            "/posts/comments/report",
            json=json_data,
            **kwargs,
        )


# ===========================================================================
# Users
# ===========================================================================


class SyncUsers:
    """Synchronous Users API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[Literal["*", "alerts"]] | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Get Users"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            "/users",
            params=params,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    def fields(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Fields"""
        return self._client._request(
            "GET",
            "/users/fields",
            **kwargs,
        )

    def find(
        self,
        *,
        username: str | None = None,
        custom_fields: dict[str, Any] | None = None,
        fields_include: list[Literal["*", "alerts"]] | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Find Users"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if custom_fields is not None:
            params["custom_fields"] = custom_fields
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            "/users/find",
            params=params,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    def get(
        self,
        user_id: Any,
        *,
        fields_include: list[Literal["*", "alerts"]] | None = None,
        **kwargs: Any,
    ) -> RespUserModel:
        """Get User"""
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            f"/users/{user_id}",
            params=params,
            model=RespUserModel,
            wrapper_key="user",
            **kwargs,
        )

    def edit(
        self,
        user_id: Any,
        *,
        username: str | None = None,
        user_title: str | None = None,
        display_group_id: int | None = None,
        display_icon_group_id: int | None = None,
        display_banner_id: int | None = None,
        conv_welcome_message: str | None = None,
        user_dob_day: int | None = None,
        user_dob_month: int | None = None,
        user_dob_year: int | None = None,
        secret_answer: str | None = None,
        secret_answer_type: int | None = None,
        short_link: str | None = None,
        language_id: int | None = None,
        gender: Literal["", "male", "female"] | None = None,
        timezone: str | None = None,
        receive_admin_email: bool | None = None,
        activity_visible: bool | None = None,
        show_dob_date: bool | None = None,
        show_dob_year: bool | None = None,
        hide_username_change_logs: bool | None = None,
        allow_view_profile: Literal["none", "members", "followed"] | None = None,
        allow_post_profile: Literal["none", "members", "followed"] | None = None,
        allow_send_personal_conversation: Literal["none", "members", "followed"] | None = None,
        allow_invite_group: Literal["none", "members", "followed"] | None = None,
        allow_receive_news_feed: Literal["none", "members", "followed"] | None = None,
        alert: dict[str, Any] | None = None,
        fields: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit User"""
        json_data: dict[str, Any] = {}
        if username is not None:
            json_data["username"] = username
        if user_title is not None:
            json_data["user_title"] = user_title
        if display_group_id is not None:
            json_data["display_group_id"] = display_group_id
        if display_icon_group_id is not None:
            json_data["display_icon_group_id"] = display_icon_group_id
        if display_banner_id is not None:
            json_data["display_banner_id"] = display_banner_id
        if conv_welcome_message is not None:
            json_data["conv_welcome_message"] = conv_welcome_message
        if user_dob_day is not None:
            json_data["user_dob_day"] = user_dob_day
        if user_dob_month is not None:
            json_data["user_dob_month"] = user_dob_month
        if user_dob_year is not None:
            json_data["user_dob_year"] = user_dob_year
        if secret_answer is not None:
            json_data["secret_answer"] = secret_answer
        if secret_answer_type is not None:
            json_data["secret_answer_type"] = secret_answer_type
        if short_link is not None:
            json_data["short_link"] = short_link
        if language_id is not None:
            json_data["language_id"] = language_id
        if gender is not None:
            json_data["gender"] = gender
        if timezone is not None:
            json_data["timezone"] = timezone
        if receive_admin_email is not None:
            json_data["receive_admin_email"] = receive_admin_email
        if activity_visible is not None:
            json_data["activity_visible"] = activity_visible
        if show_dob_date is not None:
            json_data["show_dob_date"] = show_dob_date
        if show_dob_year is not None:
            json_data["show_dob_year"] = show_dob_year
        if hide_username_change_logs is not None:
            json_data["hide_username_change_logs"] = hide_username_change_logs
        if allow_view_profile is not None:
            json_data["allow_view_profile"] = allow_view_profile
        if allow_post_profile is not None:
            json_data["allow_post_profile"] = allow_post_profile
        if allow_send_personal_conversation is not None:
            json_data["allow_send_personal_conversation"] = allow_send_personal_conversation
        if allow_invite_group is not None:
            json_data["allow_invite_group"] = allow_invite_group
        if allow_receive_news_feed is not None:
            json_data["allow_receive_news_feed"] = allow_receive_news_feed
        if alert is not None:
            json_data["alert"] = alert
        if fields is not None:
            json_data["fields"] = fields
        return self._client._request(
            "PUT",
            f"/users/{user_id}",
            json=json_data,
            **kwargs,
        )

    def claims(
        self,
        user_id: Any,
        *,
        type_: Literal["market", "nomarket"] | None = None,
        claim_state: Literal["active", "solved", "rejected", "settled"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Claims"""
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if claim_state is not None:
            params["claim_state"] = claim_state
        return self._client._request(
            "GET",
            f"/users/{user_id}/claims",
            params=params,
            **kwargs,
        )

    def upload(
        self,
        user_id: Any,
        avatar: bytes,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Upload Avatar"""
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if avatar is not None:
            files["avatar"] = avatar
        return self._client._request(
            "POST",
            f"/users/{user_id}/avatar",
            data=data,
            files=files,
            **kwargs,
        )

    def delete(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Avatar"""
        return self._client._request(
            "DELETE",
            f"/users/{user_id}/avatar",
            **kwargs,
        )

    def crop(
        self,
        user_id: Any,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Crop Avatar"""
        json_data: dict[str, Any] = {}
        if x is not None:
            json_data["x"] = x
        if y is not None:
            json_data["y"] = y
        if crop is not None:
            json_data["crop"] = crop
        return self._client._request(
            "POST",
            f"/users/{user_id}/avatar/crop",
            json=json_data,
            **kwargs,
        )

    def upload_background(
        self,
        user_id: Any,
        background: bytes,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Upload Background"""
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if background is not None:
            files["background"] = background
        return self._client._request(
            "POST",
            f"/users/{user_id}/background",
            data=data,
            files=files,
            **kwargs,
        )

    def delete_background(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Background"""
        return self._client._request(
            "DELETE",
            f"/users/{user_id}/background",
            **kwargs,
        )

    def crop_background(
        self,
        user_id: Any,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Crop Background"""
        json_data: dict[str, Any] = {}
        if x is not None:
            json_data["x"] = x
        if y is not None:
            json_data["y"] = y
        if crop is not None:
            json_data["crop"] = crop
        return self._client._request(
            "POST",
            f"/users/{user_id}/background/crop",
            json=json_data,
            **kwargs,
        )

    def followers(
        self,
        user_id: Any,
        *,
        order: Literal["natural", "follow_date", "follow_date_reverse"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Followers"""
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            f"/users/{user_id}/followers",
            params=params,
            **kwargs,
        )

    def follow(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Follow User"""
        return self._client._request(
            "POST",
            f"/users/{user_id}/followers",
            **kwargs,
        )

    def unfollow(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unfollow User"""
        return self._client._request(
            "DELETE",
            f"/users/{user_id}/followers",
            **kwargs,
        )

    def followings(
        self,
        user_id: Any,
        *,
        order: Literal["natural", "follow_date", "follow_date_reverse"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followed Users By User"""
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            f"/users/{user_id}/followings",
            params=params,
            **kwargs,
        )

    def likes(
        self,
        user_id: Any,
        *,
        node_id: int | None = None,
        like_type: Literal["like", "like2"] | None = None,
        type_: Literal["gotten", "given"] | None = "gotten",
        page: int | None = None,
        content_type: Literal["post", "post_comment", "profile_post", "profile_post_comment"] | None = "post",
        search_user_id: int | None = None,
        stats: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Likes"""
        params: dict[str, Any] = {}
        if node_id is not None:
            params["node_id"] = node_id
        if like_type is not None:
            params["like_type"] = like_type
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if content_type is not None:
            params["content_type"] = content_type
        if search_user_id is not None:
            params["search_user_id"] = search_user_id
        if stats is not None:
            params["stats"] = stats
        return self._client._request(
            "GET",
            f"/users/{user_id}/likes",
            params=params,
            **kwargs,
        )

    def ignored(
        self,
        *,
        total: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Ignored Users"""
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        return self._client._request(
            "GET",
            "/users/ignored",
            params=params,
            **kwargs,
        )

    def ignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Ignore User"""
        return self._client._request(
            "POST",
            f"/users/{user_id}/ignore",
            **kwargs,
        )

    def ignore_edit(
        self,
        user_id: Any,
        *,
        ignore_conversations: bool | None = None,
        ignore_content: bool | None = None,
        restrict_view_profile: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Ignoring Options"""
        params: dict[str, Any] = {}
        if ignore_conversations is not None:
            params["ignore_conversations"] = ignore_conversations
        if ignore_content is not None:
            params["ignore_content"] = ignore_content
        if restrict_view_profile is not None:
            params["restrict_view_profile"] = restrict_view_profile
        return self._client._request(
            "PUT",
            f"/users/{user_id}/ignore",
            params=params,
            **kwargs,
        )

    def unignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unignore User"""
        return self._client._request(
            "DELETE",
            f"/users/{user_id}/ignore",
            **kwargs,
        )

    def contents(
        self,
        user_id: Any,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> RespUserModel:
        """Get Contents"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            f"/users/{user_id}/timeline",
            params=params,
            model=RespUserModel,
            wrapper_key="user",
            **kwargs,
        )

    def trophies(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Trophies"""
        return self._client._request(
            "GET",
            f"/users/{user_id}/trophies",
            **kwargs,
        )

    def secret_answer_types(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Secret Answer Types"""
        return self._client._request(
            "GET",
            "/users/secret-answer/types",
            **kwargs,
        )

    def reset(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Reset Secret Answer"""
        return self._client._request(
            "POST",
            "/account/secret-answer/reset",
            **kwargs,
        )

    def cancel_reset(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Cancel Secret Answer Reset"""
        return self._client._request(
            "DELETE",
            "/account/secret-answer/reset",
            **kwargs,
        )


class AsyncUsers:
    """Asynchronous Users API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[Literal["*", "alerts"]] | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Get Users"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            "/users",
            params=params,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    async def fields(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Fields"""
        return await self._client._request(
            "GET",
            "/users/fields",
            **kwargs,
        )

    async def find(
        self,
        *,
        username: str | None = None,
        custom_fields: dict[str, Any] | None = None,
        fields_include: list[Literal["*", "alerts"]] | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Find Users"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if custom_fields is not None:
            params["custom_fields"] = custom_fields
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            "/users/find",
            params=params,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    async def get(
        self,
        user_id: Any,
        *,
        fields_include: list[Literal["*", "alerts"]] | None = None,
        **kwargs: Any,
    ) -> RespUserModel:
        """Get User"""
        params: dict[str, Any] = {}
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            f"/users/{user_id}",
            params=params,
            model=RespUserModel,
            wrapper_key="user",
            **kwargs,
        )

    async def edit(
        self,
        user_id: Any,
        *,
        username: str | None = None,
        user_title: str | None = None,
        display_group_id: int | None = None,
        display_icon_group_id: int | None = None,
        display_banner_id: int | None = None,
        conv_welcome_message: str | None = None,
        user_dob_day: int | None = None,
        user_dob_month: int | None = None,
        user_dob_year: int | None = None,
        secret_answer: str | None = None,
        secret_answer_type: int | None = None,
        short_link: str | None = None,
        language_id: int | None = None,
        gender: Literal["", "male", "female"] | None = None,
        timezone: str | None = None,
        receive_admin_email: bool | None = None,
        activity_visible: bool | None = None,
        show_dob_date: bool | None = None,
        show_dob_year: bool | None = None,
        hide_username_change_logs: bool | None = None,
        allow_view_profile: Literal["none", "members", "followed"] | None = None,
        allow_post_profile: Literal["none", "members", "followed"] | None = None,
        allow_send_personal_conversation: Literal["none", "members", "followed"] | None = None,
        allow_invite_group: Literal["none", "members", "followed"] | None = None,
        allow_receive_news_feed: Literal["none", "members", "followed"] | None = None,
        alert: dict[str, Any] | None = None,
        fields: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit User"""
        json_data: dict[str, Any] = {}
        if username is not None:
            json_data["username"] = username
        if user_title is not None:
            json_data["user_title"] = user_title
        if display_group_id is not None:
            json_data["display_group_id"] = display_group_id
        if display_icon_group_id is not None:
            json_data["display_icon_group_id"] = display_icon_group_id
        if display_banner_id is not None:
            json_data["display_banner_id"] = display_banner_id
        if conv_welcome_message is not None:
            json_data["conv_welcome_message"] = conv_welcome_message
        if user_dob_day is not None:
            json_data["user_dob_day"] = user_dob_day
        if user_dob_month is not None:
            json_data["user_dob_month"] = user_dob_month
        if user_dob_year is not None:
            json_data["user_dob_year"] = user_dob_year
        if secret_answer is not None:
            json_data["secret_answer"] = secret_answer
        if secret_answer_type is not None:
            json_data["secret_answer_type"] = secret_answer_type
        if short_link is not None:
            json_data["short_link"] = short_link
        if language_id is not None:
            json_data["language_id"] = language_id
        if gender is not None:
            json_data["gender"] = gender
        if timezone is not None:
            json_data["timezone"] = timezone
        if receive_admin_email is not None:
            json_data["receive_admin_email"] = receive_admin_email
        if activity_visible is not None:
            json_data["activity_visible"] = activity_visible
        if show_dob_date is not None:
            json_data["show_dob_date"] = show_dob_date
        if show_dob_year is not None:
            json_data["show_dob_year"] = show_dob_year
        if hide_username_change_logs is not None:
            json_data["hide_username_change_logs"] = hide_username_change_logs
        if allow_view_profile is not None:
            json_data["allow_view_profile"] = allow_view_profile
        if allow_post_profile is not None:
            json_data["allow_post_profile"] = allow_post_profile
        if allow_send_personal_conversation is not None:
            json_data["allow_send_personal_conversation"] = allow_send_personal_conversation
        if allow_invite_group is not None:
            json_data["allow_invite_group"] = allow_invite_group
        if allow_receive_news_feed is not None:
            json_data["allow_receive_news_feed"] = allow_receive_news_feed
        if alert is not None:
            json_data["alert"] = alert
        if fields is not None:
            json_data["fields"] = fields
        return await self._client._request(
            "PUT",
            f"/users/{user_id}",
            json=json_data,
            **kwargs,
        )

    async def claims(
        self,
        user_id: Any,
        *,
        type_: Literal["market", "nomarket"] | None = None,
        claim_state: Literal["active", "solved", "rejected", "settled"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Claims"""
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if claim_state is not None:
            params["claim_state"] = claim_state
        return await self._client._request(
            "GET",
            f"/users/{user_id}/claims",
            params=params,
            **kwargs,
        )

    async def upload(
        self,
        user_id: Any,
        avatar: bytes,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Upload Avatar"""
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if avatar is not None:
            files["avatar"] = avatar
        return await self._client._request(
            "POST",
            f"/users/{user_id}/avatar",
            data=data,
            files=files,
            **kwargs,
        )

    async def delete(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Avatar"""
        return await self._client._request(
            "DELETE",
            f"/users/{user_id}/avatar",
            **kwargs,
        )

    async def crop(
        self,
        user_id: Any,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Crop Avatar"""
        json_data: dict[str, Any] = {}
        if x is not None:
            json_data["x"] = x
        if y is not None:
            json_data["y"] = y
        if crop is not None:
            json_data["crop"] = crop
        return await self._client._request(
            "POST",
            f"/users/{user_id}/avatar/crop",
            json=json_data,
            **kwargs,
        )

    async def upload_background(
        self,
        user_id: Any,
        background: bytes,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Upload Background"""
        data: dict[str, Any] = {}
        if x is not None:
            data["x"] = x
        if y is not None:
            data["y"] = y
        if crop is not None:
            data["crop"] = crop
        files: dict[str, Any] = {}
        if background is not None:
            files["background"] = background
        return await self._client._request(
            "POST",
            f"/users/{user_id}/background",
            data=data,
            files=files,
            **kwargs,
        )

    async def delete_background(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Background"""
        return await self._client._request(
            "DELETE",
            f"/users/{user_id}/background",
            **kwargs,
        )

    async def crop_background(
        self,
        user_id: Any,
        *,
        x: int | None = None,
        y: int | None = None,
        crop: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Crop Background"""
        json_data: dict[str, Any] = {}
        if x is not None:
            json_data["x"] = x
        if y is not None:
            json_data["y"] = y
        if crop is not None:
            json_data["crop"] = crop
        return await self._client._request(
            "POST",
            f"/users/{user_id}/background/crop",
            json=json_data,
            **kwargs,
        )

    async def followers(
        self,
        user_id: Any,
        *,
        order: Literal["natural", "follow_date", "follow_date_reverse"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Followers"""
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            f"/users/{user_id}/followers",
            params=params,
            **kwargs,
        )

    async def follow(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Follow User"""
        return await self._client._request(
            "POST",
            f"/users/{user_id}/followers",
            **kwargs,
        )

    async def unfollow(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unfollow User"""
        return await self._client._request(
            "DELETE",
            f"/users/{user_id}/followers",
            **kwargs,
        )

    async def followings(
        self,
        user_id: Any,
        *,
        order: Literal["natural", "follow_date", "follow_date_reverse"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Followed Users By User"""
        params: dict[str, Any] = {}
        if order is not None:
            params["order"] = order
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            f"/users/{user_id}/followings",
            params=params,
            **kwargs,
        )

    async def likes(
        self,
        user_id: Any,
        *,
        node_id: int | None = None,
        like_type: Literal["like", "like2"] | None = None,
        type_: Literal["gotten", "given"] | None = "gotten",
        page: int | None = None,
        content_type: Literal["post", "post_comment", "profile_post", "profile_post_comment"] | None = "post",
        search_user_id: int | None = None,
        stats: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get User Likes"""
        params: dict[str, Any] = {}
        if node_id is not None:
            params["node_id"] = node_id
        if like_type is not None:
            params["like_type"] = like_type
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if content_type is not None:
            params["content_type"] = content_type
        if search_user_id is not None:
            params["search_user_id"] = search_user_id
        if stats is not None:
            params["stats"] = stats
        return await self._client._request(
            "GET",
            f"/users/{user_id}/likes",
            params=params,
            **kwargs,
        )

    async def ignored(
        self,
        *,
        total: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Ignored Users"""
        params: dict[str, Any] = {}
        if total is not None:
            params["total"] = total
        return await self._client._request(
            "GET",
            "/users/ignored",
            params=params,
            **kwargs,
        )

    async def ignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Ignore User"""
        return await self._client._request(
            "POST",
            f"/users/{user_id}/ignore",
            **kwargs,
        )

    async def ignore_edit(
        self,
        user_id: Any,
        *,
        ignore_conversations: bool | None = None,
        ignore_content: bool | None = None,
        restrict_view_profile: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Ignoring Options"""
        params: dict[str, Any] = {}
        if ignore_conversations is not None:
            params["ignore_conversations"] = ignore_conversations
        if ignore_content is not None:
            params["ignore_content"] = ignore_content
        if restrict_view_profile is not None:
            params["restrict_view_profile"] = restrict_view_profile
        return await self._client._request(
            "PUT",
            f"/users/{user_id}/ignore",
            params=params,
            **kwargs,
        )

    async def unignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unignore User"""
        return await self._client._request(
            "DELETE",
            f"/users/{user_id}/ignore",
            **kwargs,
        )

    async def contents(
        self,
        user_id: Any,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> RespUserModel:
        """Get Contents"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            f"/users/{user_id}/timeline",
            params=params,
            model=RespUserModel,
            wrapper_key="user",
            **kwargs,
        )

    async def trophies(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Trophies"""
        return await self._client._request(
            "GET",
            f"/users/{user_id}/trophies",
            **kwargs,
        )

    async def secret_answer_types(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Secret Answer Types"""
        return await self._client._request(
            "GET",
            "/users/secret-answer/types",
            **kwargs,
        )

    async def reset(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Reset Secret Answer"""
        return await self._client._request(
            "POST",
            "/account/secret-answer/reset",
            **kwargs,
        )

    async def cancel_reset(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Cancel Secret Answer Reset"""
        return await self._client._request(
            "DELETE",
            "/account/secret-answer/reset",
            **kwargs,
        )


# ===========================================================================
# Profile posts
# ===========================================================================


class SyncProfilePosts:
    """Synchronous Profile posts API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        user_id: Any,
        *,
        posts_user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[Literal["*", "latest_comments"]] | None = None,
        **kwargs: Any,
    ) -> list[RespProfilePostModel]:
        """Get Profile Posts"""
        params: dict[str, Any] = {}
        if posts_user_id is not None:
            params["posts_user_id"] = posts_user_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        return self._client._request(
            "GET",
            f"/users/{user_id}/profile-posts",
            params=params,
            model=RespProfilePostModel,
            wrapper_key="profile_posts",
            is_list=True,
            **kwargs,
        )

    def get(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> RespProfilePostModel:
        """Get Profile Post"""
        return self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}",
            model=RespProfilePostModel,
            wrapper_key="profile_post",
            **kwargs,
        )

    def edit(
        self,
        profile_post_id: int,
        *,
        post_body: str | None = None,
        disable_comments: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Profile Post"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if disable_comments is not None:
            json_data["disable_comments"] = disable_comments
        return self._client._request(
            "PUT",
            f"/profile-posts/{profile_post_id}",
            json=json_data,
            **kwargs,
        )

    def delete(
        self,
        profile_post_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Profile Post"""
        params: dict[str, Any] = {}
        if reason is not None:
            params["reason"] = reason
        return self._client._request(
            "DELETE",
            f"/profile-posts/{profile_post_id}",
            params=params,
            **kwargs,
        )

    def report_reasons(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Profile Post Report Reasons"""
        return self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}/report",
            **kwargs,
        )

    def report(
        self,
        profile_post_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report a Profile Post"""
        json_data: dict[str, Any] = {}
        if message is not None:
            json_data["message"] = message
        return self._client._request(
            "POST",
            f"/profile-posts/{profile_post_id}/report",
            json=json_data,
            **kwargs,
        )

    def create(
        self,
        user_id: Any,
        post_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Profile Post"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        if post_body is not None:
            json_data["post_body"] = post_body
        return self._client._request(
            "POST",
            "/profile-posts",
            json=json_data,
            **kwargs,
        )

    def stick(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Stick Profile Post"""
        return self._client._request(
            "POST",
            f"/profile-posts/{profile_post_id}/stick",
            **kwargs,
        )

    def unstick(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unstick Profile Post"""
        return self._client._request(
            "DELETE",
            f"/profile-posts/{profile_post_id}/stick",
            **kwargs,
        )

    def likes(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Profile Post Likes"""
        return self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}/likes",
            **kwargs,
        )

    def like(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Like Profile Post"""
        return self._client._request(
            "POST",
            f"/profile-posts/{profile_post_id}/likes",
            **kwargs,
        )

    def unlike(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unlike Profile Post"""
        return self._client._request(
            "DELETE",
            f"/profile-posts/{profile_post_id}/likes",
            **kwargs,
        )

    def list_comments(
        self,
        profile_post_id: int,
        *,
        before: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespProfilePostCommentModel]:
        """Get Profile Post Comments"""
        params: dict[str, Any] = {}
        if profile_post_id is not None:
            params["profile_post_id"] = profile_post_id
        if before is not None:
            params["before"] = before
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            "/profile-posts/comments",
            params=params,
            model=RespProfilePostCommentModel,
            wrapper_key="comments",
            is_list=True,
            **kwargs,
        )

    def create_comments(
        self,
        profile_post_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if profile_post_id is not None:
            json_data["profile_post_id"] = profile_post_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return self._client._request(
            "POST",
            "/profile-posts/comments",
            json=json_data,
            **kwargs,
        )

    def edit_comments(
        self,
        comment_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if comment_id is not None:
            json_data["comment_id"] = comment_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return self._client._request(
            "PUT",
            "/profile-posts/comments",
            json=json_data,
            **kwargs,
        )

    def delete_comments(
        self,
        comment_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if comment_id is not None:
            json_data["comment_id"] = comment_id
        return self._client._request(
            "DELETE",
            "/profile-posts/comments",
            json=json_data,
            **kwargs,
        )

    def get_comments(
        self,
        profile_post_id: int,
        comment_id: int,
        **kwargs: Any,
    ) -> RespProfilePostCommentModel:
        """Get Profile Post Comment"""
        return self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}/comments/{comment_id}",
            model=RespProfilePostCommentModel,
            wrapper_key="comment",
            **kwargs,
        )

    def report_comments(
        self,
        comment_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report a Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if message is not None:
            json_data["message"] = message
        return self._client._request(
            "POST",
            f"/profile-posts/comments/{comment_id}/report",
            json=json_data,
            **kwargs,
        )


class AsyncProfilePosts:
    """Asynchronous Profile posts API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        user_id: Any,
        *,
        posts_user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        fields_include: list[Literal["*", "latest_comments"]] | None = None,
        **kwargs: Any,
    ) -> list[RespProfilePostModel]:
        """Get Profile Posts"""
        params: dict[str, Any] = {}
        if posts_user_id is not None:
            params["posts_user_id"] = posts_user_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if fields_include is not None:
            params["fields_include"] = fields_include
        return await self._client._request(
            "GET",
            f"/users/{user_id}/profile-posts",
            params=params,
            model=RespProfilePostModel,
            wrapper_key="profile_posts",
            is_list=True,
            **kwargs,
        )

    async def get(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> RespProfilePostModel:
        """Get Profile Post"""
        return await self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}",
            model=RespProfilePostModel,
            wrapper_key="profile_post",
            **kwargs,
        )

    async def edit(
        self,
        profile_post_id: int,
        *,
        post_body: str | None = None,
        disable_comments: bool | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Profile Post"""
        json_data: dict[str, Any] = {}
        if post_body is not None:
            json_data["post_body"] = post_body
        if disable_comments is not None:
            json_data["disable_comments"] = disable_comments
        return await self._client._request(
            "PUT",
            f"/profile-posts/{profile_post_id}",
            json=json_data,
            **kwargs,
        )

    async def delete(
        self,
        profile_post_id: int,
        *,
        reason: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Profile Post"""
        params: dict[str, Any] = {}
        if reason is not None:
            params["reason"] = reason
        return await self._client._request(
            "DELETE",
            f"/profile-posts/{profile_post_id}",
            params=params,
            **kwargs,
        )

    async def report_reasons(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Profile Post Report Reasons"""
        return await self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}/report",
            **kwargs,
        )

    async def report(
        self,
        profile_post_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report a Profile Post"""
        json_data: dict[str, Any] = {}
        if message is not None:
            json_data["message"] = message
        return await self._client._request(
            "POST",
            f"/profile-posts/{profile_post_id}/report",
            json=json_data,
            **kwargs,
        )

    async def create(
        self,
        user_id: Any,
        post_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Profile Post"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        if post_body is not None:
            json_data["post_body"] = post_body
        return await self._client._request(
            "POST",
            "/profile-posts",
            json=json_data,
            **kwargs,
        )

    async def stick(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Stick Profile Post"""
        return await self._client._request(
            "POST",
            f"/profile-posts/{profile_post_id}/stick",
            **kwargs,
        )

    async def unstick(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unstick Profile Post"""
        return await self._client._request(
            "DELETE",
            f"/profile-posts/{profile_post_id}/stick",
            **kwargs,
        )

    async def likes(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Profile Post Likes"""
        return await self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}/likes",
            **kwargs,
        )

    async def like(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Like Profile Post"""
        return await self._client._request(
            "POST",
            f"/profile-posts/{profile_post_id}/likes",
            **kwargs,
        )

    async def unlike(
        self,
        profile_post_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unlike Profile Post"""
        return await self._client._request(
            "DELETE",
            f"/profile-posts/{profile_post_id}/likes",
            **kwargs,
        )

    async def list_comments(
        self,
        profile_post_id: int,
        *,
        before: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespProfilePostCommentModel]:
        """Get Profile Post Comments"""
        params: dict[str, Any] = {}
        if profile_post_id is not None:
            params["profile_post_id"] = profile_post_id
        if before is not None:
            params["before"] = before
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            "/profile-posts/comments",
            params=params,
            model=RespProfilePostCommentModel,
            wrapper_key="comments",
            is_list=True,
            **kwargs,
        )

    async def create_comments(
        self,
        profile_post_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if profile_post_id is not None:
            json_data["profile_post_id"] = profile_post_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return await self._client._request(
            "POST",
            "/profile-posts/comments",
            json=json_data,
            **kwargs,
        )

    async def edit_comments(
        self,
        comment_id: int,
        comment_body: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Edit Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if comment_id is not None:
            json_data["comment_id"] = comment_id
        if comment_body is not None:
            json_data["comment_body"] = comment_body
        return await self._client._request(
            "PUT",
            "/profile-posts/comments",
            json=json_data,
            **kwargs,
        )

    async def delete_comments(
        self,
        comment_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if comment_id is not None:
            json_data["comment_id"] = comment_id
        return await self._client._request(
            "DELETE",
            "/profile-posts/comments",
            json=json_data,
            **kwargs,
        )

    async def get_comments(
        self,
        profile_post_id: int,
        comment_id: int,
        **kwargs: Any,
    ) -> RespProfilePostCommentModel:
        """Get Profile Post Comment"""
        return await self._client._request(
            "GET",
            f"/profile-posts/{profile_post_id}/comments/{comment_id}",
            model=RespProfilePostCommentModel,
            wrapper_key="comment",
            **kwargs,
        )

    async def report_comments(
        self,
        comment_id: int,
        message: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report a Profile Post Comment"""
        json_data: dict[str, Any] = {}
        if message is not None:
            json_data["message"] = message
        return await self._client._request(
            "POST",
            f"/profile-posts/comments/{comment_id}/report",
            json=json_data,
            **kwargs,
        )


# ===========================================================================
# Conversations
# ===========================================================================


class SyncConversations:
    """Synchronous Conversations API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        folder: Literal["all", "unread", "groups", "market", "market_replacements", "staff", "giveaways", "p2p"]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespConversationModel]:
        """Get Conversations"""
        params: dict[str, Any] = {}
        if folder is not None:
            params["folder"] = folder
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            "/conversations",
            params=params,
            model=RespConversationModel,
            wrapper_key="conversations",
            is_list=True,
            **kwargs,
        )

    def create(
        self,
        *,
        recipient_id: int | None = None,
        recipients: list[str] | None = None,
        is_group: bool | None = False,
        title: str | None = None,
        open_invite: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
        message_body: str | None = None,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Create Conversation"""
        json_data: dict[str, Any] = {}
        if recipient_id is not None:
            json_data["recipient_id"] = recipient_id
        if recipients is not None:
            json_data["recipients"] = recipients
        if is_group is not None:
            json_data["is_group"] = is_group
        if title is not None:
            json_data["title"] = title
        if open_invite is not None:
            json_data["open_invite"] = open_invite
        if allow_edit_messages is not None:
            json_data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            json_data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            json_data["allow_delete_own_messages"] = allow_delete_own_messages
        if message_body is not None:
            json_data["message_body"] = message_body
        return self._client._request(
            "POST",
            "/conversations",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    def update(
        self,
        conversation_id: int,
        *,
        title: str | None = None,
        open_invite: bool | None = None,
        history_open: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Edit Conversation"""
        json_data: dict[str, Any] = {}
        if conversation_id is not None:
            json_data["conversation_id"] = conversation_id
        if title is not None:
            json_data["title"] = title
        if open_invite is not None:
            json_data["open_invite"] = open_invite
        if history_open is not None:
            json_data["history_open"] = history_open
        if allow_edit_messages is not None:
            json_data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            json_data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            json_data["allow_delete_own_messages"] = allow_delete_own_messages
        return self._client._request(
            "PUT",
            "/conversations",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    def delete(
        self,
        conversation_id: int,
        delete_type: Literal["delete", "delete_ignore"],
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Leave Conversation"""
        json_data: dict[str, Any] = {}
        if conversation_id is not None:
            json_data["conversation_id"] = conversation_id
        if delete_type is not None:
            json_data["delete_type"] = delete_type
        return self._client._request(
            "DELETE",
            "/conversations",
            json=json_data,
            **kwargs,
        )

    def start(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Start Conversation"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return self._client._request(
            "POST",
            "/conversations/start",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    def save(
        self,
        link: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Send Content To Saved Messages"""
        json_data: dict[str, Any] = {}
        if link is not None:
            json_data["link"] = link
        return self._client._request(
            "POST",
            "/conversations/save",
            json=json_data,
            **kwargs,
        )

    def get(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Get Conversation"""
        return self._client._request(
            "GET",
            f"/conversations/{conversation_id}",
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    def list_messages(
        self,
        conversation_id: int,
        *,
        page: int | None = None,
        limit: int | None = None,
        order: Literal["natural", "natural_reverse"] | None = None,
        before: int | None = None,
        after: int | None = None,
        **kwargs: Any,
    ) -> list[RespConversationMessageModel]:
        """Get Conversation Messages"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        return self._client._request(
            "GET",
            f"/conversations/{conversation_id}/messages",
            params=params,
            model=RespConversationMessageModel,
            wrapper_key="messages",
            is_list=True,
            **kwargs,
        )

    def create_messages(
        self,
        conversation_id: int,
        message_body: str,
        *,
        reply_message_id: int | None = None,
        **kwargs: Any,
    ) -> RespConversationMessageModel:
        """Create Conversation Message"""
        json_data: dict[str, Any] = {}
        if reply_message_id is not None:
            json_data["reply_message_id"] = reply_message_id
        if message_body is not None:
            json_data["message_body"] = message_body
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/messages",
            json=json_data,
            model=RespConversationMessageModel,
            wrapper_key="message",
            **kwargs,
        )

    def search(
        self,
        *,
        q: str | None = None,
        conversation_id: int | None = None,
        search_recipients: bool | None = None,
        **kwargs: Any,
    ) -> list[RespConversationModel]:
        """Search Conversations Messages"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if conversation_id is not None:
            json_data["conversation_id"] = conversation_id
        if search_recipients is not None:
            json_data["search_recipients"] = search_recipients
        return self._client._request(
            "POST",
            "/conversations/search",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversations",
            is_list=True,
            **kwargs,
        )

    def get_messages(
        self,
        message_id: int,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Get Conversation Message"""
        return self._client._request(
            "GET",
            f"/conversations/messages/{message_id}",
            model=RespConversationModel,
            wrapper_key="message",
            **kwargs,
        )

    def edit(
        self,
        conversation_id: int,
        message_id: int,
        message_body: str,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Edit Conversation Message"""
        json_data: dict[str, Any] = {}
        if message_body is not None:
            json_data["message_body"] = message_body
        return self._client._request(
            "PUT",
            f"/conversations/{conversation_id}/messages/{message_id}",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="message",
            **kwargs,
        )

    def delete_messages(
        self,
        conversation_id: int,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Conversation Message"""
        return self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/messages/{message_id}",
            **kwargs,
        )

    def invite(
        self,
        conversation_id: int,
        recipients: list[str],
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Invite Users to Conversation"""
        json_data: dict[str, Any] = {}
        if recipients is not None:
            json_data["recipients"] = recipients
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/invite",
            json=json_data,
            **kwargs,
        )

    def kick(
        self,
        conversation_id: int,
        user_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Kick User from Conversation"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/kick",
            json=json_data,
            **kwargs,
        )

    def read(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Read a Conversation"""
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/read",
            **kwargs,
        )

    def read_all(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Read All Conversations"""
        return self._client._request(
            "POST",
            "/conversations/read-all",
            **kwargs,
        )

    def stick(
        self,
        conversation_id: int,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Stick Conversation Message"""
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/messages/{message_id}/stick",
            **kwargs,
        )

    def unstick(
        self,
        conversation_id: int,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unstick Conversation Message"""
        return self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/messages/{message_id}/stick",
            **kwargs,
        )

    def star(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Star Conversation"""
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/star",
            **kwargs,
        )

    def unstar(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unstar Conversation"""
        return self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/star",
            **kwargs,
        )

    def enable(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Enable Conversation Alerts"""
        return self._client._request(
            "POST",
            f"/conversations/{conversation_id}/alerts",
            **kwargs,
        )

    def disable(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Disable Conversation Alerts"""
        return self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/alerts",
            **kwargs,
        )


class AsyncConversations:
    """Asynchronous Conversations API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        folder: Literal["all", "unread", "groups", "market", "market_replacements", "staff", "giveaways", "p2p"]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespConversationModel]:
        """Get Conversations"""
        params: dict[str, Any] = {}
        if folder is not None:
            params["folder"] = folder
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            "/conversations",
            params=params,
            model=RespConversationModel,
            wrapper_key="conversations",
            is_list=True,
            **kwargs,
        )

    async def create(
        self,
        *,
        recipient_id: int | None = None,
        recipients: list[str] | None = None,
        is_group: bool | None = False,
        title: str | None = None,
        open_invite: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
        message_body: str | None = None,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Create Conversation"""
        json_data: dict[str, Any] = {}
        if recipient_id is not None:
            json_data["recipient_id"] = recipient_id
        if recipients is not None:
            json_data["recipients"] = recipients
        if is_group is not None:
            json_data["is_group"] = is_group
        if title is not None:
            json_data["title"] = title
        if open_invite is not None:
            json_data["open_invite"] = open_invite
        if allow_edit_messages is not None:
            json_data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            json_data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            json_data["allow_delete_own_messages"] = allow_delete_own_messages
        if message_body is not None:
            json_data["message_body"] = message_body
        return await self._client._request(
            "POST",
            "/conversations",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    async def update(
        self,
        conversation_id: int,
        *,
        title: str | None = None,
        open_invite: bool | None = None,
        history_open: bool | None = None,
        allow_edit_messages: bool | None = None,
        allow_sticky_messages: bool | None = None,
        allow_delete_own_messages: bool | None = None,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Edit Conversation"""
        json_data: dict[str, Any] = {}
        if conversation_id is not None:
            json_data["conversation_id"] = conversation_id
        if title is not None:
            json_data["title"] = title
        if open_invite is not None:
            json_data["open_invite"] = open_invite
        if history_open is not None:
            json_data["history_open"] = history_open
        if allow_edit_messages is not None:
            json_data["allow_edit_messages"] = allow_edit_messages
        if allow_sticky_messages is not None:
            json_data["allow_sticky_messages"] = allow_sticky_messages
        if allow_delete_own_messages is not None:
            json_data["allow_delete_own_messages"] = allow_delete_own_messages
        return await self._client._request(
            "PUT",
            "/conversations",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    async def delete(
        self,
        conversation_id: int,
        delete_type: Literal["delete", "delete_ignore"],
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Leave Conversation"""
        json_data: dict[str, Any] = {}
        if conversation_id is not None:
            json_data["conversation_id"] = conversation_id
        if delete_type is not None:
            json_data["delete_type"] = delete_type
        return await self._client._request(
            "DELETE",
            "/conversations",
            json=json_data,
            **kwargs,
        )

    async def start(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Start Conversation"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return await self._client._request(
            "POST",
            "/conversations/start",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    async def save(
        self,
        link: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Send Content To Saved Messages"""
        json_data: dict[str, Any] = {}
        if link is not None:
            json_data["link"] = link
        return await self._client._request(
            "POST",
            "/conversations/save",
            json=json_data,
            **kwargs,
        )

    async def get(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Get Conversation"""
        return await self._client._request(
            "GET",
            f"/conversations/{conversation_id}",
            model=RespConversationModel,
            wrapper_key="conversation",
            **kwargs,
        )

    async def list_messages(
        self,
        conversation_id: int,
        *,
        page: int | None = None,
        limit: int | None = None,
        order: Literal["natural", "natural_reverse"] | None = None,
        before: int | None = None,
        after: int | None = None,
        **kwargs: Any,
    ) -> list[RespConversationMessageModel]:
        """Get Conversation Messages"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if order is not None:
            params["order"] = order
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        return await self._client._request(
            "GET",
            f"/conversations/{conversation_id}/messages",
            params=params,
            model=RespConversationMessageModel,
            wrapper_key="messages",
            is_list=True,
            **kwargs,
        )

    async def create_messages(
        self,
        conversation_id: int,
        message_body: str,
        *,
        reply_message_id: int | None = None,
        **kwargs: Any,
    ) -> RespConversationMessageModel:
        """Create Conversation Message"""
        json_data: dict[str, Any] = {}
        if reply_message_id is not None:
            json_data["reply_message_id"] = reply_message_id
        if message_body is not None:
            json_data["message_body"] = message_body
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/messages",
            json=json_data,
            model=RespConversationMessageModel,
            wrapper_key="message",
            **kwargs,
        )

    async def search(
        self,
        *,
        q: str | None = None,
        conversation_id: int | None = None,
        search_recipients: bool | None = None,
        **kwargs: Any,
    ) -> list[RespConversationModel]:
        """Search Conversations Messages"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if conversation_id is not None:
            json_data["conversation_id"] = conversation_id
        if search_recipients is not None:
            json_data["search_recipients"] = search_recipients
        return await self._client._request(
            "POST",
            "/conversations/search",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="conversations",
            is_list=True,
            **kwargs,
        )

    async def get_messages(
        self,
        message_id: int,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Get Conversation Message"""
        return await self._client._request(
            "GET",
            f"/conversations/messages/{message_id}",
            model=RespConversationModel,
            wrapper_key="message",
            **kwargs,
        )

    async def edit(
        self,
        conversation_id: int,
        message_id: int,
        message_body: str,
        **kwargs: Any,
    ) -> RespConversationModel:
        """Edit Conversation Message"""
        json_data: dict[str, Any] = {}
        if message_body is not None:
            json_data["message_body"] = message_body
        return await self._client._request(
            "PUT",
            f"/conversations/{conversation_id}/messages/{message_id}",
            json=json_data,
            model=RespConversationModel,
            wrapper_key="message",
            **kwargs,
        )

    async def delete_messages(
        self,
        conversation_id: int,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Conversation Message"""
        return await self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/messages/{message_id}",
            **kwargs,
        )

    async def invite(
        self,
        conversation_id: int,
        recipients: list[str],
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Invite Users to Conversation"""
        json_data: dict[str, Any] = {}
        if recipients is not None:
            json_data["recipients"] = recipients
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/invite",
            json=json_data,
            **kwargs,
        )

    async def kick(
        self,
        conversation_id: int,
        user_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Kick User from Conversation"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/kick",
            json=json_data,
            **kwargs,
        )

    async def read(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Read a Conversation"""
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/read",
            **kwargs,
        )

    async def read_all(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Read All Conversations"""
        return await self._client._request(
            "POST",
            "/conversations/read-all",
            **kwargs,
        )

    async def stick(
        self,
        conversation_id: int,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Stick Conversation Message"""
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/messages/{message_id}/stick",
            **kwargs,
        )

    async def unstick(
        self,
        conversation_id: int,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unstick Conversation Message"""
        return await self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/messages/{message_id}/stick",
            **kwargs,
        )

    async def star(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Star Conversation"""
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/star",
            **kwargs,
        )

    async def unstar(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unstar Conversation"""
        return await self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/star",
            **kwargs,
        )

    async def enable(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Enable Conversation Alerts"""
        return await self._client._request(
            "POST",
            f"/conversations/{conversation_id}/alerts",
            **kwargs,
        )

    async def disable(
        self,
        conversation_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Disable Conversation Alerts"""
        return await self._client._request(
            "DELETE",
            f"/conversations/{conversation_id}/alerts",
            **kwargs,
        )


# ===========================================================================
# Notifications
# ===========================================================================


class SyncNotifications:
    """Synchronous Notifications API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        type_: Literal["market", "nomarket"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespNotificationModel]:
        """Get Notifications"""
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            "/notifications",
            params=params,
            model=RespNotificationModel,
            wrapper_key="notifications",
            is_list=True,
            **kwargs,
        )

    def get(
        self,
        notification_id: int,
        **kwargs: Any,
    ) -> RespNotificationModel:
        """Get Notification"""
        return self._client._request(
            "GET",
            f"/notifications/{notification_id}/content",
            model=RespNotificationModel,
            wrapper_key="notification",
            **kwargs,
        )

    def read(
        self,
        *,
        notification_id: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Mark Notification Read"""
        json_data: dict[str, Any] = {}
        if notification_id is not None:
            json_data["notification_id"] = notification_id
        return self._client._request(
            "POST",
            "/notifications/read",
            json=json_data,
            **kwargs,
        )


class AsyncNotifications:
    """Asynchronous Notifications API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        type_: Literal["market", "nomarket"] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespNotificationModel]:
        """Get Notifications"""
        params: dict[str, Any] = {}
        if type_ is not None:
            params["type"] = type_
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            "/notifications",
            params=params,
            model=RespNotificationModel,
            wrapper_key="notifications",
            is_list=True,
            **kwargs,
        )

    async def get(
        self,
        notification_id: int,
        **kwargs: Any,
    ) -> RespNotificationModel:
        """Get Notification"""
        return await self._client._request(
            "GET",
            f"/notifications/{notification_id}/content",
            model=RespNotificationModel,
            wrapper_key="notification",
            **kwargs,
        )

    async def read(
        self,
        *,
        notification_id: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Mark Notification Read"""
        json_data: dict[str, Any] = {}
        if notification_id is not None:
            json_data["notification_id"] = notification_id
        return await self._client._request(
            "POST",
            "/notifications/read",
            json=json_data,
            **kwargs,
        )


# ===========================================================================
# Tags
# ===========================================================================


class SyncTags:
    """Synchronous Tags API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def popular(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Popular Tags"""
        return self._client._request(
            "GET",
            "/tags",
            **kwargs,
        )

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Tags"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            "/tags/list",
            params=params,
            **kwargs,
        )

    def get(
        self,
        tag_id: int,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Tagged Content"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return self._client._request(
            "GET",
            f"/tags/{tag_id}",
            params=params,
            **kwargs,
        )

    def find(
        self,
        tag: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Filtered Content"""
        params: dict[str, Any] = {}
        if tag is not None:
            params["tag"] = tag
        return self._client._request(
            "GET",
            "/tags/find",
            params=params,
            **kwargs,
        )


class AsyncTags:
    """Asynchronous Tags API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def popular(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Popular Tags"""
        return await self._client._request(
            "GET",
            "/tags",
            **kwargs,
        )

    async def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Tags"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            "/tags/list",
            params=params,
            **kwargs,
        )

    async def get(
        self,
        tag_id: int,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Tagged Content"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        return await self._client._request(
            "GET",
            f"/tags/{tag_id}",
            params=params,
            **kwargs,
        )

    async def find(
        self,
        tag: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Filtered Content"""
        params: dict[str, Any] = {}
        if tag is not None:
            params["tag"] = tag
        return await self._client._request(
            "GET",
            "/tags/find",
            params=params,
            **kwargs,
        )


# ===========================================================================
# Search
# ===========================================================================


class SyncSearch:
    """Synchronous Search API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def all(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Search"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if tag is not None:
            json_data["tag"] = tag
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return self._client._request(
            "POST",
            "/search",
            json=json_data,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    def threads(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Thread"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if tag is not None:
            json_data["tag"] = tag
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        if data_limit is not None:
            json_data["data_limit"] = data_limit
        return self._client._request(
            "POST",
            "/search/threads",
            json=json_data,
            **kwargs,
        )

    def posts(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Post"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if tag is not None:
            json_data["tag"] = tag
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        if data_limit is not None:
            json_data["data_limit"] = data_limit
        return self._client._request(
            "POST",
            "/search/posts",
            json=json_data,
            **kwargs,
        )

    def users(
        self,
        *,
        q: str | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Search Users"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        return self._client._request(
            "POST",
            "/search/users",
            json=json_data,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    def profile_posts(
        self,
        *,
        q: str | None = None,
        user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Profile Posts"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return self._client._request(
            "POST",
            "/search/profile-posts",
            json=json_data,
            **kwargs,
        )

    def tagged(
        self,
        *,
        tag: str | None = None,
        tags: list[str] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Tagged"""
        json_data: dict[str, Any] = {}
        if tag is not None:
            json_data["tag"] = tag
        if tags is not None:
            json_data["tags"] = tags
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return self._client._request(
            "POST",
            "/search/tagged",
            json=json_data,
            **kwargs,
        )

    def results(
        self,
        search_id: Any,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Search Results"""
        json_data: dict[str, Any] = {}
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return self._client._request(
            "GET",
            f"/search/{search_id}/results",
            json=json_data,
            **kwargs,
        )


class AsyncSearch:
    """Asynchronous Search API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def all(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Search"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if tag is not None:
            json_data["tag"] = tag
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return await self._client._request(
            "POST",
            "/search",
            json=json_data,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    async def threads(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Thread"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if tag is not None:
            json_data["tag"] = tag
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        if data_limit is not None:
            json_data["data_limit"] = data_limit
        return await self._client._request(
            "POST",
            "/search/threads",
            json=json_data,
            **kwargs,
        )

    async def posts(
        self,
        *,
        q: str | None = None,
        tag: str | None = None,
        forum_id: int | None = None,
        user_id: Any | None = None,
        page: int | None = None,
        limit: int | None = None,
        data_limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Post"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if tag is not None:
            json_data["tag"] = tag
        if forum_id is not None:
            json_data["forum_id"] = forum_id
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        if data_limit is not None:
            json_data["data_limit"] = data_limit
        return await self._client._request(
            "POST",
            "/search/posts",
            json=json_data,
            **kwargs,
        )

    async def users(
        self,
        *,
        q: str | None = None,
        **kwargs: Any,
    ) -> list[RespUserModel]:
        """Search Users"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        return await self._client._request(
            "POST",
            "/search/users",
            json=json_data,
            model=RespUserModel,
            wrapper_key="users",
            is_list=True,
            **kwargs,
        )

    async def profile_posts(
        self,
        *,
        q: str | None = None,
        user_id: int | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Profile Posts"""
        json_data: dict[str, Any] = {}
        if q is not None:
            json_data["q"] = q
        if user_id is not None:
            json_data["user_id"] = user_id
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return await self._client._request(
            "POST",
            "/search/profile-posts",
            json=json_data,
            **kwargs,
        )

    async def tagged(
        self,
        *,
        tag: str | None = None,
        tags: list[str] | None = None,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Search Tagged"""
        json_data: dict[str, Any] = {}
        if tag is not None:
            json_data["tag"] = tag
        if tags is not None:
            json_data["tags"] = tags
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return await self._client._request(
            "POST",
            "/search/tagged",
            json=json_data,
            **kwargs,
        )

    async def results(
        self,
        search_id: Any,
        *,
        page: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Search Results"""
        json_data: dict[str, Any] = {}
        if page is not None:
            json_data["page"] = page
        if limit is not None:
            json_data["limit"] = limit
        return await self._client._request(
            "GET",
            f"/search/{search_id}/results",
            json=json_data,
            **kwargs,
        )


# ===========================================================================
# Batch
# ===========================================================================


class SyncBatch:
    """Synchronous Batch API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def execute(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Batch"""
        return self._client._request(
            "POST",
            "/batch",
            **kwargs,
        )


class AsyncBatch:
    """Asynchronous Batch API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def execute(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Batch"""
        return await self._client._request(
            "POST",
            "/batch",
            **kwargs,
        )


# ===========================================================================
# Chatbox
# ===========================================================================


class SyncChatbox:
    """Synchronous Chatbox API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def index(
        self,
        *,
        room_id: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chats"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        return self._client._request(
            "GET",
            "/chatbox",
            params=params,
            **kwargs,
        )

    def get_messages(
        self,
        room_id: int,
        *,
        before_message_id: int | None = None,
        **kwargs: Any,
    ) -> list[RespChatboxMessageModel]:
        """Get Chat Messages"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        if before_message_id is not None:
            params["before_message_id"] = before_message_id
        return self._client._request(
            "GET",
            "/chatbox/messages",
            params=params,
            model=RespChatboxMessageModel,
            wrapper_key="messages",
            is_list=True,
            **kwargs,
        )

    def post_message(
        self,
        room_id: int,
        message: str,
        *,
        reply_message_id: int | None = None,
        **kwargs: Any,
    ) -> RespChatboxMessageModel:
        """Create Chat Message"""
        json_data: dict[str, Any] = {}
        if room_id is not None:
            json_data["room_id"] = room_id
        if reply_message_id is not None:
            json_data["reply_message_id"] = reply_message_id
        if message is not None:
            json_data["message"] = message
        return self._client._request(
            "POST",
            "/chatbox/messages",
            json=json_data,
            model=RespChatboxMessageModel,
            wrapper_key="message",
            **kwargs,
        )

    def edit_message(
        self,
        message_id: int,
        message: str,
        **kwargs: Any,
    ) -> RespChatboxMessageModel:
        """Edit Chat Message"""
        json_data: dict[str, Any] = {}
        if message_id is not None:
            json_data["message_id"] = message_id
        if message is not None:
            json_data["message"] = message
        return self._client._request(
            "PUT",
            "/chatbox/messages",
            json=json_data,
            model=RespChatboxMessageModel,
            wrapper_key="message",
            **kwargs,
        )

    def delete_message(
        self,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Chat Message"""
        json_data: dict[str, Any] = {}
        if message_id is not None:
            json_data["message_id"] = message_id
        return self._client._request(
            "DELETE",
            "/chatbox/messages",
            json=json_data,
            **kwargs,
        )

    def online(
        self,
        room_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chat Online"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        return self._client._request(
            "GET",
            "/chatbox/messages/online",
            params=params,
            **kwargs,
        )

    def report_reasons(
        self,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chat Message Report Reasons"""
        params: dict[str, Any] = {}
        if message_id is not None:
            params["message_id"] = message_id
        return self._client._request(
            "GET",
            "/chatbox/messages/report",
            params=params,
            **kwargs,
        )

    def report(
        self,
        message_id: int,
        reason: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report Chat Message"""
        json_data: dict[str, Any] = {}
        if message_id is not None:
            json_data["message_id"] = message_id
        if reason is not None:
            json_data["reason"] = reason
        return self._client._request(
            "POST",
            "/chatbox/messages/report",
            json=json_data,
            **kwargs,
        )

    def get_leaderboard(
        self,
        *,
        duration: Literal["day", "week", "month"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chat Leaderboard"""
        params: dict[str, Any] = {}
        if duration is not None:
            params["duration"] = duration
        return self._client._request(
            "GET",
            "/chatbox/messages/leaderboard",
            params=params,
            **kwargs,
        )

    def get_ignore(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Ignored Chat Users"""
        return self._client._request(
            "GET",
            "/chatbox/ignore",
            **kwargs,
        )

    def post_ignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Ignore Chat User"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return self._client._request(
            "POST",
            "/chatbox/ignore",
            json=json_data,
            **kwargs,
        )

    def delete_ignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unignore Chat User"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return self._client._request(
            "DELETE",
            "/chatbox/ignore",
            json=json_data,
            **kwargs,
        )


class AsyncChatbox:
    """Asynchronous Chatbox API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def index(
        self,
        *,
        room_id: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chats"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        return await self._client._request(
            "GET",
            "/chatbox",
            params=params,
            **kwargs,
        )

    async def get_messages(
        self,
        room_id: int,
        *,
        before_message_id: int | None = None,
        **kwargs: Any,
    ) -> list[RespChatboxMessageModel]:
        """Get Chat Messages"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        if before_message_id is not None:
            params["before_message_id"] = before_message_id
        return await self._client._request(
            "GET",
            "/chatbox/messages",
            params=params,
            model=RespChatboxMessageModel,
            wrapper_key="messages",
            is_list=True,
            **kwargs,
        )

    async def post_message(
        self,
        room_id: int,
        message: str,
        *,
        reply_message_id: int | None = None,
        **kwargs: Any,
    ) -> RespChatboxMessageModel:
        """Create Chat Message"""
        json_data: dict[str, Any] = {}
        if room_id is not None:
            json_data["room_id"] = room_id
        if reply_message_id is not None:
            json_data["reply_message_id"] = reply_message_id
        if message is not None:
            json_data["message"] = message
        return await self._client._request(
            "POST",
            "/chatbox/messages",
            json=json_data,
            model=RespChatboxMessageModel,
            wrapper_key="message",
            **kwargs,
        )

    async def edit_message(
        self,
        message_id: int,
        message: str,
        **kwargs: Any,
    ) -> RespChatboxMessageModel:
        """Edit Chat Message"""
        json_data: dict[str, Any] = {}
        if message_id is not None:
            json_data["message_id"] = message_id
        if message is not None:
            json_data["message"] = message
        return await self._client._request(
            "PUT",
            "/chatbox/messages",
            json=json_data,
            model=RespChatboxMessageModel,
            wrapper_key="message",
            **kwargs,
        )

    async def delete_message(
        self,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Delete Chat Message"""
        json_data: dict[str, Any] = {}
        if message_id is not None:
            json_data["message_id"] = message_id
        return await self._client._request(
            "DELETE",
            "/chatbox/messages",
            json=json_data,
            **kwargs,
        )

    async def online(
        self,
        room_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chat Online"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        return await self._client._request(
            "GET",
            "/chatbox/messages/online",
            params=params,
            **kwargs,
        )

    async def report_reasons(
        self,
        message_id: int,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chat Message Report Reasons"""
        params: dict[str, Any] = {}
        if message_id is not None:
            params["message_id"] = message_id
        return await self._client._request(
            "GET",
            "/chatbox/messages/report",
            params=params,
            **kwargs,
        )

    async def report(
        self,
        message_id: int,
        reason: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Report Chat Message"""
        json_data: dict[str, Any] = {}
        if message_id is not None:
            json_data["message_id"] = message_id
        if reason is not None:
            json_data["reason"] = reason
        return await self._client._request(
            "POST",
            "/chatbox/messages/report",
            json=json_data,
            **kwargs,
        )

    async def get_leaderboard(
        self,
        *,
        duration: Literal["day", "week", "month"] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Chat Leaderboard"""
        params: dict[str, Any] = {}
        if duration is not None:
            params["duration"] = duration
        return await self._client._request(
            "GET",
            "/chatbox/messages/leaderboard",
            params=params,
            **kwargs,
        )

    async def get_ignore(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Ignored Chat Users"""
        return await self._client._request(
            "GET",
            "/chatbox/ignore",
            **kwargs,
        )

    async def post_ignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Ignore Chat User"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return await self._client._request(
            "POST",
            "/chatbox/ignore",
            json=json_data,
            **kwargs,
        )

    async def delete_ignore(
        self,
        user_id: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Unignore Chat User"""
        json_data: dict[str, Any] = {}
        if user_id is not None:
            json_data["user_id"] = user_id
        return await self._client._request(
            "DELETE",
            "/chatbox/ignore",
            json=json_data,
            **kwargs,
        )


# ===========================================================================
# Forms
# ===========================================================================


class SyncForms:
    """Synchronous Forms API methods."""

    def __init__(self, client: SyncAPIClient) -> None:
        self._client = client

    def list(
        self,
        *,
        page: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forms List"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        return self._client._request(
            "GET",
            "/forms",
            params=params,
            **kwargs,
        )

    def create(
        self,
        *,
        form_id: int | None = 1,
        fields: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Form"""
        json_data: dict[str, Any] = {}
        if form_id is not None:
            json_data["form_id"] = form_id
        if fields is not None:
            json_data["fields"] = fields
        return self._client._request(
            "POST",
            "/forms/save",
            json=json_data,
            **kwargs,
        )


class AsyncForms:
    """Asynchronous Forms API methods."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self._client = client

    async def list(
        self,
        *,
        page: int | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get Forms List"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        return await self._client._request(
            "GET",
            "/forms",
            params=params,
            **kwargs,
        )

    async def create(
        self,
        *,
        form_id: int | None = 1,
        fields: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create Form"""
        json_data: dict[str, Any] = {}
        if form_id is not None:
            json_data["form_id"] = form_id
        if fields is not None:
            json_data["fields"] = fields
        return await self._client._request(
            "POST",
            "/forms/save",
            json=json_data,
            **kwargs,
        )

"""lolzpy — Typed Python SDK for LOLZ Forum & Market APIs (sync + async).

Usage::

    # Typed, separate clients (recommended):
    from lolzpy import LolzSync, LolzAsync

    with LolzSync(token="YOUR_TOKEN") as lolz:
        user = lolz.forum.users.get(user_id=4565608)

    # Unified client with runtime mode switching:
    from lolzpy import Lolz

    lolz = Lolz(token="YOUR_TOKEN")
    user = lolz.forum.users.get(user_id=4565608)

    lolz.use_async()
    user = await lolz.forum.users.get(user_id=4565608)
"""

from lolzpy._internal.base_client import AsyncAPIClient, SyncAPIClient
from lolzpy._version import __version__
from lolzpy.core.config import RetryConfig
from lolzpy.core.exceptions import (
    AuthError,
    LolzError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from lolzpy.core.types import BrowserType
from lolzpy.forum._client import (
    AsyncAssets,
    AsyncCategories,
    AsyncChatbox,
    AsyncConversations,
    AsyncForms,
    AsyncForums,
    AsyncLinks,
    AsyncNavigation,
    AsyncNotifications,
    AsyncOAuth,
    AsyncPages,
    AsyncPosts,
    AsyncProfilePosts,
    AsyncSearch,
    AsyncTags,
    AsyncThreads,
    AsyncUsers,
    SyncAssets,
    SyncCategories,
    SyncChatbox,
    SyncConversations,
    SyncForms,
    SyncForums,
    SyncLinks,
    SyncNavigation,
    SyncNotifications,
    SyncOAuth,
    SyncPages,
    SyncPosts,
    SyncProfilePosts,
    SyncSearch,
    SyncTags,
    SyncThreads,
    SyncUsers,
)
from lolzpy.forum._client import (
    AsyncBatch as AsyncForumBatch,
)
from lolzpy.forum._client import (
    SyncBatch as SyncForumBatch,
)
from lolzpy.market._client import (
    AsyncAutoPayments,
    AsyncCart,
    AsyncCategory,
    AsyncCustomDiscounts,
    AsyncImap,
    AsyncManaging,
    AsyncPayments,
    AsyncProfile,
    AsyncProxy,
    AsyncPublishing,
    AsyncPurchasing,
    SyncAutoPayments,
    SyncCart,
    SyncCategory,
    SyncCustomDiscounts,
    SyncImap,
    SyncManaging,
    SyncPayments,
    SyncProfile,
    SyncProxy,
    SyncPublishing,
    SyncPurchasing,
)
from lolzpy.market._client import (
    AsyncBatch as AsyncMarketBatch,
)
from lolzpy.market._client import (
    AsyncList as AsyncMarketList,
)
from lolzpy.market._client import (
    SyncBatch as SyncMarketBatch,
)
from lolzpy.market._client import (
    SyncList as SyncMarketList,
)

__all__ = [
    "__version__",
    "BrowserType",
    "Lolz",
    "LolzSync",
    "LolzAsync",
    "RetryConfig",
    "LolzError",
    "AuthError",
    "RateLimitError",
    "NotFoundError",
    "ServerError",
    "ValidationError",
]

# Default base URLs
_FORUM_BASE_URL = "https://prod-api.lolz.live"
_MARKET_BASE_URL = "https://prod-api.lzt.market"


# ---------------------------------------------------------------------------
# Resource group wrappers
# ---------------------------------------------------------------------------


class _SyncForum:
    """Sync Forum API resource group."""

    def __init__(self, client: SyncAPIClient) -> None:
        self.oauth = SyncOAuth(client)
        self.assets = SyncAssets(client)
        self.categories = SyncCategories(client)
        self.forums = SyncForums(client)
        self.links = SyncLinks(client)
        self.pages = SyncPages(client)
        self.navigation = SyncNavigation(client)
        self.threads = SyncThreads(client)
        self.posts = SyncPosts(client)
        self.users = SyncUsers(client)
        self.profile_posts = SyncProfilePosts(client)
        self.conversations = SyncConversations(client)
        self.notifications = SyncNotifications(client)
        self.tags = SyncTags(client)
        self.search = SyncSearch(client)
        self.batch = SyncForumBatch(client)
        self.chatbox = SyncChatbox(client)
        self.forms = SyncForms(client)


class _AsyncForum:
    """Async Forum API resource group."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self.oauth = AsyncOAuth(client)
        self.assets = AsyncAssets(client)
        self.categories = AsyncCategories(client)
        self.forums = AsyncForums(client)
        self.links = AsyncLinks(client)
        self.pages = AsyncPages(client)
        self.navigation = AsyncNavigation(client)
        self.threads = AsyncThreads(client)
        self.posts = AsyncPosts(client)
        self.users = AsyncUsers(client)
        self.profile_posts = AsyncProfilePosts(client)
        self.conversations = AsyncConversations(client)
        self.notifications = AsyncNotifications(client)
        self.tags = AsyncTags(client)
        self.search = AsyncSearch(client)
        self.batch = AsyncForumBatch(client)
        self.chatbox = AsyncChatbox(client)
        self.forms = AsyncForms(client)


class _SyncMarket:
    """Sync Market API resource group."""

    def __init__(self, client: SyncAPIClient) -> None:
        self.category = SyncCategory(client)
        self.list = SyncMarketList(client)
        self.managing = SyncManaging(client)
        self.profile = SyncProfile(client)
        self.cart = SyncCart(client)
        self.purchasing = SyncPurchasing(client)
        self.custom_discounts = SyncCustomDiscounts(client)
        self.publishing = SyncPublishing(client)
        self.payments = SyncPayments(client)
        self.auto_payments = SyncAutoPayments(client)
        self.proxy = SyncProxy(client)
        self.imap = SyncImap(client)
        self.batch = SyncMarketBatch(client)


class _AsyncMarket:
    """Async Market API resource group."""

    def __init__(self, client: AsyncAPIClient) -> None:
        self.category = AsyncCategory(client)
        self.list = AsyncMarketList(client)
        self.managing = AsyncManaging(client)
        self.profile = AsyncProfile(client)
        self.cart = AsyncCart(client)
        self.purchasing = AsyncPurchasing(client)
        self.custom_discounts = AsyncCustomDiscounts(client)
        self.publishing = AsyncPublishing(client)
        self.payments = AsyncPayments(client)
        self.auto_payments = AsyncAutoPayments(client)
        self.proxy = AsyncProxy(client)
        self.imap = AsyncImap(client)
        self.batch = AsyncMarketBatch(client)


# ---------------------------------------------------------------------------
# Common constructor kwargs
# ---------------------------------------------------------------------------


def _common_kwargs(
    *,
    proxy: str | None,
    connect_timeout: float,
    read_timeout: float,
    retry: RetryConfig | None,
    rate_limit: float,
    impersonate: BrowserType,
) -> dict:
    return dict(
        proxy=proxy,
        connect_timeout=connect_timeout,
        read_timeout=read_timeout,
        retry=retry,
        rate_limit=rate_limit,
        impersonate=impersonate,
    )


# ---------------------------------------------------------------------------
# Typed clients
# ---------------------------------------------------------------------------


class LolzSync:
    """Synchronous LOLZ SDK client combining Forum and Market APIs.

    Usage::

        with LolzSync(token="your_token") as lolz:
            threads = lolz.forum.threads.list()
            items = lolz.market.category.all()
    """

    def __init__(
        self,
        token: str,
        *,
        forum_base_url: str = _FORUM_BASE_URL,
        market_base_url: str = _MARKET_BASE_URL,
        proxy: str | None = None,
        connect_timeout: float = 10.0,
        read_timeout: float = 30.0,
        retry: RetryConfig | None = None,
        rate_limit: float = 0.0,
        impersonate: BrowserType = "chrome",
    ) -> None:
        common = _common_kwargs(
            proxy=proxy,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            retry=retry,
            rate_limit=rate_limit,
            impersonate=impersonate,
        )
        self._forum_client = SyncAPIClient(forum_base_url, token, **common)
        self._market_client = SyncAPIClient(market_base_url, token, **common)
        self.forum = _SyncForum(self._forum_client)
        self.market = _SyncMarket(self._market_client)

    def __enter__(self) -> "LolzSync":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def close(self) -> None:
        self._forum_client.close()
        self._market_client.close()


class LolzAsync:
    """Asynchronous LOLZ SDK client combining Forum and Market APIs.

    Usage::

        async with LolzAsync(token="your_token") as lolz:
            threads = await lolz.forum.threads.list()
            items = await lolz.market.category.all()
    """

    def __init__(
        self,
        token: str,
        *,
        forum_base_url: str = _FORUM_BASE_URL,
        market_base_url: str = _MARKET_BASE_URL,
        proxy: str | None = None,
        connect_timeout: float = 10.0,
        read_timeout: float = 30.0,
        retry: RetryConfig | None = None,
        rate_limit: float = 0.0,
        impersonate: BrowserType = "chrome",
    ) -> None:
        common = _common_kwargs(
            proxy=proxy,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            retry=retry,
            rate_limit=rate_limit,
            impersonate=impersonate,
        )
        self._forum_client = AsyncAPIClient(forum_base_url, token, **common)
        self._market_client = AsyncAPIClient(market_base_url, token, **common)
        self.forum = _AsyncForum(self._forum_client)
        self.market = _AsyncMarket(self._market_client)

    async def __aenter__(self) -> "LolzAsync":
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()

    async def close(self) -> None:
        await self._forum_client.close()
        await self._market_client.close()


# ---------------------------------------------------------------------------
# Unified client with runtime mode switching
# ---------------------------------------------------------------------------


class Lolz:
    """Unified LOLZ SDK client with runtime sync/async mode switching.

    Starts in sync mode by default. Use :meth:`use_async` / :meth:`use_sync`
    to switch at runtime.

    Usage::

        # Sync (default)
        lolz = Lolz(token="YOUR_TOKEN")
        user = lolz.forum.users.get(user_id=4565608)
        lolz.close()

        # Async
        lolz = Lolz(token="YOUR_TOKEN", async_mode=True)
        user = await lolz.forum.users.get(user_id=4565608)
        await lolz.close_async()

        # Switch at runtime
        lolz = Lolz(token="YOUR_TOKEN")
        lolz.use_async()
        user = await lolz.forum.users.get(user_id=4565608)
    """

    def __init__(
        self,
        token: str,
        *,
        forum_base_url: str = _FORUM_BASE_URL,
        market_base_url: str = _MARKET_BASE_URL,
        proxy: str | None = None,
        connect_timeout: float = 10.0,
        read_timeout: float = 30.0,
        retry: RetryConfig | None = None,
        rate_limit: float = 0.0,
        impersonate: BrowserType = "chrome",
        async_mode: bool = False,
    ) -> None:
        self._token = token
        self._forum_base_url = forum_base_url
        self._market_base_url = market_base_url
        self._common = _common_kwargs(
            proxy=proxy,
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            retry=retry,
            rate_limit=rate_limit,
            impersonate=impersonate,
        )
        self._async_mode = async_mode

        if async_mode:
            self._init_async()
        else:
            self._init_sync()

    # -- Mode switching -------------------------------------------------

    def use_async(self) -> "Lolz":
        """Switch to async mode. Closes any existing sync clients. Returns self for chaining."""
        if not self._async_mode:
            self.close()
            self._init_async()
            self._async_mode = True
        return self

    def use_sync(self) -> "Lolz":
        """Switch to sync mode. Closes any existing async clients. Returns self for chaining."""
        if self._async_mode:
            self._close_async_clients()
            self._init_sync()
            self._async_mode = False
        return self

    @property
    def is_async(self) -> bool:
        """Whether the client is currently in async mode."""
        return self._async_mode

    # -- Lifecycle ------------------------------------------------------

    def close(self) -> None:
        """Close sync clients. No-op if in async mode."""
        if not self._async_mode:
            self._forum_client.close()  # type: ignore[union-attr]
            self._market_client.close()  # type: ignore[union-attr]

    async def close_async(self) -> None:
        """Close async clients. No-op if in sync mode."""
        if self._async_mode:
            await self._forum_client.close()  # type: ignore[misc]
            await self._market_client.close()  # type: ignore[misc]

    def _close_async_clients(self) -> None:
        """Close async clients synchronously (for use_sync switch)."""
        import asyncio

        async def _close() -> None:
            await self._forum_client.close()  # type: ignore[misc]
            await self._market_client.close()  # type: ignore[misc]

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            future = asyncio.run_coroutine_threadsafe(_close(), loop)
            future.result(timeout=10)
        else:
            asyncio.run(_close())

    def __enter__(self) -> "Lolz":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    async def __aenter__(self) -> "Lolz":
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close_async()

    # -- Internals ------------------------------------------------------

    def _init_sync(self) -> None:
        self._forum_client: SyncAPIClient | AsyncAPIClient = SyncAPIClient(
            self._forum_base_url, self._token, **self._common
        )
        self._market_client: SyncAPIClient | AsyncAPIClient = SyncAPIClient(
            self._market_base_url, self._token, **self._common
        )
        self.forum: _SyncForum | _AsyncForum = _SyncForum(self._forum_client)  # type: ignore[arg-type]
        self.market: _SyncMarket | _AsyncMarket = _SyncMarket(self._market_client)  # type: ignore[arg-type]

    def _init_async(self) -> None:
        self._forum_client = AsyncAPIClient(self._forum_base_url, self._token, **self._common)
        self._market_client = AsyncAPIClient(self._market_base_url, self._token, **self._common)
        self.forum = _AsyncForum(self._forum_client)  # type: ignore[arg-type]
        self.market = _AsyncMarket(self._market_client)  # type: ignore[arg-type]

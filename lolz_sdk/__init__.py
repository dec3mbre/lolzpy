"""lolz-sdk — Typed Python SDK for LOLZ Forum & Market APIs (sync + async)."""

from lolz_sdk._base import AsyncAPIClient, SyncAPIClient
from lolz_sdk._exceptions import (
    AuthError,
    LolzError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from lolz_sdk._transport import RetryConfig
from lolz_sdk.forum._client import (
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
from lolz_sdk.forum._client import (
    AsyncBatch as AsyncForumBatch,
)
from lolz_sdk.forum._client import (
    SyncBatch as SyncForumBatch,
)
from lolz_sdk.market._client import (
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
from lolz_sdk.market._client import (
    AsyncDefault as AsyncMarketBatch,
)
from lolz_sdk.market._client import (
    AsyncList as AsyncMarketList,
)
from lolz_sdk.market._client import (
    SyncDefault as SyncMarketBatch,
)
from lolz_sdk.market._client import (
    SyncList as SyncMarketList,
)

__all__ = [
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
        timeout: float = 30.0,
        retry: RetryConfig | None = None,
        rate_limit: float = 0.0,
        impersonate: str = "chrome",
    ) -> None:
        common = dict(proxy=proxy, timeout=timeout, retry=retry, rate_limit=rate_limit, impersonate=impersonate)
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
        timeout: float = 30.0,
        retry: RetryConfig | None = None,
        rate_limit: float = 0.0,
        impersonate: str = "chrome",
    ) -> None:
        common = dict(proxy=proxy, timeout=timeout, retry=retry, rate_limit=rate_limit, impersonate=impersonate)
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

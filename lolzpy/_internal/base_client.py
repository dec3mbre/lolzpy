"""Base client classes for sync and async HTTP communication."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from curl_cffi.requests import AsyncSession, Response, Session

from lolzpy._internal.rate_limit import TokenBucketAsync, TokenBucketSync
from lolzpy._internal.retry import request_with_retry_async, request_with_retry_sync
from lolzpy.core.config import RetryConfig
from lolzpy.core.exceptions import ValidationError, raise_for_status
from lolzpy.core.types import T

if TYPE_CHECKING:
    from curl_cffi.requests.impersonate import BrowserTypeLiteral


class BaseClient:
    """Shared configuration for sync and async clients."""

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        proxy: str | None = None,
        timeout: float = 30.0,
        retry: RetryConfig | None = None,
        rate_limit: float = 0.0,
        impersonate: str = "chrome",
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._token = token
        self._proxy = proxy
        self._timeout = timeout
        self._retry = retry or RetryConfig()
        self._rate_limit = rate_limit
        self._impersonate = impersonate

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}

    def _url(self, path: str) -> str:
        return f"{self._base_url}/{path.lstrip('/')}"

    @staticmethod
    def _parse_response(response: Response, model: type[T] | None = None) -> Any:
        """Parse an HTTP response, optionally validating against a Pydantic model."""
        raise_for_status(
            response.status_code,
            response_data=_try_json(response),
            headers=dict(response.headers),
        )
        data = response.json()
        if model is None:
            return data
        try:
            return model.model_validate(data)
        except Exception as exc:
            raise ValidationError(
                f"Failed to validate response as {model.__name__}: {exc}",
                status_code=response.status_code,
                response_data=data,
            ) from exc


class SyncAPIClient(BaseClient):
    """Synchronous HTTP client backed by ``curl_cffi.requests.Session``."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._session = Session(
            impersonate=cast("BrowserTypeLiteral", self._impersonate),
            proxy=self._proxy,
            timeout=self._timeout,
            headers=self._headers(),
        )
        self._limiter: TokenBucketSync | None = TokenBucketSync(self._rate_limit) if self._rate_limit > 0 else None

    # Context manager ---------------------------------------------------

    def __enter__(self) -> SyncAPIClient:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def close(self) -> None:
        self._session.close()

    # Request -----------------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        model: type[T] | None = None,
        **kwargs: Any,
    ) -> Any:
        if self._limiter is not None:
            self._limiter.acquire()

        url = self._url(path)
        cleaned_params = _clean_params(params)

        response = request_with_retry_sync(
            self._session,
            method,
            url,
            self._retry,
            params=cleaned_params,
            json=json,
            data=data,
            **kwargs,
        )
        return self._parse_response(response, model)


class AsyncAPIClient(BaseClient):
    """Asynchronous HTTP client backed by ``curl_cffi.requests.AsyncSession``."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._session = AsyncSession(
            impersonate=cast("BrowserTypeLiteral", self._impersonate),
            proxy=self._proxy,
            timeout=self._timeout,
            headers=self._headers(),
        )
        self._limiter: TokenBucketAsync | None = (
            TokenBucketAsync(self._rate_limit) if self._rate_limit > 0 else None
        )

    # Context manager ---------------------------------------------------

    async def __aenter__(self) -> AsyncAPIClient:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    async def close(self) -> None:
        await self._session.close()

    # Request -----------------------------------------------------------

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        model: type[T] | None = None,
        **kwargs: Any,
    ) -> Any:
        if self._limiter is not None:
            await self._limiter.acquire()

        url = self._url(path)
        cleaned_params = _clean_params(params)

        response = await request_with_retry_async(
            self._session,
            method,
            url,
            self._retry,
            params=cleaned_params,
            json=json,
            data=data,
            **kwargs,
        )
        return self._parse_response(response, model)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _try_json(response: Response) -> Any:
    try:
        return response.json()
    except Exception:
        return None


def _clean_params(params: dict[str, Any] | None) -> dict[str, Any] | None:
    """Remove None values from query parameters."""
    if params is None:
        return None
    return {k: v for k, v in params.items() if v is not None}

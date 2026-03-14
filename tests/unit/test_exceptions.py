"""Tests for lolzpy.core.exceptions."""

from __future__ import annotations

import pytest

from lolzpy.core.exceptions import (
    AuthError,
    LolzError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    raise_for_status,
)

# ---------------------------------------------------------------------------
# Exception hierarchy
# ---------------------------------------------------------------------------


class TestExceptionHierarchy:
    def test_all_subclass_lolz_error(self):
        for cls in (AuthError, NotFoundError, RateLimitError, ServerError, ValidationError):
            assert issubclass(cls, LolzError)

    def test_lolz_error_attrs(self):
        exc = LolzError("boom", status_code=418, response_data={"tea": True})
        assert str(exc) == "boom"
        assert exc.message == "boom"
        assert exc.status_code == 418
        assert exc.response_data == {"tea": True}

    def test_lolz_error_request_context(self):
        exc = LolzError(
            "fail", status_code=500,
            request_url="https://api.test/v1/users", request_method="GET",
        )
        assert exc.request_url == "https://api.test/v1/users"
        assert exc.request_method == "GET"

    def test_lolz_error_request_context_defaults_none(self):
        exc = LolzError("fail")
        assert exc.request_url is None
        assert exc.request_method is None

    def test_rate_limit_error_retry_after(self):
        exc = RateLimitError("slow down", retry_after=3.5)
        assert exc.retry_after == 3.5
        assert exc.status_code == 429

    def test_rate_limit_error_no_retry_after(self):
        exc = RateLimitError("slow down", retry_after=None)
        assert exc.retry_after is None

    def test_rate_limit_error_with_request_context(self):
        exc = RateLimitError(
            "slow", retry_after=1.0,
            request_url="https://api.test/v1", request_method="POST",
        )
        assert exc.request_url == "https://api.test/v1"
        assert exc.request_method == "POST"
        assert exc.retry_after == 1.0


# ---------------------------------------------------------------------------
# raise_for_status
# ---------------------------------------------------------------------------


class TestRaiseForStatus:
    @pytest.mark.parametrize("code", [200, 201, 204, 301, 302, 399])
    def test_success_codes_do_not_raise(self, code: int):
        raise_for_status(code, {}, {})

    def test_401_raises_auth_error(self):
        with pytest.raises(AuthError) as exc_info:
            raise_for_status(401, {"error": "bad token"}, {})
        assert exc_info.value.status_code == 401
        assert exc_info.value.message == "bad token"

    def test_403_raises_auth_error(self):
        with pytest.raises(AuthError) as exc_info:
            raise_for_status(403, {}, {})
        assert exc_info.value.status_code == 403

    def test_404_raises_not_found(self):
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(404, {"message": "gone"}, {})
        assert exc_info.value.message == "gone"

    def test_429_raises_rate_limit_with_retry_after(self):
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(429, {}, {"Retry-After": "10"})
        assert exc_info.value.retry_after == 10.0

    def test_429_raises_rate_limit_lowercase_header(self):
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(429, {}, {"retry-after": "5"})
        assert exc_info.value.retry_after == 5.0

    def test_429_invalid_retry_after_is_none(self):
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(429, {}, {"Retry-After": "not-a-number"})
        assert exc_info.value.retry_after is None

    def test_429_no_headers(self):
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(429, {}, None)
        assert exc_info.value.retry_after is None

    @pytest.mark.parametrize("code", [500, 502, 503, 504])
    def test_5xx_raises_server_error(self, code: int):
        with pytest.raises(ServerError) as exc_info:
            raise_for_status(code, {}, {})
        assert exc_info.value.status_code == code

    def test_unknown_error_code(self):
        with pytest.raises(LolzError) as exc_info:
            raise_for_status(418, {}, {})
        assert exc_info.value.status_code == 418
        assert type(exc_info.value) is LolzError

    def test_error_message_from_response_data(self):
        with pytest.raises(LolzError) as exc_info:
            raise_for_status(400, {"error": "bad request"}, {})
        assert exc_info.value.message == "bad request"

    def test_error_message_fallback(self):
        with pytest.raises(LolzError) as exc_info:
            raise_for_status(400, "not a dict", {})
        assert "HTTP 400" in exc_info.value.message

    def test_request_context_propagated_to_auth_error(self):
        with pytest.raises(AuthError) as exc_info:
            raise_for_status(
                401, {"error": "bad"}, {},
                request_url="https://api.test/v1", request_method="GET",
            )
        assert exc_info.value.request_url == "https://api.test/v1"
        assert exc_info.value.request_method == "GET"

    def test_request_context_propagated_to_rate_limit(self):
        with pytest.raises(RateLimitError) as exc_info:
            raise_for_status(
                429, {}, {"Retry-After": "5"},
                request_url="https://api.test/buy", request_method="POST",
            )
        assert exc_info.value.request_url == "https://api.test/buy"
        assert exc_info.value.request_method == "POST"
        assert exc_info.value.retry_after == 5.0

    def test_request_context_propagated_to_server_error(self):
        with pytest.raises(ServerError) as exc_info:
            raise_for_status(
                502, {}, {},
                request_url="https://api.test/data", request_method="DELETE",
            )
        assert exc_info.value.request_url == "https://api.test/data"
        assert exc_info.value.request_method == "DELETE"

    def test_request_context_propagated_to_not_found(self):
        with pytest.raises(NotFoundError) as exc_info:
            raise_for_status(
                404, {}, {},
                request_url="https://api.test/missing", request_method="GET",
            )
        assert exc_info.value.request_url == "https://api.test/missing"

    def test_request_context_defaults_none(self):
        with pytest.raises(LolzError) as exc_info:
            raise_for_status(418, {}, {})
        assert exc_info.value.request_url is None
        assert exc_info.value.request_method is None

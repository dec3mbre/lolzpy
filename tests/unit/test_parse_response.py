"""Tests for BaseClient._parse_response — core response handling."""

from __future__ import annotations

import pytest
from pydantic import BaseModel, Field

from lolzpy._internal.base_client import BaseClient
from lolzpy.core.exceptions import (
    AuthError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from tests.conftest import make_response


class UserModel(BaseModel):
    user_id: int
    username: str


class ItemModel(BaseModel):
    item_id: int
    title: str


class StrictModel(BaseModel):
    value: int = Field(strict=True)


# ---------------------------------------------------------------------------
# Success cases
# ---------------------------------------------------------------------------


class TestParseResponseSuccess:
    def test_json_response_returns_dict(self):
        resp = make_response(200, json_data={"users": [1, 2, 3]})
        result = BaseClient._parse_response(resp)
        assert result == {"users": [1, 2, 3]}

    def test_json_response_with_model_returns_model(self):
        resp = make_response(200, json_data={"user_id": 1, "username": "alice"})
        result = BaseClient._parse_response(resp, model=UserModel)
        assert isinstance(result, UserModel)
        assert result.user_id == 1
        assert result.username == "alice"

    def test_non_json_response_returns_none(self):
        resp = make_response(200, body=b"OK")
        result = BaseClient._parse_response(resp)
        assert result is None

    def test_empty_body_returns_none(self):
        resp = make_response(200)
        result = BaseClient._parse_response(resp)
        assert result is None

    def test_non_json_with_model_returns_none(self):
        resp = make_response(200, body=b"<html>OK</html>")
        result = BaseClient._parse_response(resp, model=UserModel)
        assert result is None


# ---------------------------------------------------------------------------
# Error status codes
# ---------------------------------------------------------------------------


class TestParseResponseErrors:
    def test_401_raises_auth_error(self):
        resp = make_response(401, json_data={"error": "unauthorized"})
        with pytest.raises(AuthError) as exc_info:
            BaseClient._parse_response(resp)
        assert exc_info.value.status_code == 401

    def test_403_raises_auth_error(self):
        resp = make_response(403, json_data={"error": "forbidden"})
        with pytest.raises(AuthError):
            BaseClient._parse_response(resp)

    def test_404_raises_not_found(self):
        resp = make_response(404, json_data={"error": "not found"})
        with pytest.raises(NotFoundError):
            BaseClient._parse_response(resp)

    def test_429_raises_rate_limit_with_retry_after(self):
        resp = make_response(429, json_data={"error": "slow down"}, headers={"Retry-After": "10"})
        with pytest.raises(RateLimitError) as exc_info:
            BaseClient._parse_response(resp)
        assert exc_info.value.retry_after == 10.0

    def test_500_raises_server_error(self):
        resp = make_response(500, json_data={"error": "internal"})
        with pytest.raises(ServerError):
            BaseClient._parse_response(resp)

    def test_502_html_body_raises_server_error(self):
        resp = make_response(502, body=b"<html>Bad Gateway</html>")
        with pytest.raises(ServerError):
            BaseClient._parse_response(resp)


# ---------------------------------------------------------------------------
# Validation errors
# ---------------------------------------------------------------------------


class TestParseResponseValidation:
    def test_model_validation_failure_raises(self):
        resp = make_response(200, json_data={"wrong_field": "data"})
        with pytest.raises(ValidationError) as exc_info:
            BaseClient._parse_response(resp, model=UserModel)
        assert "UserModel" in exc_info.value.message

    def test_strict_model_type_mismatch_raises(self):
        resp = make_response(200, json_data={"value": "not_an_int"})
        with pytest.raises(ValidationError):
            BaseClient._parse_response(resp, model=StrictModel)


# ---------------------------------------------------------------------------
# Wrapper key and list unwrapping
# ---------------------------------------------------------------------------


class TestParseResponseWrapperKey:
    def test_singular_wrapper_unwraps(self):
        resp = make_response(200, json_data={"user": {"user_id": 1, "username": "alice"}, "system_info": {}})
        result = BaseClient._parse_response(resp, model=UserModel, wrapper_key="user")
        assert isinstance(result, UserModel)
        assert result.username == "alice"
        assert result.user_id == 1

    def test_list_wrapper_unwraps(self):
        resp = make_response(
            200,
            json_data={
                "items": [
                    {"item_id": 1, "title": "Item A"},
                    {"item_id": 2, "title": "Item B"},
                ],
                "system_info": {},
            },
        )
        result = BaseClient._parse_response(resp, model=ItemModel, wrapper_key="items", is_list=True)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(item, ItemModel) for item in result)
        assert result[0].title == "Item A"
        assert result[1].item_id == 2

    def test_empty_list_returns_empty(self):
        resp = make_response(200, json_data={"items": [], "system_info": {}})
        result = BaseClient._parse_response(resp, model=ItemModel, wrapper_key="items", is_list=True)
        assert result == []

    def test_missing_wrapper_key_raises_validation_error(self):
        resp = make_response(200, json_data={"other": {"user_id": 1, "username": "alice"}})
        with pytest.raises(ValidationError):
            BaseClient._parse_response(resp, model=UserModel, wrapper_key="user")

    def test_no_wrapper_key_validates_entire_dict(self):
        resp = make_response(200, json_data={"user_id": 5, "username": "bob"})
        result = BaseClient._parse_response(resp, model=UserModel)
        assert isinstance(result, UserModel)
        assert result.username == "bob"

    def test_none_data_with_wrapper_key_returns_none(self):
        resp = make_response(200, body=b"")
        result = BaseClient._parse_response(resp, model=UserModel, wrapper_key="user")
        assert result is None

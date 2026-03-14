"""Tests for request_with_retry_sync/async — retry logic with mocked sessions."""

from __future__ import annotations

from unittest.mock import patch

import pytest
from curl_cffi.requests.exceptions import RequestException, SessionClosed

from lolzpy._internal.retry import request_with_retry_async, request_with_retry_sync
from lolzpy.core.config import RetryConfig
from tests.conftest import make_async_session, make_response, make_session

# ---------------------------------------------------------------------------
# Sync retry
# ---------------------------------------------------------------------------


class TestRequestWithRetrySync:
    @patch("lolzpy._internal.retry.time.sleep")
    def test_success_on_first_attempt(self, mock_sleep):
        resp = make_response(200, json_data={"ok": True})
        session = make_session([resp])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200
        mock_sleep.assert_not_called()

    @patch("lolzpy._internal.retry.time.sleep")
    def test_retry_on_429_then_success(self, mock_sleep):
        resp_429 = make_response(429, json_data={"error": "rate limited"}, headers={"Retry-After": "1"})
        resp_200 = make_response(200, json_data={"ok": True})
        session = make_session([resp_429, resp_200])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200
        assert session.request.call_count == 2
        mock_sleep.assert_called_once()

    @patch("lolzpy._internal.retry.time.sleep")
    def test_retry_on_500_with_backoff(self, mock_sleep):
        resp_500 = make_response(500, json_data={"error": "server error"})
        resp_200 = make_response(200, json_data={"ok": True})
        session = make_session([resp_500, resp_500, resp_200])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200
        assert session.request.call_count == 3
        assert mock_sleep.call_count == 2

    @patch("lolzpy._internal.retry.time.sleep")
    def test_exhausted_retries_returns_last_response(self, mock_sleep):
        resp_500 = make_response(500, json_data={"error": "server error"})
        session = make_session([resp_500, resp_500, resp_500, resp_500])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 500
        assert session.request.call_count == 4

    @patch("lolzpy._internal.retry.time.sleep")
    def test_non_retryable_status_returns_immediately(self, mock_sleep):
        resp_400 = make_response(400, json_data={"error": "bad request"})
        session = make_session([resp_400])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 400
        assert session.request.call_count == 1
        mock_sleep.assert_not_called()

    @patch("lolzpy._internal.retry.time.sleep")
    def test_connection_error_retry_then_raise(self, mock_sleep):
        session = make_session([ConnectionError("refused"), ConnectionError("refused")])
        config = RetryConfig(max_retries=1)

        with pytest.raises(ConnectionError):
            request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert session.request.call_count == 2

    @patch("lolzpy._internal.retry.time.sleep")
    def test_connection_error_retry_then_success(self, mock_sleep):
        resp_200 = make_response(200, json_data={"ok": True})
        session = make_session([ConnectionError("refused"), resp_200])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200

    def test_session_closed_no_retry(self):
        session = make_session([SessionClosed("closed")])
        config = RetryConfig(max_retries=3)

        with pytest.raises(SessionClosed):
            request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert session.request.call_count == 1

    @patch("lolzpy._internal.retry.time.sleep")
    def test_request_exception_retry(self, mock_sleep):
        resp_200 = make_response(200, json_data={"ok": True})
        session = make_session([RequestException("timeout"), resp_200])
        config = RetryConfig(max_retries=3)

        result = request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200

    @patch("lolzpy._internal.retry.time.sleep")
    def test_retry_after_header_respected(self, mock_sleep):
        resp_429 = make_response(429, json_data={}, headers={"Retry-After": "7"})
        resp_200 = make_response(200, json_data={"ok": True})
        session = make_session([resp_429, resp_200])
        config = RetryConfig(max_retries=3, max_retry_after=60.0)

        request_with_retry_sync(session, "GET", "https://api.test/v1", config)
        # Delay should be 7.0 (from Retry-After header)
        mock_sleep.assert_called_once_with(7.0)


# ---------------------------------------------------------------------------
# Async retry
# ---------------------------------------------------------------------------


class TestRequestWithRetryAsync:
    @pytest.mark.asyncio
    @patch("lolzpy._internal.retry.asyncio.sleep")
    async def test_success_on_first_attempt(self, mock_sleep):
        resp = make_response(200, json_data={"ok": True})
        session = make_async_session([resp])
        config = RetryConfig(max_retries=3)

        result = await request_with_retry_async(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200
        mock_sleep.assert_not_called()

    @pytest.mark.asyncio
    @patch("lolzpy._internal.retry.asyncio.sleep")
    async def test_retry_on_429_then_success(self, mock_sleep):
        resp_429 = make_response(429, json_data={"error": "rate limited"}, headers={"Retry-After": "1"})
        resp_200 = make_response(200, json_data={"ok": True})
        session = make_async_session([resp_429, resp_200])
        config = RetryConfig(max_retries=3)

        result = await request_with_retry_async(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 200
        assert session.request.call_count == 2

    @pytest.mark.asyncio
    @patch("lolzpy._internal.retry.asyncio.sleep")
    async def test_exhausted_retries_returns_last_response(self, mock_sleep):
        resp_500 = make_response(500, json_data={"error": "server error"})
        session = make_async_session([resp_500, resp_500, resp_500, resp_500])
        config = RetryConfig(max_retries=3)

        result = await request_with_retry_async(session, "GET", "https://api.test/v1", config)
        assert result.status_code == 500

    @pytest.mark.asyncio
    @patch("lolzpy._internal.retry.asyncio.sleep")
    async def test_connection_error_retry_then_raise(self, mock_sleep):
        session = make_async_session([ConnectionError("refused"), ConnectionError("refused")])
        config = RetryConfig(max_retries=1)

        with pytest.raises(ConnectionError):
            await request_with_retry_async(session, "GET", "https://api.test/v1", config)

    @pytest.mark.asyncio
    async def test_session_closed_no_retry(self):
        session = make_async_session([SessionClosed("closed")])
        config = RetryConfig(max_retries=3)

        with pytest.raises(SessionClosed):
            await request_with_retry_async(session, "GET", "https://api.test/v1", config)
        assert session.request.call_count == 1

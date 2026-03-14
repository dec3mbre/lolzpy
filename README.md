# lolz-sdk

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/your-org/lolz-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/lolz-sdk/actions)
[![PyPI](https://img.shields.io/pypi/v/lolz-sdk)](https://pypi.org/project/lolz-sdk/)
[![Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

Typed Python SDK for the [LOLZ Forum](https://lolz.live) and [ZT.Market](https://lzt.market) APIs.

- **Full sync & async** support via [`curl_cffi`](https://github.com/yifeikong/curl_cffi) (browser TLS fingerprinting)
- **Pydantic v2** typed response models, auto-generated from OpenAPI schemas
- **Token-bucket rate limiting** (thread-safe sync + asyncio-safe async)
- **Automatic retry** with exponential backoff and `Retry-After` header support
- **Exception hierarchy** — `AuthError`, `RateLimitError`, `NotFoundError`, `ServerError`
- **Grouped API methods** — `client.forum.users.get_me()`, `client.market.purchasing.fast_buy()`
- **151 Forum + 115 Market** operations, all auto-generated from official OpenAPI specs
- **Proxy support** — HTTP, HTTPS, SOCKS5
- **PEP 561** typed package
- MIT licence

---

## Installation

```bash
pip install lolz-sdk
```

---

## Quick Start

### Synchronous

```python
from lolz_sdk import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    # Forum
    me = lolz.forum.users.get_me()
    threads = lolz.forum.threads.list(forum_id=876, limit=10)

    # Market
    profile = lolz.market.profile.get_me()
    items = lolz.market.category.all(category_name="steam")
```

### Asynchronous

```python
import asyncio
from lolz_sdk import LolzAsync

async def main():
    async with LolzAsync(token="YOUR_TOKEN") as lolz:
        me = await lolz.forum.users.get_me()
        items = await lolz.market.category.all(category_name="steam")

asyncio.run(main())
```

### Unified Client (runtime mode switching)

```python
from lolz_sdk import Lolz

# Starts in sync mode
lolz = Lolz(token="YOUR_TOKEN")
me = lolz.forum.users.get_me()

# Switch to async at runtime
lolz.use_async()
me = await lolz.forum.users.get_me()

# Switch back
lolz.use_sync()
me = lolz.forum.users.get_me()
lolz.close()
```

---

## Client Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `token` | `str` | **required** | API bearer token |
| `proxy` | `str \| None` | `None` | Proxy URL (see below) |
| `timeout` | `float` | `30.0` | HTTP timeout in seconds |
| `retry` | `RetryConfig \| None` | `RetryConfig()` | Retry configuration |
| `rate_limit` | `float` | `0.0` | Max requests/sec (0 = unlimited) |
| `impersonate` | `str` | `"chrome"` | Browser TLS fingerprint |
| `forum_base_url` | `str` | `"https://prod-api.lolz.live"` | Forum API base URL |
| `market_base_url` | `str` | `"https://prod-api.lzt.market"` | Market API base URL |

The `Lolz` unified client also accepts `async_mode: bool = False`.

---

## Proxy Support

```python
from lolz_sdk import LolzSync

# HTTP proxy
lolz = LolzSync(token="YOUR_TOKEN", proxy="http://user:pass@host:8080")

# SOCKS5 proxy
lolz = LolzSync(token="YOUR_TOKEN", proxy="socks5://user:pass@host:1080")

# HTTPS proxy
lolz = LolzSync(token="YOUR_TOKEN", proxy="https://host:8443")
```

---

## Retry Configuration

```python
from lolz_sdk import LolzSync, RetryConfig

lolz = LolzSync(
    token="YOUR_TOKEN",
    retry=RetryConfig(
        max_retries=5,          # Max retry attempts (default: 3)
        initial_delay=1.0,      # Initial backoff delay in seconds (default: 0.5)
        max_delay=16.0,         # Max backoff delay (default: 8.0)
        max_retry_after=120.0,  # Max Retry-After header value to respect (default: 60.0)
    ),
)
```

Retries automatically on: `429`, `500`, `502`, `503`, `504` with exponential backoff + ±25% jitter.

---

## Rate Limiting

```python
from lolz_sdk import LolzSync

# Token-bucket: max 3 requests per second
lolz = LolzSync(token="YOUR_TOKEN", rate_limit=3.0)
```

The rate limiter is thread-safe (sync) and asyncio-safe (async). Set `rate_limit=0.0` to disable.

---

## Error Handling

```python
from lolz_sdk import LolzSync, AuthError, RateLimitError, NotFoundError, ServerError, LolzError

with LolzSync(token="YOUR_TOKEN") as lolz:
    try:
        user = lolz.forum.users.get(user_id=123)
    except AuthError as e:
        print(f"Auth failed ({e.status_code}): {e.message}")
    except RateLimitError as e:
        print(f"Rate limited, retry after {e.retry_after}s")
    except NotFoundError:
        print("User not found")
    except ServerError as e:
        print(f"Server error: {e.status_code}")
    except LolzError as e:
        print(f"API error: {e.message}")
```

### Exception Hierarchy

| Exception | HTTP Codes | Description |
|---|---|---|
| `LolzError` | all | Base exception |
| `AuthError` | 401, 403 | Authentication / authorization failure |
| `NotFoundError` | 404 | Resource not found |
| `RateLimitError` | 429 | Rate limit exceeded (includes `retry_after`) |
| `ServerError` | 5xx | Server-side error |
| `ValidationError` | — | Response doesn't match expected Pydantic model |

---

## Forum API Examples

```python
from lolz_sdk import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    # Users
    me = lolz.forum.users.get_me()
    user = lolz.forum.users.get(user_id=2410024)
    followers = lolz.forum.users.followers(user_id=2410024)

    # Threads
    threads = lolz.forum.threads.list(forum_id=876, limit=20)
    thread = lolz.forum.threads.get(thread_id=1234567)
    new_thread = lolz.forum.threads.create(
        forum_id=876,
        thread_title="Hello World",
        post_body="My first thread via SDK.",
    )

    # Posts
    posts = lolz.forum.posts.list(thread_id=1234567)
    new_post = lolz.forum.posts.create(thread_id=1234567, post_body="Reply via SDK")

    # Conversations
    convs = lolz.forum.conversations.list()
    new_conv = lolz.forum.conversations.create(
        recipient_id=2410024,
        message_body="Hi!",
        conversation_title="Hello",
    )

    # Search
    results = lolz.forum.search.search(q="python sdk")
```

---

## Market API Examples

```python
from lolz_sdk import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    # Profile
    profile = lolz.market.profile.get_me()

    # Browse items
    items = lolz.market.category.all(category_name="steam")

    # Purchase
    bought = lolz.market.purchasing.fast_buy(item_id=12345678, price=100, currency="rub")

    # Manage listings
    listings = lolz.market.managing.list()

    # Payments
    payments = lolz.market.payments.list()

    # Cart
    cart = lolz.market.cart.list()
```

---

## Context Managers

All client classes support context managers for automatic cleanup:

```python
# Sync
with LolzSync(token="YOUR_TOKEN") as lolz:
    ...

# Async
async with LolzAsync(token="YOUR_TOKEN") as lolz:
    ...

# Unified — sync
with Lolz(token="YOUR_TOKEN") as lolz:
    ...

# Unified — async
async with Lolz(token="YOUR_TOKEN", async_mode=True) as lolz:
    ...
```

---

## Project Structure

```
lolz_sdk/
├── __init__.py             # Public API: LolzSync, LolzAsync, Lolz
├── _version.py             # Version string
├── py.typed                # PEP 561 marker
├── core/                   # Public: config, exceptions, types
│   ├── config.py           # RetryConfig
│   ├── exceptions.py       # Exception hierarchy
│   └── types.py            # Type aliases
├── _internal/              # Private: transport layer
│   ├── base_client.py      # SyncAPIClient, AsyncAPIClient
│   ├── rate_limit.py       # TokenBucketSync, TokenBucketAsync
│   └── retry.py            # Retry logic, backoff
├── forum/                  # Forum API (auto-generated)
│   ├── _client.py          # 151 operations in 18 groups
│   └── _models.py          # Pydantic v2 models
└── market/                 # Market API (auto-generated)
    ├── _client.py           # 115 operations in 14 groups
    └── _models.py           # Pydantic v2 models

codegen/                    # Code generation tooling
├── schemas/                # OpenAPI specs (forum.json, market.json)
├── parser.py               # OpenAPI → ParsedSpec
├── renderer.py             # Jinja2 → Python
├── templates/              # Jinja2 templates
└── generate.py             # CLI: python -m codegen --all
```

---

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Lint
ruff check lolz_sdk/

# Type check
pyright lolz_sdk/

# Regenerate clients from OpenAPI schemas
pip install -e ".[codegen]"
python -m codegen --all
```

---

## License

MIT — see [LICENSE](LICENSE).

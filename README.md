# lolz-sdk

Typed Python SDK for LOLZ Forum & Market APIs with sync and async support.

## Installation

```bash
pip install lolz-sdk
```

## Quick Start

### Synchronous

```python
from lolz_sdk import LolzSync

with LolzSync(token="your_token") as lolz:
    # Forum API
    threads = lolz.forum.threads.list(forum_id=876)
    user = lolz.forum.users.get(user_id=1)

    # Market API
    items = lolz.market.category.steam(pmin=100, pmax=500)
    account = lolz.market.managing.get(item_id=123456)
```

### Asynchronous

```python
import asyncio
from lolz_sdk import LolzAsync

async def main():
    async with LolzAsync(token="your_token") as lolz:
        threads = await lolz.forum.threads.list(forum_id=876)
        items = await lolz.market.category.all()

asyncio.run(main())
```

## Configuration

### Proxy

```python
lolz = LolzSync(
    token="your_token",
    proxy="http://user:pass@proxy.example.com:3128",
    # SOCKS5: proxy="socks5://localhost:1080"
)
```

### Retry & Rate Limiting

```python
from lolz_sdk import LolzSync, RetryConfig

lolz = LolzSync(
    token="your_token",
    retry=RetryConfig(
        max_retries=5,          # default: 3
        initial_delay=1.0,      # default: 0.5s
        max_delay=16.0,         # default: 8.0s
    ),
    rate_limit=3.0,             # max 3 requests/second (0 = disabled)
)
```

### Error Handling

```python
from lolz_sdk import LolzSync, AuthError, RateLimitError, NotFoundError, ServerError

with LolzSync(token="your_token") as lolz:
    try:
        user = lolz.forum.users.get(user_id=1)
    except AuthError:
        print("Invalid or expired token")
    except NotFoundError:
        print("User not found")
    except RateLimitError as e:
        print(f"Rate limited, retry after {e.retry_after}s")
    except ServerError:
        print("Server error (5xx)")
```

## API Reference

### Forum Resources

| Resource | Access | Example Methods |
|----------|--------|----------------|
| `forum.threads` | Threads | `list`, `get`, `create`, `edit`, `delete` |
| `forum.posts` | Posts | `list`, `get`, `create`, `edit`, `delete` |
| `forum.users` | Users | `list`, `get`, `edit`, `find` |
| `forum.categories` | Categories | `list`, `get` |
| `forum.forums` | Forums | `list`, `get`, `follow`, `unfollow` |
| `forum.conversations` | Conversations | `list`, `get`, `create`, `delete` |
| `forum.notifications` | Notifications | `list`, `get`, `read` |
| `forum.search` | Search | `all`, `threads`, `posts` |
| `forum.profile_posts` | Profile Posts | `list`, `get`, `create` |
| `forum.chatbox` | Chatbox | `index`, `get_messages` |
| `forum.tags` | Tags | `popular`, `list` |

### Market Resources

| Resource | Access | Example Methods |
|----------|--------|----------------|
| `market.category` | Category Search | `all`, `steam`, `fortnite`, `telegram`, ... |
| `market.managing` | Account Managing | `get`, `edit`, `open`, `close`, `bump` |
| `market.purchasing` | Purchasing | `fast_buy`, `check`, `confirm` |
| `market.publishing` | Publishing | `fast_sell`, `add` |
| `market.payments` | Payments | `get`, `history`, `transfer` |
| `market.cart` | Cart | `get`, `add`, `delete` |
| `market.proxy` | Proxy | `get`, `create`, `delete` |
| `market.list` | Account Lists | `user`, `orders`, `fave`, `viewed` |

## Development

### Regenerate API clients from OpenAPI specs

```bash
pip install -e ".[codegen]"
python -m codegen.generate --all
```

### Add a new API schema

1. Place the OpenAPI JSON in `schemas/`
2. Add entry to `SCHEMAS` dict in `codegen/generate.py`
3. Run `python -m codegen.generate --all`
4. Wire the new subpackage in `lolz_sdk/__init__.py`

## License

MIT

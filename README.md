# lolzpy

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/lolzpy)](https://pypi.org/project/lolzpy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/dec3mbre/lolz-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/dec3mbre/lolz-sdk/actions)
[![Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

Типизированный Python SDK для [LOLZ Forum](https://lolz.live) и [ZT.Market](https://lzt.market).

- 151 операция Forum API, 115 операций Market API
- Pydantic v2 модели, авто-генерация из OpenAPI
- Token-bucket rate limiting
- Автоматический retry: по HTTP-кодам, по типам исключений, с хуком
- Браузерный TLS fingerprint через `curl_cffi`
- Sync, async и универсальный клиент

---

## Содержание

- [Установка](#установка)
- [Быстрый старт](#быстрый-старт)
- [Параметры клиента](#параметры-клиента)
- [Retry](#retry)
- [Rate Limiting](#rate-limiting)
- [Обработка ошибок](#обработка-ошибок)
- [Примеры](#примеры)
- [Кодогенерация](#кодогенерация)
- [Разработка](#разработка)

---

## Установка

```bash
pip install lolzpy
```

---

## Быстрый старт

```python
from lolzpy import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    user    = lolz.forum.users.get(user_id=4565608)
    profile = lolz.market.profile.get()
    items   = lolz.market.category.steam()
```

**Async:**

```python
import asyncio
from lolzpy import LolzAsync

async def main():
    async with LolzAsync(token="YOUR_TOKEN") as lolz:
        user  = await lolz.forum.users.get(user_id=4565608)
        items = await lolz.market.category.steam()

asyncio.run(main())
```

**Переключение режима в рантайме:**

```python
from lolzpy import Lolz

lolz = Lolz(token="YOUR_TOKEN")

user = lolz.forum.users.get(user_id=4565608)

lolz.use_async()
user = await lolz.forum.users.get(user_id=4565608)

lolz.use_sync()
lolz.close()
```

---

## Параметры клиента

| Параметр | По умолчанию | Описание |
|---|---|---|
| `token` | — | Bearer-токен API |
| `proxy` | `None` | `http://`, `https://`, `socks5://` |
| `connect_timeout` | `10.0` | Таймаут установки соединения (секунды) |
| `read_timeout` | `30.0` | Таймаут чтения ответа (секунды) |
| `rate_limit` | `0.0` | Макс. запросов/сек (0 = без лимита) |
| `retry` | `RetryConfig()` | Настройки повторных запросов |
| `impersonate` | `"chrome"` | TLS-отпечаток: `"chrome"`, `"firefox"`, `"safari"`, `"edge"` |
| `forum_base_url` | `https://prod-api.lolz.live` | |
| `market_base_url` | `https://prod-api.lzt.market` | |

`Lolz` дополнительно принимает `async_mode: bool = False`.

---

## Retry

`RetryConfig` полностью настраиваем: коды, типы исключений и хук на каждую попытку.

```python
import logging
from lolzpy import LolzSync, RetryConfig

logger = logging.getLogger(__name__)

lolz = LolzSync(
    token="YOUR_TOKEN",
    retry=RetryConfig(
        max_retries=5,
        initial_delay=1.0,       # начальная задержка (секунды)
        max_delay=16.0,          # максимальная задержка
        max_retry_after=120.0,   # максимальный Retry-After из заголовка
        retry_on=[429, 500, 502, 503, 504],  # HTTP-коды для retry
        retry_on_exceptions=[
            ConnectionError,
            TimeoutError,
        ],
        on_retry=lambda attempt, delay: logger.warning(
            f"retry {attempt}, wait {delay:.1f}s"
        ),
    ),
)
```

**Поведение:**

- `429` всегда обрабатывается отдельно: задержка берётся из заголовка `Retry-After`, если он присутствует
- Остальные коды из `retry_on` используют экспоненциальный backoff ± 25% jitter
- `retry_on_exceptions` покрывает сетевые ошибки, не имеющие HTTP-кода
- `on_retry` вызывается перед каждой повторной попыткой — удобно для логирования и метрик

Дефолтный `RetryConfig()` соответствует прежнему поведению — обратная совместимость сохраняется.

---

## Rate Limiting

```python
from lolzpy import LolzSync

# Token-bucket: максимум 3 запроса в секунду
lolz = LolzSync(token="YOUR_TOKEN", rate_limit=3.0)
```

Алгоритм — token bucket. Потокобезопасен (sync) и asyncio-safe (async). `0.0` — без ограничений.

---

## Обработка ошибок

Все исключения содержат `request_url` и `request_method` — сразу видно какой вызов упал:

```python
from lolzpy import AuthError, RateLimitError, NotFoundError, ServerError, LolzError

try:
    user = lolz.forum.users.get(user_id=123)
except AuthError as e:
    # e.status_code, e.message, e.request_url, e.request_method
    print(f"{e.request_method} {e.request_url} → {e.status_code}: {e.message}")
except RateLimitError as e:
    # e.retry_after — секунды из Retry-After или None
    print(f"rate limited, retry after {e.retry_after}s")
except NotFoundError as e:
    print(f"not found: {e.request_url}")
except ServerError as e:
    print(f"server error {e.status_code}")
except LolzError as e:
    print(e.message)
```

**Иерархия исключений:**

```
LolzError               ← message, status_code, response_data, request_url, request_method
├── AuthError           ← 401, 403
├── NotFoundError       ← 404
├── RateLimitError      ← 429: + retry_after
├── ServerError         ← 5xx
└── ValidationError     ← ответ не соответствует Pydantic-модели
```

---

## Примеры

**Forum API:**

```python
with LolzSync(token="YOUR_TOKEN") as lolz:
    user      = lolz.forum.users.get(user_id=2410024)
    followers = lolz.forum.users.followers(user_id=2410024)
    threads   = lolz.forum.threads.list(forum_id=876, limit=20)
    thread    = lolz.forum.threads.get(thread_id=1234567)
    post      = lolz.forum.posts.create(thread_id=1234567, post_body="...")
    conv      = lolz.forum.conversations.create(
                    recipient_id=2410024,
                    message_body="Привет!",
                    conversation_title="Приветствие",
                )
    results   = lolz.forum.search.search(q="python sdk")
```

**Market API:**

```python
with LolzSync(token="YOUR_TOKEN") as lolz:
    profile  = lolz.market.profile.get()
    items    = lolz.market.category.steam()
    bought   = lolz.market.purchasing.fast_buy(item_id=12345678, price=100)
    listings = lolz.market.managing.bulk_get()
    payments = lolz.market.payments.list()
    cart     = lolz.market.cart.get()
```

**Прокси:**

```python
lolz = LolzSync(token="YOUR_TOKEN", proxy="socks5://user:pass@host:1080")
```

---

## Структура проекта

```
lolzpy/
├── core/           # RetryConfig, исключения, типы
├── _internal/      # HTTP-клиент, rate limiter, retry
├── forum/          # Forum API: _client.py, _models.py  ← авто-генерация
└── market/         # Market API: _client.py, _models.py ← авто-генерация

codegen/            # Кодогенерация из OpenAPI
├── schemas/        # forum.json, market.json
├── parser.py
├── renderer.py
└── templates/
```

---

## Кодогенерация

```bash
pip install -e ".[codegen]"

# Все API сразу
python -m codegen.generate --all

# Один API
python -m codegen.generate --schema codegen/schemas/forum.json --name forum
python -m codegen.generate --schema codegen/schemas/market.json --name market
```

Обновление при изменении API: заменить схему → перегенерировать → `pytest tests/ -v`.

---

## Разработка

```bash
pip install -e ".[dev]"

pytest tests/ -v   # юнит и интеграционные тесты
ruff check lolzpy/
pyright lolzpy/
```

### Live-тесты (реальный API)

Live-тесты отправляют запросы к настоящему API. Для запуска нужен токен:

```bash
LOLZ_TOKEN=your_token pytest tests/live/ -v -s
```

| Флаг | Описание |
|---|---|
| `-v` | Подробный вывод |
| `-s` | Показать `print()` — ответы API |

Можно запустить отдельно Forum или Market:

```bash
LOLZ_TOKEN=your_token pytest tests/live/test_forum.py -v -s
LOLZ_TOKEN=your_token pytest tests/live/test_market.py -v -s
```

Без `LOLZ_TOKEN` live-тесты автоматически пропускаются.

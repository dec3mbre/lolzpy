# lolzpy

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/your-org/lolzpy/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/lolzpy/actions)
[![PyPI](https://img.shields.io/pypi/v/lolzpy)](https://pypi.org/project/lolzpy/)
[![Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

Типизированный Python SDK для API [LOLZ Forum](https://lolz.live) и [ZT.Market](https://lzt.market).

---

## Преимущества SDK

| Возможность | lolzpy | Аналоги |
|---|:---:|:---:|
| **Типизированные ответы** (Pydantic v2) | ✅ | ❌ `dict` |
| **Иерархия исключений** (`AuthError`, `RateLimitError`, …) | ✅ | ❌ общий `Exception` |
| **Token-bucket rate limiting** (thread-safe + asyncio-safe) | ✅ | ❌ `time.sleep` |
| **Автоматический retry** с экспоненциальным backoff и jitter | ✅ | ❌ |
| **Поддержка `Retry-After` заголовка** | ✅ | ❌ |
| **Браузерный TLS fingerprint** (обход Cloudflare) | ✅ curl_cffi | ❌ httpx |
| **Полное покрытие Market API** (115 операций) | ✅ | Частичное |
| **Полное покрытие Forum API** (151 операция) | ✅ | Частичное |
| **Авто-генерация из OpenAPI** спецификаций | ✅ | ❌ Ручной код |
| **Unit-тесты** | 114 тестов | 0 |
| **CI/CD** (GitHub Actions) | ✅ | ❌ |
| **PEP 561** (типизированный пакет) | ✅ | ❌ |
| **Переключение sync/async** в рантайме | ✅ | ✅ |
| **Группированные методы** (`client.forum.users.get_me()`) | ✅ | ✅ |
| **Поддержка прокси** (HTTP, HTTPS, SOCKS5) | ✅ | ✅ |

---

## Почему именно этот стек

### curl_cffi вместо httpx / requests

[curl_cffi](https://github.com/yifeikong/curl_cffi) — обёртка над libcurl с поддержкой **браузерного TLS fingerprint**. LOLZ API защищён Cloudflare — стандартные HTTP-клиенты (`httpx`, `requests`, `aiohttp`) отправляют TLS-отпечаток Python, который легко блокируется. `curl_cffi` имитирует отпечаток настоящего браузера (Chrome, Firefox, Safari), что на порядок повышает стабильность работы.

| | curl_cffi | httpx | requests |
|---|:---:|:---:|:---:|
| TLS fingerprint браузера | ✅ | ❌ | ❌ |
| Sync + Async в одной библиотеке | ✅ | ✅ | ❌ |
| HTTP/2 | ✅ | ✅ | ❌ |
| SOCKS5 прокси | ✅ | Через плагин | Через плагин |
| Скорость | ≈ libcurl (C) | Python | Python |

### Pydantic v2 вместо сырых `dict`

Все ответы API десериализуются в **типизированные модели Pydantic v2**. Это даёт:

- **Автодополнение в IDE** — IDE подсказывает доступные поля и их типы
- **Валидация на лету** — неожиданный формат ответа сразу выбросит `ValidationError` вместо `KeyError` в рантайме
- **Скорость** — Pydantic v2 написан на Rust, валидация в 5-50× быстрее v1
- **Документируемость** — модели служат живой документацией API

```python
me = lolz.forum.users.get_me()
print(me.user.username)      # IDE знает тип: str
print(me.user.user_id)       # IDE знает тип: int
# me.nonexistent_field       # IDE покажет ошибку ещё до запуска
```

### Авто-генерация из OpenAPI

Клиентский код и модели **генерируются автоматически** из официальных OpenAPI-схем LOLZ. Это гарантирует:

- **Полное покрытие** — все 266 операций (151 Forum + 115 Market) без ручного пропуска
- **Актуальность** — обновление API = перегенерация одной командой
- **Отсутствие человеческих ошибок** — опечатки и несовпадение сигнатур исключены

### Token-bucket rate limiting

Вместо примитивного `time.sleep(3)` между запросами используется **алгоритм token bucket**:

- Потокобезопасный (sync) и asyncio-safe (async)
- Равномерное распределение запросов, а не burst + пауза
- Настраиваемый лимит через параметр `rate_limit`

### Иерархия исключений

Вместо единого `Exception` — конкретные классы с полезной информацией:

```python
try:
    user = lolz.forum.users.get(user_id=123)
except AuthError as e:
    # e.status_code = 401/403, e.message = "..."
except RateLimitError as e:
    # e.retry_after = 2.5 (секунды, из заголовка Retry-After)
except NotFoundError:
    # 404
except ServerError:
    # 5xx
```

---

## Установка

```bash
pip install lolzpy
```

---

## Быстрый старт

### Синхронный клиент

```python
from lolzpy import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    # Forum
    me = lolz.forum.users.get_me()
    threads = lolz.forum.threads.list(forum_id=876, limit=10)

    # Market
    profile = lolz.market.profile.get_me()
    items = lolz.market.category.all(category_name="steam")
```

### Асинхронный клиент

```python
import asyncio
from lolzpy import LolzAsync

async def main():
    async with LolzAsync(token="YOUR_TOKEN") as lolz:
        me = await lolz.forum.users.get_me()
        items = await lolz.market.category.all(category_name="steam")

asyncio.run(main())
```

### Универсальный клиент (переключение в рантайме)

```python
from lolzpy import Lolz

# По умолчанию — синхронный режим
lolz = Lolz(token="YOUR_TOKEN")
me = lolz.forum.users.get_me()

# Переключение на async
lolz.use_async()
me = await lolz.forum.users.get_me()

# Обратно на sync
lolz.use_sync()
me = lolz.forum.users.get_me()
lolz.close()
```

---

## Параметры клиента

| Параметр | Тип | По умолчанию | Описание |
|---|---|---|---|
| `token` | `str` | **обязательный** | Bearer-токен API |
| `proxy` | `str \| None` | `None` | URL прокси (см. ниже) |
| `timeout` | `float` | `30.0` | Таймаут HTTP-запроса (секунды) |
| `retry` | `RetryConfig \| None` | `RetryConfig()` | Настройки повторных запросов |
| `rate_limit` | `float` | `0.0` | Макс. запросов/сек (0 = без лимита) |
| `impersonate` | `str` | `"chrome"` | TLS-отпечаток браузера |
| `forum_base_url` | `str` | `"https://prod-api.lolz.live"` | Базовый URL Forum API |
| `market_base_url` | `str` | `"https://prod-api.lzt.market"` | Базовый URL Market API |

Универсальный клиент `Lolz` также принимает `async_mode: bool = False`.

---

## Прокси

```python
from lolzpy import LolzSync

# HTTP
lolz = LolzSync(token="YOUR_TOKEN", proxy="http://user:pass@host:8080")

# SOCKS5
lolz = LolzSync(token="YOUR_TOKEN", proxy="socks5://user:pass@host:1080")

# HTTPS
lolz = LolzSync(token="YOUR_TOKEN", proxy="https://host:8443")
```

---

## Настройка retry

```python
from lolzpy import LolzSync, RetryConfig

lolz = LolzSync(
    token="YOUR_TOKEN",
    retry=RetryConfig(
        max_retries=5,          # Макс. попыток (по умолчанию: 3)
        initial_delay=1.0,      # Начальная задержка в секундах (по умолчанию: 0.5)
        max_delay=16.0,         # Макс. задержка (по умолчанию: 8.0)
        max_retry_after=120.0,  # Макс. Retry-After из заголовка (по умолчанию: 60.0)
    ),
)
```

Автоматический retry на: `429`, `500`, `502`, `503`, `504` с экспоненциальным backoff ± 25% jitter.

---

## Rate Limiting

```python
from lolzpy import LolzSync

# Token-bucket: максимум 3 запроса в секунду
lolz = LolzSync(token="YOUR_TOKEN", rate_limit=3.0)
```

Rate limiter потокобезопасен (sync) и asyncio-safe (async). `rate_limit=0.0` — без ограничений.

---

## Обработка ошибок

```python
from lolzpy import LolzSync, AuthError, RateLimitError, NotFoundError, ServerError, LolzError

with LolzSync(token="YOUR_TOKEN") as lolz:
    try:
        user = lolz.forum.users.get(user_id=123)
    except AuthError as e:
        print(f"Ошибка авторизации ({e.status_code}): {e.message}")
    except RateLimitError as e:
        print(f"Лимит запросов, повтор через {e.retry_after}с")
    except NotFoundError:
        print("Пользователь не найден")
    except ServerError as e:
        print(f"Ошибка сервера: {e.status_code}")
    except LolzError as e:
        print(f"Ошибка API: {e.message}")
```

### Иерархия исключений

| Исключение | HTTP-коды | Описание |
|---|---|---|
| `LolzError` | все | Базовое исключение |
| `AuthError` | 401, 403 | Ошибка аутентификации / авторизации |
| `NotFoundError` | 404 | Ресурс не найден |
| `RateLimitError` | 429 | Превышен лимит запросов (содержит `retry_after`) |
| `ServerError` | 5xx | Ошибка на стороне сервера |
| `ValidationError` | — | Ответ не соответствует Pydantic-модели |

---

## Примеры Forum API

```python
from lolzpy import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    # Пользователи
    me = lolz.forum.users.get_me()
    user = lolz.forum.users.get(user_id=2410024)
    followers = lolz.forum.users.followers(user_id=2410024)

    # Темы
    threads = lolz.forum.threads.list(forum_id=876, limit=20)
    thread = lolz.forum.threads.get(thread_id=1234567)
    new_thread = lolz.forum.threads.create(
        forum_id=876,
        thread_title="Hello World",
        thread_body="Моя первая тема через SDK.",
    )

    # Посты
    posts = lolz.forum.posts.list(thread_id=1234567)
    new_post = lolz.forum.posts.create(thread_id=1234567, post_body="Ответ через SDK")

    # Диалоги
    convs = lolz.forum.conversations.list()
    new_conv = lolz.forum.conversations.create(
        recipient_id=2410024,
        message_body="Привет!",
        conversation_title="Приветствие",
    )

    # Поиск
    results = lolz.forum.search.search(q="python sdk")
```

---

## Примеры Market API

```python
from lolzpy import LolzSync

with LolzSync(token="YOUR_TOKEN") as lolz:
    # Профиль
    profile = lolz.market.profile.get_me()

    # Просмотр аккаунтов
    items = lolz.market.category.all(category_name="steam")

    # Покупка
    bought = lolz.market.purchasing.fast_buy(item_id=12345678, price=100, currency="rub")

    # Управление лотами
    listings = lolz.market.managing.list()

    # Платежи
    payments = lolz.market.payments.list()

    # Корзина
    cart = lolz.market.cart.list()
```

---

## Контекстные менеджеры

Все клиенты поддерживают контекстные менеджеры для автоматического закрытия соединений:

```python
# Sync
with LolzSync(token="YOUR_TOKEN") as lolz:
    ...

# Async
async with LolzAsync(token="YOUR_TOKEN") as lolz:
    ...

# Универсальный — sync
with Lolz(token="YOUR_TOKEN") as lolz:
    ...

# Универсальный — async
async with Lolz(token="YOUR_TOKEN", async_mode=True) as lolz:
    ...
```

---

## Структура проекта

```
lolzpy/
├── __init__.py             # Публичный API: LolzSync, LolzAsync, Lolz
├── _version.py             # Версия пакета
├── py.typed                # PEP 561 маркер
├── core/                   # Публичное: конфигурация, исключения, типы
│   ├── config.py           # RetryConfig
│   ├── exceptions.py       # Иерархия исключений
│   └── types.py            # Алиасы типов
├── _internal/              # Приватное: транспортный слой
│   ├── base_client.py      # SyncAPIClient, AsyncAPIClient
│   ├── rate_limit.py       # TokenBucketSync, TokenBucketAsync
│   └── retry.py            # Логика retry, backoff
├── forum/                  # Forum API (авто-генерация)
│   ├── _client.py          # 151 операция в 18 группах
│   └── _models.py          # Pydantic v2 модели
└── market/                 # Market API (авто-генерация)
    ├── _client.py          # 115 операций в 14 группах
    └── _models.py          # Pydantic v2 модели

codegen/                    # Инструменты кодогенерации
├── schemas/                # OpenAPI-схемы (forum.json, market.json)
├── parser.py               # OpenAPI → ParsedSpec
├── renderer.py             # Jinja2 → Python
├── templates/              # Jinja2 шаблоны
└── generate.py             # CLI: python -m codegen --all
```

---

## Разработка

```bash
# Установка dev-зависимостей
pip install -e ".[dev]"

# Запуск тестов
pytest tests/ -v

# Линтинг
ruff check lolzpy/

# Проверка типов
pyright lolzpy/

# Перегенерация клиентов из OpenAPI-схем
pip install -e ".[codegen]"
python -m codegen --all
```

---

## Лицензия

MIT — см. [LICENSE](LICENSE).

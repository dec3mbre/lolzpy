"""
quickstart.py — Быстрый старт с lolzpy SDK.

Вставьте свой токен в переменную TOKEN ниже и запустите скрипт:

    python examples/quickstart.py

Скрипт демонстрирует основные возможности SDK:
  • Профиль маркета
  • Форумы и категории
  • Категории маркета
  • Поиск аккаунтов (Steam)
  • Курсы валют
  • Async-пример
"""

from __future__ import annotations

import json

from lolzpy import LolzSync

# ──────────────────────────────────────────────────────────────
#  Вставьте сюда ваш токен
# ──────────────────────────────────────────────────────────────
TOKEN = "YOUR_TOKEN"

SEPARATOR = "=" * 60


def pp(data: object) -> None:
    """Красивый вывод dict / list через json."""
    if isinstance(data, (dict, list)):
        print(json.dumps(data, indent=2, ensure_ascii=False, default=str))
    else:
        print(data)


def main() -> None:
    if TOKEN == "YOUR_TOKEN":
        print("⚠  Замените TOKEN на ваш реальный токен и перезапустите скрипт.")
        return

    # rate_limit=3.0 — рекомендуемая задержка между запросами (сек)
    client = LolzSync(TOKEN, rate_limit=3.0)

    # ── 1. Профиль ──────────────────────────────────────────
    print(SEPARATOR)
    print("1. Профиль маркета (market.profile.get)")
    print(SEPARATOR)
    try:
        me = client.market.profile.get()
        print(f"  user_id  : {me.user_id}")
        print(f"  username : {me.username}")
        print(f"  balance  : {me.balance} {me.currency}")
        print(f"  hold     : {me.hold}")
        print(f"  Продано  : {me.sold_items_count}")
        print(f"  Активных : {me.active_items_count}")
    except Exception as exc:
        print(f"  Ошибка: {exc}")

    # ── 2. Форумы ───────────────────────────────────────────
    print()
    print(SEPARATOR)
    print("2. Форумы (forum.forums.list)")
    print(SEPARATOR)
    try:
        forums = client.forum.forums.list()
        forum_list = forums.get("forums", [])
        print(f"  Всего форумов: {len(forum_list)}")
        for f in forum_list[:5]:
            print(f"  • [{f.get('forum_id')}] {f.get('forum_title')}")
        if len(forum_list) > 5:
            print(f"  ... и ещё {len(forum_list) - 5}")
    except Exception as exc:
        print(f"  Ошибка: {exc}")

    # ── 3. Категории форума ─────────────────────────────────
    print()
    print(SEPARATOR)
    print("3. Категории форума (forum.categories.list)")
    print(SEPARATOR)
    try:
        cats = client.forum.categories.list()
        cat_list = cats.get("categories", [])
        print(f"  Всего категорий: {len(cat_list)}")
        for c in cat_list[:5]:
            print(f"  • [{c.get('category_id')}] {c.get('category_title')}")
        if len(cat_list) > 5:
            print(f"  ... и ещё {len(cat_list) - 5}")
    except Exception as exc:
        print(f"  Ошибка: {exc}")

    # ── 4. Маркет: категории ────────────────────────────────
    print()
    print(SEPARATOR)
    print("4. Категории маркета (market.category.list)")
    print(SEPARATOR)
    try:
        market_cats = client.market.category.list()
        pp(market_cats)
    except Exception as exc:
        print(f"  Ошибка: {exc}")

    # ── 5. Маркет: поиск Steam-аккаунтов ───────────────────
    print()
    print(SEPARATOR)
    print("5. Поиск Steam-аккаунтов (market.category.steam)")
    print("   Фильтр: цена 50–200 ₽, первая страница")
    print(SEPARATOR)
    try:
        steam = client.market.category.steam(pmin=50, pmax=200, page=1)
        items = steam.get("items", [])
        total = steam.get("totalItems", "?")
        print(f"  Найдено всего: {total}")
        print(f"  На странице  : {len(items)}")
        for item in items[:3]:
            print(
                f"  • [{item.get('item_id')}] "
                f"{item.get('title', '—')} — "
                f"{item.get('price')} {item.get('currency', '₽')}"
            )
        if len(items) > 3:
            print(f"  ... и ещё {len(items) - 3} на этой странице")
    except Exception as exc:
        print(f"  Ошибка: {exc}")

    # ── 6. Маркет: курсы валют ──────────────────────────────
    print()
    print(SEPARATOR)
    print("6. Курсы валют (market.payments.currency)")
    print(SEPARATOR)
    try:
        currency = client.market.payments.currency()
        pp(currency)
    except Exception as exc:
        print(f"  Ошибка: {exc}")

    # ── Готово ──────────────────────────────────────────────
    print()
    print(SEPARATOR)
    print("Готово! Все секции выполнены.")
    print(SEPARATOR)

    client.close()


# ── 7. Async-пример ────────────────────────────────────────
async def main_async() -> None:
    """Тот же сценарий, но через LolzAsync (асинхронный клиент)."""
    from lolzpy import LolzAsync

    if TOKEN == "YOUR_TOKEN":
        print("⚠  Замените TOKEN на ваш реальный токен.")
        return

    async with LolzAsync(TOKEN, rate_limit=3.0) as client:
        # Профиль
        me = await client.market.profile.get()
        print(f"[async] {me.username} — баланс {me.balance} {me.currency}")

        # Форумы
        forums = await client.forum.forums.list()
        print(f"[async] Форумов: {len(forums.get('forums', []))}")

        # Steam-аккаунты
        steam = await client.market.category.steam(pmin=50, pmax=200, page=1)
        print(f"[async] Steam-аккаунтов на странице: {len(steam.get('items', []))}")


if __name__ == "__main__":
    main()

    # Раскомментируйте для запуска async-версии:
    # import asyncio
    # asyncio.run(main_async())

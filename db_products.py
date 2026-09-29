import sqlite3
from config import db_path


def get_all_products():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    products = cur.fetchall()
    conn.close()
    return products


def get_products_by_category(trener):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE тренер = ?", (trener,))
    products = cur.fetchall()
    conn.close()
    return products


def get_products_low_stock():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE количество <= 9")
    products = cur.fetchall()
    conn.close()
    return products


def get_trener():
    """Список всех категорий."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT тренер FROM Товар ORDER BY тренер")
    treners = [row[0] for row in cur.fetchall()]
    conn.close()
    return treners


def print_catalog(products):
    """Каталог с индикатором."""
    print(f"\n{'=' * 60}")
    print(f"КАТАЛОГ ({len(products)} товаров)")
    print("=" * 60)

    for p in products:
        # ⚠️ Замените индексы на свои!
        name = p[1]
        category = p[2]
        price = p[4]
        qty = p[5]

        indicator = "много" if qty > 12 else "мало"
        highlight = "⚠️" if qty <= 9 else "  "

        print(f"{highlight} {name} ({category})")
        print(f"   Цена: {price} руб. | Кол-во: {qty} ({indicator})")

    print("=" * 60)


if __name__ == "__main__":
    print("1. Все товары")
    print_catalog(get_all_products())

    print("\n2. Тренеры:")
    for cat in get_trener():
        print(f"   - {cat}")

    print("\n3. Товары с низким остатком (≤9):")
    print_catalog(get_products_low_stock())


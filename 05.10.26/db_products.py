import sqlite3
from config import DB_PATH
from models import Products


def get_all_products():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар ORDER BY id")
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = Products(
            id=row[0],
            name=row[1],
            coach=row[2],
            time=row[3],
            price=row[4],
            qty=row[5],
            picture=row[6]
        )
        products.append(product)
    return products




def get_products_by_category(trener):
    conn = sqlite3.connect()
    cur = conn.cursor(DB_PATH)
    cur.execute("SELECT * FROM Товар WHERE тренер = ?", (trener,))
    rows = cur.fetchall()
    conn.close()
    
    products = []
    for row in rows:
        product = Products(
            id=row[0],
            name=row[1],
            coach=row[2],
            time=row[3],
            price=row[4],
            qty=row[5],
            picture=row[6]
        )
        products.append(product)
    return products


def get_products_low_stock():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Товар WHERE количество <= 9")
    rows = cur.fetchall()
    conn.close()
    products = []
    for row in rows:
        product = Products(
            id=row[0],
            name=row[1],
            coach=row[2],
            time=row[3],
            price=row[4],
            qty=row[5],
            picture=row[6]
        )
    return products


def get_trener():
    """Список всех категорий."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT тренер FROM Товар ORDER BY тренер")
    treners = [row[0] for row in cur.fetchall()]
    conn.close()
    return treners


def print_products(products):
    """Выводит информацию о товарах."""
    print(f"\nВсего товаров: {len(products)}\n")
    for p in products:
        print(p.info())
        print("-" * 60)


def print_catalog_with_highlight(products):
    print(f"\n{'=' * 70}")
    print(f"КАТАЛОГ ({len(products)} товаров)")
    print("=" * 70)

    for p in products:
        highlight = "⚠️" if p.qty <= 9 else "  "
        print(f"{highlight} {p.info()}")

    print("=" * 70)


if __name__ == "__main__":
    print("1. Все товары:")
    print_catalog_with_highlight(get_all_products())

    print("\n2. Товары категории «Тренер»:")
    print_catalog_with_highlight(get_products_by_category("Ольга Морозова"))

    print("\n3. Товары с низким остатком (≤9):")
    print_catalog_with_highlight(get_products_low_stock())



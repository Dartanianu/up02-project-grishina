import sqlite3
from datetime import datetime
from config import db_path
from models import Products


def get_all_products():
    conn = sqlite3.connect(db_path)
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


def apply_discount_to_best_seller(products, discount):
    if not products:
        return None, None, None
    max_training = max(products, key=lambda p: p.qty)
    old_price = max_training.price
    new_price = max_training.price * (1 - discount / 100)
    max_training.price = new_price
    return max_training, old_price, new_price
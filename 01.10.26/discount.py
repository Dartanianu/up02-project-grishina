import sqlite3
from datetime import datetime, timedelta
from config import db_path
from models import Products, Order


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


def get_all_products_orders():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT Товар.id, Товар.цена, Товар.количество, Заказ.товар_id, Заказ.дата FROM Товар ORDER BY id")
    rows = cur.fetchall()
    conn.close()

    orders = []
    for row in rows:
        product = Products(
            id=row[0],
            price=row[1],
            qty=row[2]
        )

        order = Order(
            data=row[3],
            product=product,
        )
        orders.append(order)
    return orders


def apply_discount_to_best_seller(products, discount):
    if not products:
        return None, None, None
    max_training = max(products, key=lambda p: p.qty)
    old_price = max_training.price
    new_price = max_training.price * (1 - discount / 100)
    max_training.price = new_price
    return max_training, old_price, new_price

def apply_discount_to_any_orders(products, orders, discount, current_date=None):
    if not products:
        return None, None, None

    if current_date is None:
        current_date = datetime.now

    first_day_this_month = current_date.replace(day=1)
    last_day_prev_month = first_day_this_month - timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)

    orders_ids = {
        o.product_id for o in orders
        if first_day_prev_month <= o.date <= last_day_prev_month
    }

    candidates = [p for p in products if p.id not in orders_ids]
    
    if not candidates:
        return None, None, None
    
    best = max(candidates, key=lambda p: p.qty)
    old_price = best.price
    new_price = best.price * (1 - discount / 100)
    best.price = new_price
    
    return best, old_price, new_price
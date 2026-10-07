import sqlite3
from datetime import datetime
from config import DB_PATH


def get_connection():
    """Соединение с БД."""
    return sqlite3.connect(DB_PATH)


def add_order_to_db(client, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO Заказ (дата, клиент) VALUES (?, ?)",
        (date, client)
    )
    conn.commit()
    order_id = cur.lastrowid
    conn.close()

    return order_id


def update_product_quantity(product_id, new_quantity):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE Товар SET количество = ? WHERE id = ?", (new_quantity, product_id)
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка обновлении кол-ва товара: {e}")
        return None
    finally:
        conn.close()


def get_last_order_id():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT MAX(id) FROM Заказ")
        row = cur.fetchone()
        return row[0] if row and row[0] is not None else None
    except sqlite3.Error as e:
        print(f"Ошибка при получении последнего заказа: {e}")
        return None
    finally:
        conn.close()


def get_product_quantity(product_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT количество FROM Товар WHERE id = ?", (product_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0


def add_order_item(order_id, product_id, quantity,price):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute(
                "INSERT INTO Состав_заказа "
        "(заказ_id, товар_id, количество, цена) "
        "VALUES (?, ?, ?, ?)",
        (order_id, product_id, quantity, price)
    )
    conn.commit()
    item_id = cur.lastrowid
    conn.close
    
    return item_id


def create_order(client, items):
    
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        cur.execute(
            "INSERT INTO Заказ (дата, клиент) VALUES (?, ?)",
            (date, client)
        )
        order_id = cur.lastrowid
        
        for product_id, quantity, price in items:
            cur.execute(
                "INSERT INTO Состав_заказа "
                "(заказ_id, товар_id, количество, цена) "
                "VALUES (?, ?, ?, ?)",
                (order_id, product_id, quantity, price)
            )
            
        conn.commit()
        return order_id
    except Exception as e:
        conn.rollback()
        print(f"Ошибка создания заказа: {e}")
        return None
    finally:
        conn.close()
import sqlite3
from datetime import datetime
from config import DB_PATH


def get_connection():
    """Соединение с БД."""
    return sqlite3.connect(DB_PATH)


def add_order_to_db(client, product_id, quantity):
    conn = get_connection()
    try:
        cur = conn.cursor()
        date_now = datetime.now().strftime("%Y-%m-%d")
        cur.execute(
            "INSERT INTO Заказ (клиент, товар_id, количество, дата) VALUES (?, ?, ?, ?)", (client, product_id, quantity, date_now)
        )
        conn.commit()
        return cur.lastrowid
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении заказа {e}")
        return None
    finally:
        conn.close()


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

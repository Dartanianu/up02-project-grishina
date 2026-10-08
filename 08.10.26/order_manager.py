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


def get_all_orders():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, дата, клиент, товар_id FROM Заказ ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_order_items(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
        Состав_заказа.id, Товар.тип,
        Состав_заказа.количество,
        Состав_заказа.цена
        FROM Состав_заказа
        JOIN Товар ON Состав_заказа.товар_id = Товар.id
        WHERE Состав_заказа.заказ_id = ?
    """, (order_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_order_total(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUM(количество * цена)
        FROM Состав_заказа
        WHERE заказ_id = ?
    """, (order_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] or 0.0

def update_order_date(order_id, new_date):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "UPDATE Заказ SET дата = ? WHERE id = ?",
            (new_date, order_id)
        )
        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Ошибка обновления даты: {e}")
        return False

    finally:
        conn.close()

def delete_order_item(item_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Получаем данные позиции для восстановления остатков
        cur.execute("""
            SELECT товар_id, количество
            FROM Состав_заказа
            WHERE id = ?
        """, (item_id,))
        row = cur.fetchone()

        if not row:
            return False

        product_id, quantity = row

        # Удаляем
        cur.execute("DELETE FROM Состав_заказа WHERE id = ?", (item_id,))

        # Восстанавливаем остатки
        cur.execute("""
            UPDATE Товар
            SET количество = количество + ?
            WHERE id = ?
        """, (quantity, product_id))

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Ошибка удаления позиции: {e}")
        return False

    finally:
        conn.close()

     
def get_order_by_id(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, дата, клиент FROM Заказ WHERE id = ?",
                (order_id,))
    row = cur.fetchone()
    conn.close()
    return row




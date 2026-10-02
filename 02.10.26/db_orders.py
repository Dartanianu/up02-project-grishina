import sqlite3
from config import DB_PATH
from models import Products, Order


def get_all_orders():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT Заказ.id, Заказ.дата, Заказ.клиент, Заказ.количество, Товар.id, Товар.тренер, Товар.тип, Товар.длительность, Товар.цена, Товар.количество, Товар.фото FROM Заказ JOIN Товар ON Заказ.товар_id = Товар.id ORDER BY Заказ.id")
    rows = cur.fetchall()
    conn.close()

    orders = []
    for row in rows:
        product = Products(
            id=row[4],
            name=row[5],
            coach=row[6],
            time=row[7],
            price=row[8],
            qty=row[9],
            picture=row[10]
        )
        
        order = Order(
            id=row[0],
            data=row[1],
            client=row[2],
            product=product,
            qty=row[3]
        )
        orders.append(order)
    return orders


def get_trener():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT тренер FROM Товар ORDER BY тренер")
    treners = [row[0] for row in cur.fetchall()]
    conn.close()
    return treners


def print_orders(orders):
    print(f"\nВсего заказов: {len(orders)}\n")
    for p in orders:
        print(p.info())
        print("-" * 60)


if __name__ == "__main__":
    print("1. Все товары:")
    print_orders(get_all_orders())
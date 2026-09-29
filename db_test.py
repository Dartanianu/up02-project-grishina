import sqlite3
from config import db_path

def test_connection():
    try:
        conn = sqlite3.connect(db_path)
        print(f"✅Подключение к {db_path} установлено")
        
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM Товар")
        count = cur.fetchone()[0]
        print(f"📦 Товаров в базе: {count}")
        
        conn.close()
        print("✅ Соединение закрыто")
    except sqlite3.Error as e:
        print(f"❌ Ошибка БД: {e}")


if __name__ == "__main__":
    test_connection()

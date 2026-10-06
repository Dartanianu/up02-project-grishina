import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Внешние ключи в SQLite надо включать отдельно
cursor.execute("PRAGMA foreign_keys = ON;")

# 1. Создаём новую таблицу с нужным FK
cursor.execute("""
    CREATE TABLE Заказ_new (
        id INTEGER PRIMARY KEY,
        дата TEXT,
        клиент INTEGER,
        товар_id INTEGER,
        FOREIGN KEY (товар_id) REFERENCES Товар(id)
    )
""")

# 2. Переносим данные
cursor.execute("""
    INSERT INTO Заказ_new (id, дата, клиент, товар_id)
    SELECT id, дата, клиент, товар_id FROM Заказ
""")

# 3. Удаляем старую и переименовываем новую
cursor.execute("DROP TABLE Заказ")
cursor.execute("ALTER TABLE Заказ_new RENAME TO Заказ")

conn.commit()
conn.close()
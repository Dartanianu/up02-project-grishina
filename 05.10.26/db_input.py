import sqlite3

conn = sqlite3.connect('databases/db_variant_24.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON')

'''
# Добавление данных для Тестировки
products = [
    ('Волейбол', 'Тимофей Каплин', 67, 1000, 17, 'volleyball.png'),
    ('Футбол', 'Арсений Лупачев', 45, 0, 5, 'football.png')
]

cursor.executemany(
    'INSERT INTO Товар (тип, тренер, длительность, цена, количество, фото) VALUES (?, ?, ?, ?, ?, ?)',
    products
)


orders = [
    ('2026-08-15', 'Петрова Анна Сергеевна', 4, 2),
    ('2026-08-20', 'Иванов Иван Иванович', 5, 1),
    ('2026-08-25', 'Петрова Анна Сергеевна', 4, 5),
    ('2026-01-15', 'Петрова Анна Сергеевна', 6, 3),
    ('2026-01-20', 'Петрова Анна Сергеевна', 2, 1),
    ('2026-01-31', 'Иванов Иван Иванович', 3, 2),
]

cursor.executemany(
    'INSERT INTO Заказ (дата, клиент, товар_id, количество) VALUES (?, ?, ?, ?)',
    orders
)


# Изменение типа данных атрибута Фото
cursor.execute('ALTER TABLE Товар DROP COLUMN фото')
cursor.execute('ALTER TABLE Товар ADD COLUMN фото VARCHAR(30) NULL')

# Добавление фото в опред строки
pictures = {
    1: 'yoga.png',
    2: 'fitness.png',
    3: 'boxing.png',
    5: 'crossfit.png',
    6: 'pilates.png',
    8: 'volleyball.png',
    9: 'football.png'
}

for user_id, path in pictures.items():
    cursor.execute("UPDATE Товар SET фото = ? WHERE id = ?", (path, user_id))



products = [
    ('Тестттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттт', 'Дарья Гришина', 0, 1000, 17, None),
    ('Сноубординг', 'Владлен Бикьюбел', 45, 10000000, 5, None)
]

cursor.executemany(
    'INSERT INTO Товар (тип, тренер, длительность, цена, количество, фото) VALUES (?, ?, ?, ?, ?, ?)',
    products
)

'''

conn.commit()
conn.close()
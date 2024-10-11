import sqlite3
import time

async def create_user(user, user_challenge):
    connection = sqlite3.connect('year_challenge.db')

    cursor = connection.cursor()
    x = time.time()
    
    # Подумать нужно ли сделать id или username уникальным
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    leap TEXT NOT NULL,
    list_money TEXT,
    added_money TEXT,
    start_amount INTEGER,
    end_amount INTEGER NOT NULL,
    initial_date timestamp DEFAULT {x},
    data_transfer timestamp
    )
    ''')

    cursor.execute(
        "INSERT into Users (id, username, leap, list_money, added_money, start_amount, end_amount, initial_date, data_transfer) VALUES (?,?,?,?,?,?,?,?,?)",
        (user, 'test', '1', '100', '0', 0, '66000', f'{x}', f'{x}'))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    connection = sqlite3.connect('year_challenge.db')

    cursor = connection.cursor()
    # Поправить запрос на добавление записи в БД
    cursor.execute(
        "INSERT into Users (id, username, leap, list_money, added_money, start_amount, end_amount, initial_date, data_transfer) VALUES (?,?,?,?,?,?,?,?,?)",
        (1, 'test', '1', '100', '0', 0, '66000', '2024-10-10', '2024-10-10'))

    connection.commit()

    cursor.execute('SELECT * FROM Users')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()

import sqlite3
import time
from year_challenge import YearChallenge


def create_user(user, user_challenge: YearChallenge):
    connection = sqlite3.connect('year_challenge.db')

    cursor = connection.cursor()

    # Подумать нужно ли сделать id или username уникальным
    # Добавить needTransfer
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    leap INTEGER NOT NULL,
    list_money TEXT,
    added_money TEXT,
    start_amount INTEGER,
    end_amount INTEGER NOT NULL,
    initial_date timestamp,
    data_transfer timestamp
    )
    ''')

    cursor.execute(
        "INSERT into Users (id, username, leap, list_money, added_money, start_amount, end_amount, initial_date, data_transfer) VALUES (?,?,?,?,?,?,?,?,?)",
        (user, 'test', user_challenge.getLeap(), user_challenge.getListMoney(), user_challenge.getAddedMoney(), user_challenge.getStartAmount(), user_challenge.getEndAmount(), user_challenge.getInitiateDate(), user_challenge.getDateTransfer()))

    connection.commit()
    connection.close()

def select_user(user):
    connection = sqlite3.connect('year_challenge.db')

    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM Users WHERE username = {user}")

    rows = cursor.fetchall()
    connection.close()
    return rows[0]

def update_user(user, user_challenge: YearChallenge):
    connection = sqlite3.connect('year_challenge.db')

    cursor = connection.cursor()

    cursor.execute(f"UPDATE Users SET * WHERE id = {user}")

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

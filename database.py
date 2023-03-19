import sqlite3

conn = sqlite3.connect("app/static/db.db",check_same_thread=False)
cursor = conn.cursor()


def get_all_from_base():
    cursor.execute("""SELECT * FROM products""")
    return cursor.fetchall()

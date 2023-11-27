import sqlite3


# połączenie z bazą
def get_conn():
    conn = sqlite3.connect('../database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn
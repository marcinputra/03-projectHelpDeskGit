import sqlite3


def execute_script(cursor, script_file):
    with open(script_file, encoding='utf-8') as file:
        query = file.read()
    cursor.executescript(query)


if __name__ == '__main__':
    conn = sqlite3.connect('../database.sqlite')
    cursor = conn.cursor()

    execute_script(cursor, 'database_user.sql')

    conn.commit()
    conn.close()
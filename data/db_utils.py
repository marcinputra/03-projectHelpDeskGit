import sqlite3


# połączenie z bazą
def get_conn():
    conn = sqlite3.connect('../database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


# jak zrobić zapytanie kiedy admin się loguje
# i ma miec wszystkie rekordy
def get_all_events(id):
    conn = get_conn()
    c = conn.cursor()
    query = """
        SELECT * FROM reports
        JOIN users 
        ON users.id = reports.id_user
        WHERE users.id = ?
    """
    result = c.execute(query, (id,))
    return result.fetchall()


def insert_event(type_e, id_user, data, state, location):
    conn = get_conn()
    c = conn.cursor()
    query = """
           INSERT INTO reports (type, id_user, data, state, location)
           VALUES (?, ?, ?, ?, ?)
       """

    params = (type_e, id_user, data, state, location)

    c.execute(query, params)
    conn.commit()

    return c.rowcount
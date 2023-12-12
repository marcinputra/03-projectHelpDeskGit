import sqlite3


# połączenie z bazą
def get_conn():
    conn = sqlite3.connect('../database.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


# jak zrobić zapytanie kiedy admin się loguje
# i ma miec wszystkie rekordy admin is_true po stronie pythona
def get_all_events(id):
    conn = get_conn()
    c = conn.cursor()

    res = c.execute('SELECT * FROM users WHERE id = ?', (id,))
    user_data = res.fetchone()
    if user_data:
        if user_data['is_admin']:
            query = """
                   SELECT * 
                   FROM reports 
                   INNER JOIN users 
                   ON users.id = reports.id_user
                   INNER JOIN events
                   ON events.id_events = reports.id_events
               """
            result = c.execute(query)
        else:
            query = """
                   SELECT * 
                   FROM reports 
                   INNER JOIN users 
                   ON users.id = reports.id_user
                   INNER JOIN events
                   ON events.id_events = reports.id_events
                   WHERE users.id = ?
               """
            result = c.execute(query, (id,))

    return result.fetchall()


def insert_event(id_events, id_user, data, state, location, description, phone, mail):
    conn = get_conn()
    c = conn.cursor()
    query = """
           INSERT INTO reports (id_events, id_user, data, state, location, description, phone, mail)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
       """
    params = (id_events, id_user, data, state, location, description, phone, mail)
    c.execute(query, params)
    conn.commit()

    return c.rowcount


# zapytanie do zdarzeń
def all_event():
    conn = get_conn()
    c = conn.cursor()
    query = """
        SELECT * FROM events
    """
    result = c.execute(query)
    conn.commit()
    return result.fetchall()


def add_user(name, lastname, login, hashed_password, id_organization, is_admin):
    conn = get_conn()
    c = conn.cursor()
    query = """
        INSERT INTO users (name, lastname, login, password, id_organization, is_admin)
        VALUES (?, ?, ?, ?, ?, ?);
    """
    param = (name, lastname, login, hashed_password, id_organization, is_admin, )
    c.execute(query, param)
    conn.commit()
    return c.rowcount
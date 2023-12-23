import sqlite3


# połączenie z bazą
def get_conn():
    conn = sqlite3.connect('../database.sqlite')
    conn.execute('PRAGMA foreign_keys = ON')
    conn.row_factory = sqlite3.Row
    return conn


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


def update_event(data, location, description, phone, mail, id_events):
    conn = get_conn()
    c = conn.cursor()
    query = """
           UPDATE reports 
           SET data = ?, location = ?, description = ?, phone = ?, mail = ?
           WHERE id_reports = ?
       """
    params = (data, location, description, phone, mail, id_events)
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


def one_event(id_reports):
    conn = get_conn()
    c = conn.cursor()
    query = """
            SELECT * 
            FROM reports 
            INNER JOIN users 
            ON users.id = reports.id_user
            INNER JOIN events
            ON events.id_events = reports.id_events
            WHERE id_reports = ?
        """
    params = (id_reports, )
    result = c.execute(query, params)
    conn.commit()
    return result.fetchone()


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


def is_admin(id_user):
    conn = get_conn()
    c = conn.cursor()
    query = """
        SELECT is_admin
        FROM users
        WHERE id = ?
    """
    param = (id_user,)
    c.execute(query, param)
    conn.commit()
    return c.fetchone()


def change_state(state, id_reports):
    conn = get_conn()
    c = conn.cursor()
    query = """
           UPDATE reports 
           SET state = ?
           WHERE id_reports = ?
       """
    param = (state, id_reports, )
    c.execute(query, param)
    conn.commit()
    return c.rowcount
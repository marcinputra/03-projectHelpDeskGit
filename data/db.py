import sqlite3
# from datetime import date
from flask import Blueprint, request, redirect, session, url_for
from data.db_utils import insert_event
database_db = Blueprint('database_endpoints', __name__)


@database_db.route('/add_event', methods=['POST', 'GET'])
def add_event():
    if not session:
        return redirect(url_for('auth_endpoints.login'))
    id_events = request.form.get('id_events')
    id_user = session['user_id']
    data = '2023-12-12'
    state = 'Otwarte'
    location = request.form.get('location')
    description = request.form.get('description')
    phone = request.form.get('phone')
    mail = request.form.get('mail')
    try:
        insert_event(id_events, id_user, data, state, location, description, phone, mail)
    except sqlite3.IntegrityError:
        return "Bad Request insert", 400
    return redirect('/')
import sqlite3
import datetime
from flask import Blueprint, request, redirect, session, url_for
from data.db_utils import insert_event, update_event
database_db = Blueprint('database_endpoints', __name__)


@database_db.route('/add_event', methods=['POST', 'GET'])
def add_event():
    if not session:
        return redirect(url_for('auth_endpoints.login'))
    id_events = request.form.get('id_events')
    id_user = session['user_id']
    data = datetime.date.today()
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


@database_db.route('/update_event/<int:id_reports>', methods=['POST', 'GET'])
def update(id_reports):
    if not session:
        return redirect(url_for('auth_endpoints.login'))
    id_events = id_reports
    data = datetime.date.today()
    location = request.form.get('location')
    description = request.form.get('description')
    phone = request.form.get('phone')
    mail = request.form.get('mail')
    try:
        update_event(data, location, description, phone, mail, id_events)
    except sqlite3.IntegrityError:
        return "Bad Request insert", 400
    return redirect('/')
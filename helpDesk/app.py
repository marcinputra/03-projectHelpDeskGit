from flask import Flask, render_template, session, redirect, url_for
from forms.forms import forms_bp
from auth.auth import auth_db
from data.db_utils import get_all_events, one_event, is_admin, change_state
from data.db import database_db
import datetime

from config.config import Config

app = Flask(__name__, template_folder='./templates')
app.config.from_object(Config)

app.register_blueprint(forms_bp)
app.register_blueprint(auth_db, url_prefix='/auth')
app.register_blueprint(database_db)


@app.route('/')
def index():
    if not session:
        return redirect(url_for('auth_endpoints.login')) #info='Zalogowac sie musisz..'
    id = session['user_id']
    events = get_all_events(id)

    context = {
        'events': events
    }

    return render_template('index.html', **context)


@app.route('/details/<int:id_reports>')
def details(id_reports):
    if not session:
        return redirect(url_for('auth_endpoints.login')) #info='Zalogowac sie musisz..'
    # pobieranie danych z bazy
    id_reports = one_event(id_reports)

    timetoevent = datetime.date.today() - datetime.date.fromisoformat(id_reports['data'])

    context = {
        'id_reports': id_reports,
        'timetoevent': timetoevent.days,
    }

    return render_template('details.html', **context)


@app.route('/edit_event/<int:id_reports>')
def edit(id_reports):
    if not session:
        return redirect(url_for('auth_endpoints.login')) #info='Zalogowac sie musisz..'

    id_reports = one_event(id_reports)
    timetoevent = datetime.date.today() - datetime.date.fromisoformat(id_reports['data'])
    # id_user zalogowanego

    admin = is_admin(session['user_id'])
    context = {
        'id_reports': id_reports,
        'timetoevent': timetoevent.days,
        'is_admin': admin
    }
    return render_template('edit.html', **context)


@app.route('/update_event_close_open/<int:id_reports>', methods=['POST', 'GET'])
def update_event_close_open(id_reports):
    if not session:
        return redirect(url_for('auth_endpoints.login'))
    state = "Zamknięte"
    id_reports = id_reports
    change_state(state, id_reports)

    id = session['user_id']
    events = get_all_events(id)

    context = {
        'events': events
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

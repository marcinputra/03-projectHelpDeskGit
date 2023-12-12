from flask import render_template, Blueprint, session, redirect, url_for
from auth.auth import login_required
from data.db_utils import all_event

forms_bp = Blueprint('forms_endpoints', __name__, template_folder='../templates')


@forms_bp.route('/add_form')
@login_required
def add_form():
    if not session:
        return redirect(url_for('auth_endpoints.login')) #info='Zalogowac sie musisz'
    event = all_event()
    context = {
        'id_events': event,
        'event': event
    }
    return render_template('add.html', **context)
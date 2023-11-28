from functools import wraps
from flask import render_template, Blueprint, redirect, url_for, session, request, flash, get_flashed_messages, url_for

from data.db_utils import get_conn
# from werkzeug.security import check_password_hash

auth_db = Blueprint('auth_endpoints', __name__, template_folder='../templates')


def login_required(view):
    # do czego ten wraps
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session:
            return view(*args, **kwargs)
        else:
            return redirect(url_for('auth_endpoints.login'))

    return wrapped_view


@auth_db.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # info = request.args['info']
        message = get_flashed_messages()
        return render_template('login.html', message=message) # info=info

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        conn = get_conn()
        c = conn.cursor()
        result = c.execute('SELECT * FROM users WHERE login = ?', (login,))
        user_data = result.fetchone()
        if user_data:
            if password == user_data['password']:   # hashowanie hasła
                session['user_id'] = user_data['id']
                session['name'] = user_data['name']
                session['lastname'] = user_data['lastname']
                return redirect(url_for('index'))
        flash('Błędny login lub hasło.')
        return redirect(url_for('auth_endpoints.login'))


@auth_db.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth_endpoints.login'))

from flask import Blueprint, request, redirect, session, url_for

database_db = Blueprint('database_endpoints', __name__)

@database_db.route('/add_event', methods=['POST'])
def add_event():
    if not session:
        return redirect(url_for('auth_endpoints.login'))
    id = session['id']
    name = session['name']
    return redirect('/')
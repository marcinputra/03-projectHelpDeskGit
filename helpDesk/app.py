from flask import Flask, render_template, session, redirect, url_for
from forms.forms import forms_bp
from auth.auth import auth_db
from data.db_utils import get_all_events
from data.db import database_db

from config.config import Config

app = Flask(__name__, template_folder='./templates')
app.config.from_object(Config)

app.register_blueprint(forms_bp)
app.register_blueprint(auth_db, url_prefix='/auth')
app.register_blueprint(database_db)


@app.route('/')
def index():
    if not session:
        return redirect(url_for('auth_endpoints.login')) #info='Zalogowac sie musisz'
    id = session['user_id']
    events = get_all_events(id)

    context = {
        'events': events
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

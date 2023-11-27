from flask import Flask, render_template, session, redirect, url_for
from auth.auth import auth_db

from config.config import Config

app = Flask(__name__, template_folder='./templates')
app.config.from_object(Config)

# dlaczego dodajemy tu url_prefix ?
app.register_blueprint(auth_db, url_prefix='/auth')


@app.route('/')
def index():
    if not session:
        return redirect(url_for('auth_endpoints.login')) #info='Zalogowac sie musisz'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

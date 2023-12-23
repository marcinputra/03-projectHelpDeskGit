from flask import render_template, Blueprint

details_bp = Blueprint('details_endpoints', __name__, template_folder='../templates')
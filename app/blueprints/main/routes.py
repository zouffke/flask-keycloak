from flask import render_template

from app.blueprints.main import bp
from extensions import oidc


@bp.route('/')
@oidc.require_login
def home():
    return render_template('index.html')

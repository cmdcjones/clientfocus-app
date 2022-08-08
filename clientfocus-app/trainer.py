from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.exceptions import abort

bp = Blueprint('trainer', __name__)

mock_clients = ['Trish Regan', 'Peng Chen', 'Tori Jung', 'Hunter Ghobadi']

@bp.route('/')
def index():
    return render_template('trainer/index.html', clients=mock_clients)
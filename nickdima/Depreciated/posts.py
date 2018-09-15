import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from dbmysq import get_db

bp = Blueprint('posts', __name__, url_prefix='/posts')



# Just testing code
@bp.route('/test')
def test():
    return redirect(url_for('auth.login')) #bp_name.view_name == Endpoint
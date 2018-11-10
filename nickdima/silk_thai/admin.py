from flask import Blueprint, request, render_template, g, session, flash, redirect, url_for
from functools import wraps

bp = Blueprint('admin', __name__, url_prefix='/thai/admin', static_folder='static', template_folder='template')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        # check password credentials
        error = False
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'adminuser' and password == 'adminpass':
            session['admin_check'] = 'SECRET_CHANGE'
            return redirect(url_for('admin.manage'))
        else:
            return 'Your attempt has been logged'


    return render_template('admin/login.html')


def requires_login(view):

    @wraps(view)
    def wrapped(*args, **kwargs):

        #check if username / password are correct
        if session['admin_check'] != 'SECRET_CHANGE':
            print('Sorry, you are not an admin')
            session.clear()
            return redirect(url_for('homepage.home'))

        return view(*args, **kwargs)

    return wrapped

@bp.route('/logout', methods=['GET', 'POST'])
@requires_login
def logout():

    logged_out = False
    if request.method == 'POST':
        session.clear()
        logged_out = True

    return render_template('admin/logout.html', logged_out=logged_out)

@bp.route('/manage', methods=['GET', 'POST'])
@requires_login
def manage():

    return render_template('admin/manage.html')


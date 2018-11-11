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

        # TODO, COMPARE THIS TO ADMIN PASSWORD HASH IN DATABASE
        if username == 'adminuser' and password == 'adminpass':
            session['admin_check'] = 'SECRET_CHANGE'
            return redirect(url_for('admin.manage'))
        else:
            session.clear()
            return 'Your attempt has been logged'

    return render_template('admin/login.html')


def requires_login(view):

    @wraps(view)
    def wrapped(*args, **kwargs):

        try:
            if session['admin_check'] != 'SECRET_CHANGE':
                print('Sorry, you are not an admin')
                session.clear()
                return redirect(url_for('homepage.home'))
        except Exception as e:
            print(e)
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
        print('logged admin out')

    return render_template('admin/logout.html', logged_out=logged_out)

@bp.route('/manage', methods=['GET', 'POST'])
@requires_login
def manage():

    # Pass list of unavailable ingredients
    # Pass list of ingredients
    # Pass list of unavailable items
    # Pass list of available items

    return render_template('admin/manage.html')


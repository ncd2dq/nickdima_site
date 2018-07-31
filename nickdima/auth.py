import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request,
    session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from dbmysq import get_db
# Blueprint to group similar view functions / code used for those functions
# flash to store error messages avaiable in template / across request
# g to store data across requests
# render_template to render the jina templates
# request to check what method was used / any forms submitted in request
# session to access the cookie if needed (logged in user)
# url_for to generate the url for a specific blueprint/view function


# Give a name to the blueprint, provide this module location
# url_prefix will be prepended to all view routes in this bp
# /login -- /auth/login, /register --> /auth/register
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    '''Recieve login credentials, store user information in the session cookie, send to main page'''
    
    # Flow: get login information, pull from database based on username, validate login credentials
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect Username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect Password'

        if error is None:
            session.clear()
            session['user_id'] = user['id'] # Just store user id to query database later with
            return redirect(url_for('home.home_index'))
        else:
            flash(error) # store the error for access in the template

    return render_template('auth/login.html')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    '''
    Ensure no user with same username exists, put username/pass_hash in db.
    '''
    if request.method == 'POST':
        cur, con = get_db()
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is requried'

        else: 
            cur.execute(
                'SELECT * FROM users WHERE username = %s', (username,)
            )
            if cur.fetchone():
                error = 'Username taken, please choose another.'

        if error == None:
            cur.execute(
                'INSERT INTO users (username, password) VALUES (%s, %s)', (username, generate_password_hash(password))
            )
            con.commit()

            return redirect(url_for(('auth.login')))

        else:
            flash(error)

    return render_template('auth/register.html')


@bp.route('/logout', methods=('GET',))
def logout():
    if request.method == 'GET':
        g.user = None
        session.clear()

    return redirect(url_for('auth.login'))

def login_required(view):
    '''
    Makes a decorator that will run a function to check
    if a user is logged in before running a view function. Redirects
    to login page if not
    '''
    @functools.wraps(view) # This makes it look like the original function ran this code (in logging tools)
    def wrapped_view(**kwargs):
        '''Makes the decorator function'''
        if g.user is None:
            return redirect(url_for('auth.login')) #bp_name.view_func_name

        return view(**kwargs)

    # returns it so the original function is reasigned with decorator around it
    return wrapped_view


# runs this before ANY url request / view function (even in this blueprint or not)
@bp.before_app_request
def load_logged_in_user():
    '''
    Puts the user information in 'g', an object that is used
    to share data across requests
    '''
    user_id = session.get('user_id') # Session is a proxy that acts like a dictionary

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT id, username FROM users WHERE id = ?', (user_id,)
        ).fetchone()



# Just testing code
@bp.route('/test')
def test():
    return redirect(url_for('auth.register'))
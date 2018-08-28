import os
from flask import Flask, redirect, url_for

# Application factory "create_app" or "make_app"
def create_app(test_config=None):
    '''
    Create your application
    Load configuration files
    Import / register blueprints
    Register your database
    '''

    # Configuration loaded from instance/ directory when set to true
    app = Flask(__name__, instance_relative_config=True)

    # Secret_key is used to sign cookies so session info can't be modified
    # use a random_number for deployment
    # Database is the path to your database (in the instance folder here)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        #DATABASE = os.path.join(app.instance_path, 'nickdb.sqlite')
        MYSQL_HOST = 'sql9.freemysqlhosting.net',
        MYSQL_USER = 'sql9249883',
        MYSQL_PASSWORD = 'xwzfPYlGVy',
        MYSQL_DB = 'sql9249883',
        MYSQL_CURSORCLASS = 'DictCursor'
    )
    #nicholas.dima1@gmail.com
    #VyK^gPRirq*Q)&TV

    # Use configuration from config.py unless a testing config is supplied
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # If instance folder doesn't exist, make it
    # Will usually make it one directory above __init__.py so that it is not
    # available to clients
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Create a simple test routes / easter eggs
    @app.route('/hello')
    def hello():
        return "You should not be here.<br><br>How did you find this, please leave immediately."

    @app.route('/hayley')
    def hayley():
        return "Hi my darling <3"

    @app.route('/imupset')
    def upset():
        return "Ligma"

    # Register Database for teardown context / CLI command
    # Local import (checks within package first to avoid using wrong lib)
    import dbmysq
    dbmysq.init_it(app)

    #import dbmysq 
    #dbmysq.init_app(app)

    # Reguster blueprints
    import auth
    app.register_blueprint(auth.bp)

    import posts
    app.register_blueprint(posts.bp)

    import home
    app.register_blueprint(home.bp)

    @app.route('/')
    def home():
        return url_for('home.home_index')

    import lunchbreak
    app.register_blueprint(lunchbreak.bp)

    #import thai restauraunt stuff

    import silk_thai.checkout
    app.register_blueprint(silk_thai.checkout.bp)
    
    import silk_thai.homepage
    app.register_blueprint(silk_thai.homepage.bp)

    import silk_thai.menu
    app.register_blueprint(silk_thai.menu.bp)

    return app
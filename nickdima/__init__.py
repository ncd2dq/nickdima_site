import os
from flask import Flask, redirect, url_for
import eventlet
eventlet.monkey_patch()
#CAUSES PROBLEM
#from flask_socketio import SocketIO

#New
from flask_heroku import Heroku

#REALLY 
from test_pong.pong_db import get_db, restart_db, get_ball
#import test_pong.pong #socketio events
from nickdima.socker import socker

#CAUSES PROBLEM
#socker = SocketIO()

#from test_pong import pong
#pong_thread = False



# Application factory "create_app" or "make_app"
def create_app(test_config=None):
    #socker = SocketIO()
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
    #import dbmysq
    #dbmysq.init_it(app)

    #import dbmysq 
    #dbmysq.init_app(app)

    # Reguster blueprints
    import auth
    app.register_blueprint(auth.bp)

    import posts
    app.register_blueprint(posts.bp)

    import home.home
    app.register_blueprint(home.home.bp)

    @app.route('/')
    def home():
        return redirect(url_for('home.home_index'))

    import lunchbreak.lunchbreak
    app.register_blueprint(lunchbreak.lunchbreak.bp)

    #import thai restauraunt stuff

    import silk_thai.checkout
    app.register_blueprint(silk_thai.checkout.bp)
    
    import silk_thai.homepage
    app.register_blueprint(silk_thai.homepage.bp)

    import silk_thai.menu
    app.register_blueprint(silk_thai.menu.bp)

    socker.init_app(app)

    import test_pong.pong 
    app.register_blueprint(test_pong.pong.bp)  #test_pong.pong.bp)

    #CAUSES PROBLEM
    #socker.init_app(app)


    '''
    #@socker.on('connect')
    #def handle_con():
    #    print('connected server')
    #    socker.emit('testing', {'data': 'hi'})

    #
    # FOR SOME REASON I NEED ALL SOCKET EVENTS HERE
    #
    @socker.on('connect')
    def handle_connect():
        print('THE HANDLE CONNECT FUNCTION WAS WRITTEN')
        socker.emit('testing', {'hello': 'hi'})

    #UGLY THREADING CODE
    def run_pong_inner():
        ball = get_ball()
        db = get_db()
        #determine if ball hits walls of space
        if ball['y'] > 400 or ball['y'] < 0:
            ball['y_s'] *= - 1

        if ball['x'] > 400:
            ball['x'] = 200
            ball['y'] = 200
            ball['player_1_score'] += 1

        if ball['x'] < 0:
            ball['x'] = 200
            ball['y'] = 200
            ball['player_2_score'] += 1
            #ball['x_s'] *= -1

        #determine if ball hits paddles
        key_list = db.keys()

        for key in key_list:
            if key != 'count' and key != 'player_1_score' and key != 'player_2_score':
                cur_paddle = db[key]
                x = cur_paddle['x']
                y = cur_paddle['y']
                if ball['x'] > x and ball['x'] < x + 15:
                    if ball['y'] > y and ball['y'] < y + 50:
                        ball['x_s'] *= -1

        ball['x'] += ball['x_s']
        ball['y'] += ball['y_s']

        socker.emit('recieve_ball_loc', ball)

    def run_pong():
        while True:
            run_pong_inner()
            eventlet.sleep(0.04)
    #UGLY THREADING CODE#


    @socker.on('player_connect')
    def handle_player_connect(data):
        global pong_thread

        print('received player_connect event')
        data_base = get_db()
        if data_base['count'] == 0:
            data_base[data['id']] = {'player_number': 1}
            data_base[data['id']]['x'] = 10
            data_base[data['id']]['y'] = 50
            data_base['count'] += 1
            socker.emit('what_player', {'id': data['id'], 'player_number': data_base['count']})
        elif data_base['count'] == 1:
            data_base[data['id']] = {'player_number': 2}
            data_base[data['id']]['x'] = 375
            data_base[data['id']]['y'] = 50
            data_base['count'] += 1
            socker.emit('what_player', {'id': data['id'], 'player_number': data_base['count']})

            #all players connected
            print('SENDING ALL PLAYERS CONNECTED SIGNAL')
            socker.emit('all_players', data_base)

            pong_thread = eventlet.spawn(run_pong) #how to end?

    @socker.on('move_request')
    def handle_move_request(data):
        data_base = get_db()
        data_base[data['id']]['y'] += data['y']

        socker.emit('all_info', data_base)

    @socker.on('disconnect')
    def handle_disconnect():
        restart_db()
        global pong_thread
        #tell all clients to SCRAM!
        socker.emit('scram', {'get': 'the fuck out'})

        pong_thread.kill()


    @socker.on('send_chat')
    def handle_chatting(data):
        socker.emit('recv_chat', data)

    @socker.on('send_ball_loc')
    def handle_being_sent(ball_loc):
        socker.emit('recieve_ball_loc', ball_loc)

    #
    # END OF ALL SOCKET EVENTS FOR SOME REASON
    #
    '''

    #new c
    heroku = Heroku(app)

    return app

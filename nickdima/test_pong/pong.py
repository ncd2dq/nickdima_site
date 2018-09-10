from flask import Blueprint, render_template
from test_pong.pong_db import get_db, restart_db, get_ball, get_rally_count, reset_rally_count
import sys
from nickdima.socker import socker
import eventlet
eventlet.monkey_patch()



bp = Blueprint('test_pong', __name__, url_prefix='/test_pong', static_folder='static', template_folder='template')

pong_thread = False

@bp.route('/test_pong_game')
def test_pong_game():

    print('hello logs')

    return render_template('indexpong.html')


#
# EVENT HANDLERS
#

#reset server comment


@socker.on('connect')
def handle_connect():
    print('THE HANDLE CONNECT FUNCTION WAS WRITTEN')
    socker.emit('testing', {'hello': 'hi'})

#UGLY THREADING CODE
def run_pong_inner():
    ball = get_ball()
    db = get_db()
    rally = get_rally_count()

    rally['count'] += 1

    #determine if ball hits walls of space
    if ball['y'] > 400 or ball['y'] < 0:
        ball['y_s'] *= - 1

    if ball['x'] > 400:
        ball['x'] = 200
        ball['y'] = 200
        ball['player_1_score'] += 1
        reset_rally_count()

    if ball['x'] < 0:
        ball['x'] = 200
        ball['y'] = 200
        ball['player_2_score'] += 1
        reset_rally_count()

    #make ball speed faster if rally has been continuing
    if rally['count'] % 100 == 0:
        ball['x_s'] *= 1.1
        ball['y_s'] *= 1.1
        socket.emit('testing', {'data': 'ball faster'})

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
#UGLY THREADING CODE


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
from flask import Blueprint, render_template
from flask_socketio import send, emit
from test_pong.pong_db import get_db
from . import socketio


bp = Blueprint('test_pong', __name__, url_prefix='/test_pong', static_folder='static', template_folder='template')


@bp.route('/test_pong_game')
def test_pong_game():

    return render_template('index.html')

#data_base: {'id': {'x': 10, 'y': 50}, 'id2': {'x': 390, 'y': 50}}
@socketio.on('connect')
def handle_connect():
    print('Player connected')

@socketio.on('player_connect')
def handle_player_connect(data):
    print('received player_connect event')
    data_base = get_db()
    if data_base['count'] == 0:
        data_base[data['id']] = {'player_number': 1}
        data_base[data['id']]['x'] = 10
        data_base[data['id']]['y'] = 50
        data_base['count'] += 1
        socketio.emit('what_player', {'id': data['id'], 'player_number': data_base['count']})
    elif data_base['count'] == 1:
        data_base[data['id']] = {'player_number': 2}
        data_base[data['id']]['x'] = 375
        data_base[data['id']]['y'] = 50
        data_base['count'] += 1
        socketio.emit('what_player', {'id': data['id'], 'player_number': data_base['count']})

        #all players connected
        print('SENDING ALL PLAYERS CONNECTED SIGNAL')
        socketio.emit('all_players', data_base)

@socketio.on('move_request')
def handle_move_request(data):
    data_base = get_db()
    data_base[data['id']]['y'] += data['y']

    socketio.emit('all_info', data_base)

@socketio.on('message')
def handle_message(message):
    print('recieved: {}'.format(message))

    send('This is from flask:' + message)


@socketio.on('increment')
def handle_increment(data):
    data_base = get_db()
    data_base['x_1'] += data['value']
    print(data_base)
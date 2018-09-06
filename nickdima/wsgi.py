import sys
sys.path.insert(0, "/app/nickdima")


from __init__ import create_app, socker

app = create_app()



'''
JUST THIS SOMEHOW WORKS

import sys
sys.path.insert(0, "/app/nickdima")
import os
from flask import Flask, redirect, url_for
import eventlet
eventlet.monkey_patch()
#CAUSES PROBLEM
from flask_socketio import SocketIO

#CAUSES PROBLEM
socker = SocketIO()

#New
from flask_heroku import Heroku



code =  <script>
    let your_sock = io.connect('http://' + document.domain + ':' + location.port + '/');
    your_sock.on('connect', function(){
        console.log('I have connected with ID ' + '9');
    });

    your_sock.on('testing', function(data){
        console.log(data);
        console.log('here');
    });</script>

def create_app():
    app = Flask(__name__)

    socker.init_app(app)
    heroku = Heroku(app)

    @app.route('/home')
    def home():
        print('HELLO HEROKU LOGS')
        return '<!Doctype html><html><head><script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script></head><body>'+ code + '</body></html>'

    @socker.on('connect')
    def handle_connect():
        print('PLAYER HAS CONNECTED')

        socker.emit('testing', {'data': 'hi'})

        print('TRIED TO EMIT')

    return app

app = create_app()

'''
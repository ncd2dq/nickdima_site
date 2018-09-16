from nickdima.socker import socker
from stay_alive.main_logic import run_survivor
import eventlet
eventlet.monkey_patch()

survivor_thread = None

@socker.on('connect', namespace='/stay_alive')
def handle_connect():
    print('Connected to stay_alive')
    socker.emit('con_test', {'stay alive': 'from stay alive'}, namespace='/stay_alive')

    survivor_thread = eventlet.spawn(run_survivor)


@socker.on('disconnect', namespace='/stay_alive')
def handle_disconnect():

    survivor_thread.kill()
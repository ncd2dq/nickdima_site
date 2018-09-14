from nickdima.socker import socker
from stay_alive import run_survivor

@socker.on('connect', namespace='/stay_alive')
def handle_connect():
    print('Connected to stay_alive')
    socker.emit('con_test', {'stay alive': 'complete'})
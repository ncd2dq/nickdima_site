from nickdima.socker import socker
from stay_alive.stay_alive_db import get_db
from stay_alive.main_logic import run_survivor
import eventlet
import random
eventlet.monkey_patch()

survivor_thread = None

def get_hero_ids():
    db = get_db()
    hero_ids = []

    for hero in db['heros']:
        hero_ids.append(hero['id'])

    return hero_ids


@socker.on('connect', namespace='/stay_alive')
def handle_connect():

    # Each connected player gets a new hero
    existing_ids = get_hero_ids()
    attempt_id = 1
    while attempt_id in existing_ids:
        attempt_id += 1
    new_hero = Hero(attempt_id, db['map'])
    db['heros'].append(new_hero)


    # Start the game thread only when the first player joins
    if len(existing_ids == 1):
        survivor_thread = eventlet.spawn(run_survivor)

    socker.emit('your_hero_id', {'your_hero_id':attempt_id}, namespace='/stay_alive')


@socker.on('disconnect', namespace='/stay_alive')
def handle_disconnect():

    survivor_thread.kill()
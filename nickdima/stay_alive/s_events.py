from nickdima.socker import socker
from stay_alive.stay_alive_db import get_db, reset_db
from stay_alive.main_logic import run_survivor
from stay_alive.heros import Hero
import eventlet
import random
eventlet.monkey_patch()

survivor_thread = None

def get_hero_ids():
    db = get_db()
    hero_ids = []

    for hero in db['heros']:
        hero_export = hero.export()
        hero_ids.append(hero_export['id'])

    return hero_ids


@socker.on('connect', namespace='/stay_alive')
def handle_connect():
    global survivor_thread
    db = get_db()
    # Start the game thread only when the first player joins
    if db['total_players'] == 0:
        survivor_thread = eventlet.spawn(run_survivor)

    # Each connected player gets a new hero
    existing_ids = get_hero_ids()
    attempt_id = 1
    while attempt_id in existing_ids:
        attempt_id += 1
    new_hero = Hero(attempt_id, db['map'])
    db['heros'].append(new_hero)


    socker.emit('your_hero_id', {'your_hero_id':attempt_id}, namespace='/stay_alive')
    db['total_players'] += 1

@socker.on('move_req', namespace='/stay_alive')
def handle_mov_req(data):
    db = get_db()
    cur_hero = None

    # Retrieve the hero that made the request
    for hero in db['heros']:
        if hero['id'] == data['id']:
            cur_hero = hero
            break

    cur_hero.dir = [data['dir'], data['type']]


@socker.on('disconnect', namespace='/stay_alive')
def handle_disconnect():
    global survivor_thread
    db = get_db()
    print(db, 'pre reset')
    survivor_thread.kill()
    reset_db()


    db = get_db()
    print(db, 'post reset')
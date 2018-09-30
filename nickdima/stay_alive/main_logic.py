from stay_alive.stay_alive_db import get_db
from nickdima.socker import socker

from stay_alive.resource_nodes import ResourceNode
from stay_alive.daylight import DayLight
import eventlet
import random
eventlet.monkey_patch()
'''
#
#Below is a reference of the master game database
#

'projectiles' : 
[ {type' : 'bullet', 'location' : (x, y), 'dmg' : 5} ],

'monsters' : 
[ {'obj_name': 'bomber', 'location': (x, y), 'hp': 10} ],

'resource_nodes' : 
[ {'type': 'wood', 'amount': 5, 'location': (x, y), ''}],

'heros' : 
[ {'id' : 1, 
'inventory' : {'water' : 10, 'wood' : 5, 'brick': 5, 'steal' : 5, 'tool' : 'wood', 'gun' : 'steal', 
                'ammo' : 10},
'state' : 'inside', 
'location' : (x, y), 
'equiped' : {'class' : gun/tool, 'type': 'steal'},
'building' : {'class' : 'wall/gun/tool', 'type': steal}} ]

'structures' : 
[{'type' : 'wall/door/turret', 'location' : (x, y), 'hp' : 50, 'state' : 'open/closed'}],

'daylight' :
{'current' : 10, 'max' : 2800, 'water_cost' : 5, 'ticks' : 7},

'map' :
{'max_x' : 800, 'max_y' : 800, 
'events' :
    {'type' : 'earthquake/firestorm/acidraid', 'current' : 150, 'max' : 600, 'dmg' : 5}
}

#
#All objects additionally have a 'hitbox' : {'x_len' : 5, 'y_len' : 10}
#

'''

def game_loop():

    db = get_db()

    #
    # Client input layer ---------------------------------------
    #


    #
    # Process if inputs are valid ------------------------------
    #


    #
    # Do game logic --------------------------------------------
    #
    for hero in db['heros']:
        hero.update()

    db['daylight'].progress()


    # Remove depleated resources
    for resource_node in db['resource_nodes']:
        if resource_node.amount == 0:
            db['resource_nodes'].remove(resource_node)
    # 10% chance of a new resource node as long as there are less than 15 on the map
    if random.random() < 0.1 and len(db['resource_nodes']) < 15:
        db['resource_nodes'].append(
            ResourceNode(random.choice(list(ResourceNode.color_dict.keys())), db['map'])
            )


    #
    # Extraction Layer ----------------------------------------
    #
    # Get all data that needs to be sent to clients
    heros_data = []
    for hero in db['heros']:
        heros_data.append(hero.export())

    daylight_data = db['daylight'].export()

    resource_nodes_data = []
    for resource_node in db['resource_nodes']:
        resource_nodes_data.append(resource_node.export())

    #
    # Replication layer ---------------------------------------
    #
    # Send all data to clients
    # TO DO only send data to players if that object is within 400 distance units from them
    socker.emit('hero_data', {'hero_data': heros_data}, namespace='/stay_alive')
    socker.emit('daylight_data', {'daylight_data': daylight_data}, namespace='/stay_alive')
    socker.emit('resource_nodes_data', {'resource_nodes_data': resource_nodes_data}, namespace='/stay_alive')


def run_survivor():
    db = get_db()
    db['daylight'] = DayLight(2800, 5, 7, get_db)

    while True:
        game_loop()
        eventlet.sleep(0.04)
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

db = {}

def get_db():
    global db
    return db

def reset_db():
    global db
    db = {}
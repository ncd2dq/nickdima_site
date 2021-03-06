'''
#
#Below is a reference of the master game database in how it should be sent over sockets
#Each dictionary below will actually be a CLASS in the python-server-held dictionary, but the export method of each should
#produce the dictionary shown below
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
'alive' : True/False,
'location' : (x, y), 
'equiped' : {'class' : gun/tool, 'type': 'steal'},
'building' : {'class' : 'wall/gun/tool', 'type': steal}},
'dir' : ['up/down': True/False, 'left/right': True/False] # THIS IS NOT EXPORTED

'structures' : 
[{'type' : 'wall/door/turret', 'location' : (x, y), 'hp' : 50, 'state' : 'open/closed', 'rotation' : '0/90'}],

'daylight' :
{'current' : 10, 'maxi' : 2800, 'water_cost' : 5, 'ticks' : 7},

#Max_x/Max_y should be pixel dimensions of background image
'map' :
{'max_x' : 800, 'max_y' : 800, 
'events' :
    {'type' : 'earthquake/firestorm/acidraid', 'current' : 150, 'max' : 600, 'dmg' : 5}
}

#
#All objects additionally have a 'hitbox' : {'x_len' : 5, 'y_len' : 10}
#

'''

db = {'total_players' : 0, 'map': {'max_x' : 1955, 'max_y' : 1955}, 'heros': [], 'structures': [],
        'daylight':{'current':0, 'maxi': 2800, 'water_cost': 5, 'ticks': 7}, 'resource_nodes': []}

def get_db():
    global db
    return db

def reset_db():
    global db
    db = {'total_players' : 0, 'map': {'max_x' : 1955, 'max_y' : 1955}, 'heros': [], 'structures': [],
        'daylight':{'current':0, 'maxi': 2800, 'water_cost': 5, 'ticks': 7}, 'resource_nodes': []}
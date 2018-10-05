'''
'heros' : 
[ {'id' : 1, 
'inventory' : {'water' : 10, 'wood' : 5, 'brick': 5, 'steal' : 5, 'tool' : 'wood', 'gun' : 'steal', 
                'ammo' : 10},
'state' : 'inside', 
'alive' : True/False,
'location' : (x, y), 
'equiped' : {'class' : gun/tool, 'type': 'steal'},
'building' : {'class' : 'wall/gun/tool', 'type': steal}} ]
'dir' : ['up/down': True/False, 'left/right': True/False] # THIS IS NOT EXPORTED
'''
import random
import copy
import math
from stay_alive.stay_alive_db import get_db

class Hero(object):
    def __init__(self, id, map):
        self.id = id # Unique player id
        self.inventory = self._create_inventory()
        self.state = 'outside' #Inside/Outside
        self.location = self._create_location(map) #[X, Y]
        self.equipped = None
        self.building = None
        self.hitbox = {'x_len' : 10, 'y_len' : 10}
        self.dir = ['up', False, 'right', False] # Up/Down, Right/Left and if actively moving

        self.map = map

        self.alive = True

        self.move_speed = 8

    def _create_inventory(self):
        '''Water is your main survival resource'''
        initial_inventory = {'water' : 25, 'wood' : 0, 'brick' : 0, 'steal' : 0, 'tool': None, 'gun' : None, 'ammo' : None}
        return initial_inventory

    def _create_location(self, map):
        '''Any random location within the middle-ish area of the map'''
        initial_location = [random.random() * (map['max_x'] / 2) + (map['max_x'] / 3), 
                            random.random() * (map['max_y'] / 2) + (map['max_y'] / 3)]
        return initial_location

    def _detect_map_edge_collide(self, dir):
        '''
        This method is made to run with the move method to check if a 
        character is walking off the map
        '''

        # Check Top Left Point
        if dir == 'up':
            if self.location[1] - self.move_speed < 0:
                return True

        # Check Bottom Left Point
        elif dir == 'down':
            if self.location[1] + self.hitbox['y_len'] + self.move_speed > self.map['max_y']:
                return True

        # Check Top Right Point
        elif dir == 'right':
            if self.location[0] + self.hitbox['x_len'] + self.move_speed > self.map['max_x']:
                return True

        # Check Bottom Left Point
        elif dir == 'left':
            if self.location[0] - self.move_speed < 0:
                return True

        return False

    def _detect_all_collisions(self, dir, coll_type, get_structs):
        '''
        Params:
        get_structs should be a function that can return a nested dictionary
        coll_type is the column within that nested dictionary that returns a list of objects with locations/hitboxes

        #TO DO:
        could improve this by first determining which objects are near before edge checking
        '''
        structures = get_structs()[coll_type]
        if dir == 'up':
            for structure in structures:
                # Just need to check one of the top y points vs structure y range
                if ( 
                    # Is the new y location of the TOP LEFT point in between the y ranges
                    (self.location[1] - self.move_speed < structure['location'][1] + structure['hitbox']['y_len'] 
                    and self.location[1] - self.move_speed > structure['location'][1]) 
                ):
                    # Check the x condition of the top 2 points vs structure x range
                    if ( 
                        # Is the x location of the LEFT points in between the x ranges
                        (self.location[0] > structure['location'][0] 
                        and self.location[0] < structure['location'][0] + structure['hitbox']['x_len']) 
                    or 
                        # Is the x location of the RIGHT points in between the x ranges
                        (self.location[0] + self.hitbox['x_len'] > structure['location'][0]
                        and self.location[0] + self.hitbox['x_len'] < structure['location'][0] + structure['hitbox']['x_len'] ) 
                    ):
                        
                        if structure['state'] == 'closed':
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

        elif dir == 'down':
            for structure in structures:
                # Just need to check one of the bottom y points vs structure y range
                if ( 
                    # Is the new y location of the TOP LEFT point in between the y ranges
                    (self.location[1] + self.hitbox['y_len'] + self.move_speed < structure['location'][1] + structure['hitbox']['y_len'] 
                    and self.location[1] + self.hitbox['y_len'] + self.move_speed > structure['location'][1]) 
                ):
                    # Check the x condition of the top 2 points vs structure x range
                    if ( 
                        # Is the x location of the LEFT points in between the x ranges
                        (self.location[0] > structure['location'][0] 
                        and self.location[0] < structure['location'][0] + structure['hitbox']['x_len']) 
                    or 
                        # Is the x location of the RIGHT points in between the x ranges
                        (self.location[0] + self.hitbox['x_len'] > structure['location'][0]
                        and self.location[0] + self.hitbox['x_len'] < structure['location'][0] + structure['hitbox']['x_len'] ) 
                    ):
                        
                        if structure['state'] == 'closed':
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

        elif dir == 'left':
            for structure in structures:
                # Just need to check one of the left x points vs structure x range
                if ( 
                    # Is the new x location of the LEFT points in between the x ranges
                    (self.location[0] - self.move_speed < structure['location'][0] + structure['hitbox']['x_len'] 
                    and self.location[0] - self.move_speed > structure['location'][0]) 
                ):
                    # Check the y condition of the left 2 points vs structure y range
                    if ( 
                        # Is the y location of the TOP points in between the y ranges
                        (self.location[1] > structure['location'][1] 
                        and self.location[1] < structure['location'][1] + structure['hitbox']['y_len']) 
                    or 
                        # Is the y location of the BOTTOM points in between the y ranges
                        (self.location[1] + self.hitbox['y_len'] > structure['location'][1]
                        and self.location[1] + self.hitbox['y_len'] < structure['location'][1] + structure['hitbox']['y_len'] ) 
                    ):
                        
                        if structure['state'] == 'closed':
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

        elif dir == 'right':
            for structure in structures:
                # Just need to check one of the right x points vs structure x range
                if ( 
                    # Is the new x location of the RIGHT points in between the x ranges
                    (self.location[0] + self.hitbox['x_len'] + self.move_speed < structure['location'][0] + structure['hitbox']['x_len'] 
                    and self.location[0] + self.hitbox['y_len'] + self.move_speed > structure['location'][0]) 
                ):
                    # Check the y condition of the left 2 points vs structure y range
                    if ( 
                        # Is the y location of the TOP points in between the y ranges
                        (self.location[1] > structure['location'][1] 
                        and self.location[1] < structure['location'][1] + structure['hitbox']['y_len']) 
                    or 
                        # Is the y location of the BOTTOM points in between the y ranges
                        (self.location[1] + self.hitbox['y_len'] > structure['location'][1]
                        and self.location[1] + self.hitbox['y_len'] < structure['location'][1] + structure['hitbox']['y_len'] ) 
                    ):
                        
                        if structure['state'] == 'closed':
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
                    
        # No collisions detected
        return False


    def move(self, dir, get_structs, coll_type='structures'):
        if dir == 'up':
            if not self._detect_all_collisions(dir, coll_type, get_structs) and not self._detect_map_edge_collide(dir):
                self.location[1] -= self.move_speed

        elif dir == 'down':
            if not self._detect_all_collisions(dir, coll_type, get_structs) and not self._detect_map_edge_collide(dir):
                self.location[1] += self.move_speed

        elif dir == 'left':
            if not self._detect_all_collisions(dir, coll_type, get_structs) and not self._detect_map_edge_collide(dir):
                self.location[0] -= self.move_speed

        elif dir == 'right':
            if not self._detect_all_collisions(dir, coll_type, get_structs) and not self._detect_map_edge_collide(dir):
                self.location[0] += self.move_speed

    def update(self):
        if self.dir[1] == True:
            self.move(self.dir[0], get_db)
        if self.dir[3] == True:
            self.move(self.dir[2], get_db)

    def _distance_from(self, center1, center2):

        dist = math.sqrt( ( ((center2[0] - center1[0]) ** 2) + ((center2[1] - center1[1]) ** 2) ) )

        return dist

    def action_key(self):
        # First up, attempt to collect resources
        db = get_db()

        hero_center = [self.location[0] + (self.hitbox['x_len'] / 2), self.location[1] + (self.hitbox['y_len'] / 2)]

        # collect a resource by having your center be close enough to the center of the circular resource node
        for resource in db['resource_nodes']:
            resc_center = [resource.location[0] + (resource.hitbox['x_len'] / 2), resource.location[1] + (resource.hitbox['y_len'] / 2)]
            if self._distance_from(resc_center, hero_center) <= resource.hitbox['x_len']:
                if resource.be_consumed():
                    self.inventory[resource.type] += 3




    def export(self, data='all'):
        '''Turn all your attributes into a dictionary to be sent to the client'''
        export_dict = {}

        if data == 'all':
            export_dict['id'] = self.id
            export_dict['inventory'] = copy.deepcopy(self.inventory)
            export_dict['state'] = self.state
            export_dict['location'] = copy.deepcopy(self.location)
            export_dict['equpied'] = copy.deepcopy(self.equipped)
            export_dict['building'] = copy.deepcopy(self.building)
            export_dict['hitbox'] = copy.deepcopy(self.hitbox)
            export_dict['alive'] = self.alive

        return export_dict


if __name__ == '__main__':
    map = {'max_x' : 500, 'max_y' : 600}
    h1 = Hero(1, map)

    test_obj = {'state' : 'closed', 'location' : [0, 0], 'hitbox' : {'x_len' : 10, 'y_len' : 10}}
    test_obj2 = {'state' : 'open', 'location' : [50, 50], 'hitbox' : {'x_len' : 50, 'y_len' : 50}}
    test_db = {'structures' : [test_obj, test_obj2]}

    def get_test_db():
        return test_db
    print(h1.location)
    h1.location[0] = 0
    h1.location[1] = 15
    print(h1.location)
    h1.move('up', get_test_db)
    print(h1.location)

    print(h1.export())

    print(h1._distance_from([1, 0], [1, 1]))
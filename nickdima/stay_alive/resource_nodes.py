'''
'resource_nodes' : 
[ {'type': 'wood', 'amount': 5, 'location': (x, y), ''}]
'''

class ResourceNode(object):

    color_dict = {'water' : 'blue', 'wood' : 'brown', 'brick': 'red', 'steal' : 'grey'}

    def __init__(self, type, map):
        self.type = type
        self.amount = 10
        self.hitbox = {'x_len' : 50, 'y_len' : 50}
        self.location = _create_location(map)
        self.color = ResourceNode.color_dict[self.type]

        self.max_cooldown = 100 
        self.cool_down = 0


    def _create_location(self, map):
        '''Any random location within the middle-ish area of the map'''
        initial_location = [random.random() * map['max_x'], 
                            random.random() * map['max_y']]

        return initial_location

    def be_consumed(self):
        if self.cool_down == 0:
            self.amount -= 1
            self.cool_down = self.max_cooldown
            self.hitbox['x_len'] -= 2
            self.hitbox['y_len'] -= 2   
               
            return True

        else:
            return False

    def update(self):
        if self.cool_down != 0:
            self.cool_down -= 1


    def export(self):
        export_dict = {}

        export_dict['type'] = self.type
        export_dict['amount'] = self.amount
        export_dict['location'] = self.location
        export_dict['color'] = self.color
        export_dict['hitbox'] = self.hitbox

        return export_dict
'''
'structures' : 
[{'type' : 'wall/door/turret', 'location' : (x, y), 'hp' : 50, 'state' : 'open/closed', 'rotation' : '0/90'}],
'''

class Wall(object):
    def __init__(self, location, rotation):

        self.location = location
        self.rotation = rotation
        if rotation == 0:
            self.hitbox = {'x_len' : 40, 'y_len' : 20}
        elif rotation == 90:
            self.hitbox = {'x_len' : 20, 'y_len' : 40}
        self.state = 'closed'
        self.hp = 50

    def export(self):
        export_dict = {}

        export_dict['type'] = 'wall'
        export_dict['location'] = self.location
        export_dict['hp'] = self.hp
        export_dict['state'] = 'closed'
        export_dict['rotation'] = self.rotation

        return export_dict
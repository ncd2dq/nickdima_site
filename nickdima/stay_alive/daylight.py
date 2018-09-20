'''
'daylight' :
{'current' : 10, 'maxi' : 2800, 'water_cost' : 5, 'ticks' : 7},
'''


class DayLight(object):
    def __init__(self, maxi, water_cost, ticks, get_db):
        self.current = 0
        self.maxi = maxi
        self.water_cost = water_cost
        self.ticks = ticks
        self.get_db = get_db

    def collect_water_tax(self):
        '''At each tick mark, charge each player for water'''
        db = self.get_db()
        heros = db['heros']

        for hero in heros:
            water_left = hero.inventory['water'] - self.water_cost

            # If the hero does not have enough water, they are now dead
            if water_left < 0:
                hero.alive = False
            else:
                hero.inventory['water'] = water_left

    def progress(self):
        self.current += 1

        tick_mark = self.maxi / self.ticks

        if self.current > self.maxi:
            self.current = 0
            self.collect_water_tax()
        elif self.current % tick_mark == 0:
            self.collect_water_tax()


    def export(self):
        export_dict = {}

        export_dict['current'] = self.current
        export_dict['maxi'] = self.maxi
        export_dict['water_cost'] = self.water_cost
        export_dict['ticks'] = self.ticks
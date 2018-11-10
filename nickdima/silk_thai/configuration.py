# Monday = 0, Sunday = 6
# Hour in range(24)

web_configuration = {
    'delivery_time_minutes' : 60,
    'takeout_time_minutes' : 15,
    'delivery_minimum_cents' : 2000,
    'accepting_takeout' : False,
    'accepting_delivery' : False,
    'hours_of_operation' : {
                                0: (11, 21, 30), 
                                1: (11, 21, 30), 
                                2: (11, 21, 30), 
                                3: (11, 21, 30), 
                                4: (11, 22, 30), 
                                5: (11, 22, 30), 
                                6: (11, 21, 30)
                            },
    'lunch_hours' : {
                        0: (11, 13), 
                        1: (11, 13), 
                        2: (11, 13), 
                        3: (11, 13), 
                        4: (11, 13),  
                        5: False, 
                        6: False
                    }
}
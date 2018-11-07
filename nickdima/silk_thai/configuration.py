# Monday = 0, Sunday = 6
# Hour in range(24)

web_configuration = {
    'delivery_time_minutes' : 60,
    'takeout_time_minutes' : 15,
    'hours_of_operation' : {
                                0: (11, 9, 30), 
                                1: (11, 9, 30), 
                                2: (11, 9, 30), 
                                3: (11, 9, 30), 
                                4: (11, 10, 30), 
                                5: (11, 10, 30), 
                                6: (11, 9, 30)
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
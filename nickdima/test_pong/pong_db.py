db = {'count': 0}
ball_location = {'x': 200, 'y': 200, 'x_s': 5, 'y_s': 5}

def get_db():
    global db
    
    return db

def get_ball():
    global ball_location

    return ball_location

def restart_db():
    global db 
    
    db = {'count': 0}
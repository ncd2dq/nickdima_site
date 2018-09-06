db = {'count': 0}

def get_db():
    global db
    
    return db

def restart_db():
    global db 
    
    db = {'count': 0}
db = {'count': 0}
ball_location = {'x': 200, 'y': 200, 'x_s': 5, 'y_s': 5, 'player_1_score': 0, 'player_2_score': 0}
rally = {'count': 0}

#Every rally win, a player gets increased paddle size. It resets at first loss
paddle_stats = {
'p1': {'xsize': 15, 'ysize': 50, 'rally_wins': 0}, 
'p2': {'xsize': 15, 'ysize': 50, 'rally_wins': 0}, 
'defaults': {'xsize': 15, 'ysize': 50, 'rally_wins': 0},
'maximum': {'xsize': 50, 'ysize': 250}
}

def get_paddle_stats():
    global paddle_stats

    return paddle_stats

def get_rally_count():
    global rally

    return rally

def reset_rally_count():
    global rally

    rally['count'] = 0

def get_db():
    global db
    
    return db

def get_ball():
    global ball_location

    return ball_location

def restart_db():
    global db 
    global ball_location
    global rally
    global paddle_stats
    
    rally = {'count': 0}
    db = {'count': 0}
    ball_location = {'x': 200, 'y': 200, 'x_s': 5, 'y_s': 5, 'player_1_score': 0, 'player_2_score': 0}
    paddle_stats = {
'p1': {'xsize': 15, 'ysize': 50, 'rally_wins': 0}, 
'p2': {'xsize': 15, 'ysize': 50, 'rally_wins': 0}, 
'defaults': {'xsize': 15, 'ysize': 50, 'rally_wins': 0},
'maximum': {'xsize': 50, 'ysize': 250}
}
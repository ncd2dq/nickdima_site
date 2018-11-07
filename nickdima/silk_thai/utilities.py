from silk_thai.configuration import web_configuration
from pytz import timezone
from functools import wraps

def get_day_hour_minute():
    '''
    Return the Day of Week, Hour of Day, Minute of Day
    '''
    tz = timezone('EST')
    week_day, day_hour, day_minute = datetime.now(tz).weekday(), datetime.now(tz).time().hour, datetime.now(tz).time().minute    
    return week_day, day_hour, day_minute

def read_configuration_is_open():
    '''
    Using the configuration file, determine if Silk Thai is accepting orders
    '''
    is_currently_open = True
    week_day, day_hour, day_minute = get_day_hour_minute()

    if web_configuration['hours_of_operation'][week_day] == False:
        is_currently_open = False
    elif day_hour < web_configuration['hours_of_operation'][week_day][0]:
        is_currently_open = False
    elif day_hour == web_configuration['hours_of_operation'][week_day][1] and day_minute >= web_configuration['hours_of_operation'][week_day][2]:
        is_currently_open = False
    elif day_hour > web_configuration['hours_of_operation'][week_day][1]:
        is_currently_open = False

    print('Are we currently open?', is_currently_open)
    return is_currently_open

def is_lunch():
    '''
    Return a boolean - are we serving lunch?
    '''
    lunch_time = True
    # Monday = 0, Sunday = 6
    # Hour in range(24)
    week_day, day_hour, day_minute = get_day_hour_minute()
    if web_configuration['lunch_hours'][week_day] is False:
        lunch_time = False
    elif day_hour < web_configuration['lunch_hours'][week_day][0] or day_hour > web_configuration['lunch_hours'][week_day][1]:
        lunch_time = False

    # TODO: MAKE SOMETHING HAPPEN IF THE STORE IS CLOSED
    print('Is it lunch time?', lunch_time)
    print(week_day, day_hour)
    print('THIS IS THE TIME WE FIGURED OUT')

    return lunch_time
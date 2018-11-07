from silk_thai.configuration import web_configuration
from pytz import timezone
from datetime import datetime
from functools import wraps

def is_delivery_minimum_met(order_total):
    '''
    Returns if the delivery minimum criterion is met
    '''
    delivery_minimum_met = False
    if order_total >= web_configuration['delivery_minimum_dollars']:
        delivery_minimum_met = True
    return delivery_minimum_met

def get_day_hour_minute():
    '''
    Return the Day of Week, Hour of Day, Minute of Day
    '''
    # Monday = 0, Sunday = 6
    # Hour in range(1, 25)
    tz = timezone('EST')
    week_day, day_hour, day_minute = datetime.now(tz).weekday(), datetime.now(tz).time().hour, datetime.now(tz).time().minute    
    return week_day, day_hour, day_minute

def read_configuration_is_open():
    '''
    Using the configuration file, determine if Silk Thai is accepting orders
    '''
    is_currently_open = True
    week_day, day_hour, day_minute = get_day_hour_minute()

    print(week_day, day_hour, day_minute)
    if web_configuration['hours_of_operation'][week_day] == False:
        print('Plain old false')
        is_currently_open = False
    elif day_hour < web_configuration['hours_of_operation'][week_day][0]:
        print('closed reason 1')
        is_currently_open = False
    elif day_hour == web_configuration['hours_of_operation'][week_day][1] and day_minute >= web_configuration['hours_of_operation'][week_day][2]:
        print('closed reason 2')
        is_currently_open = False
    elif day_hour > web_configuration['hours_of_operation'][week_day][1]:
        print('closed reason 3')
        is_currently_open = False

    print('Are we currently open?', is_currently_open)
    return is_currently_open

def is_lunch():
    '''
    Return a boolean - are we serving lunch?
    '''
    lunch_time = True
    week_day, day_hour, day_minute = get_day_hour_minute()
    if web_configuration['lunch_hours'][week_day] is False:
        lunch_time = False
    elif day_hour < web_configuration['lunch_hours'][week_day][0] or day_hour > web_configuration['lunch_hours'][week_day][1]:
        lunch_time = False

    print('Is it lunch time?', lunch_time)

    return lunch_time


def is_not_summary_page(view):
    '''
    Ensures users cannot skip summary page
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):

        session['from_summary'] = False

        return view(*args, **kwargs)

    return wrapped
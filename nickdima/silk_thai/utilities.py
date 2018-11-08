#from silk_thai.configuration import web_configuration
from pytz import timezone
from datetime import datetime
from functools import wraps
from flask import session

def is_delivery_minimum_met(order_total):
    '''
    ::param:: order_total is type(CustomCurrency)
    Returns if the delivery minimum criterion is met
    '''
    return order_total.is_larger(CustomCurrency(web_configuration['delivery_minimum_cents']))

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


class CustomCurrency(object):
    '''
    This class will be used for handling currency.
    -Store as an integer in cents when performing maths
    -Export as a string dollar/cents form
    '''
    def __init__(self, int_or_string):
        if type(int_or_string) == int:
            self.int_cents_form = int_or_string
        elif type(int_or_string) == str:
            self.string_form = int_or_string
            self.int_cents_form = self.create_integer_cents_form(self.string_form)
        else:
            raise Exception('Not an int or string CustomCurrency')

    def is_larger(self, other):
        if self.int_cents_form > other.int_cents_form:
            return True
        return False

    def __add__(self, other):
        return CustomCurrency(self.int_cents_form + other.int_cents_form)

    def __sub__(self, other):
        CustomCurrency(self.int_cents_form - other.int_cents_form)

    def create_integer_cents_form(self, string_form):
        '''
        string_form = '239023.23432' 'LEFT_SIDE.RIGHT_SIDE'
        '''
        left_right = string_form.split('.')
        left_side = int(left_right[0]) * 100
        if len(left_right[1]) == 1:
            right_side = int(left_right[1]) * 10
        elif len(left_right[1]) == 2:
            right_side = int(left_right[1])
        result = left_side + right_side

        return result

    def add_string(self, string_number):
        '''
        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        add_this = self.create_integer_cents_form(string_number)

        result = current_amount + add_this

        return CustomCurrency(result)

    def add_int_cents(self, int_cents):
        '''
        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        result = current_amount + int_cents

        return CustomCurrency(result)

    def multi_string_scalar(self, string_scalar):
        '''
        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        scalar = int(string_scalar)

        result = current_amount * scalar

        return CustomCurrency(result)

    def multi_int_scalar(self, int_scalar):
        '''
        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        scalar = int_scalar

        result = current_amount * scalar

        return CustomCurrency(result)

    def export_string(self):
        '''
        Return a string representation in dollar form 
        326 --> '3.26'
        300 --> '3.00'
        '''
        current_amount = str(self.int_cents_form)
        left_side = current_amount[:-2]
        right_side = current_amount[-2:]

        result = '{}.{}'.format(left_side, right_side)

        return result

if __name__ == '__main__':

    a = CustomCurrency('2.0')
    c = CustomCurrency(1232)
    d = '2.4'
    e = 14

    test1 = c + a
    test2 = c.add_string(d)
    test3 = a.add_int_cents(e)
    test4 = a.add_string(d)
    print(test1.export_string())
    print(test2.export_string())
    print(test3.export_string())
    print(test4.export_string())
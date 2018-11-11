from silk_thai.configuration import web_configuration
from pytz import timezone
from datetime import datetime
from functools import wraps
from flask import session


def is_accepting_delivery_takeout():
    '''
    ::return:: delivery is boolean
    ::return:: takeout is boolean

    Reads configuration file to see if Silk Thai is currently accepting
    new delivery orders and/or takeout orders
    '''
    delivery = web_configuration['accepting_delivery']
    takeout  = web_configuration['accepting_takeout']

    return delivery, takeout


def is_delivery_minimum_met(order_total):
    '''
    ::param:: order_total is CustomCurrency

    ::return:: boolean

    Return if the delivery minimum criterion (from configuration) is met
    '''
    return order_total.is_larger(CustomCurrency(web_configuration['delivery_minimum_cents']))


def get_day_hour_minute():
    '''
    ::return:: integers

    Monday = 0 --> Sunday = 6
    Hour = 1 --> 24
    '''
    tz = timezone('EST')
    week_day, day_hour, day_minute = (
                                        datetime.now(tz).weekday(), 
                                        datetime.now(tz).time().hour, 
                                        datetime.now(tz).time().minute 
                                    )   

    return week_day, day_hour, day_minute


def read_configuration_is_open():
    '''
    ::return:: bolean

    Using the configuration file, determine if Silk Thai is open for business
    '''
    is_currently_open = True
    week_day, day_hour, day_minute = get_day_hour_minute()

    if web_configuration['hours_of_operation'][week_day] == False:
        is_currently_open = False

    elif day_hour < web_configuration['hours_of_operation'][week_day][0]:
        is_currently_open = False

    elif (day_hour == web_configuration['hours_of_operation'][week_day][1] 
        and day_minute >= web_configuration['hours_of_operation'][week_day][2]):
        is_currently_open = False

    elif day_hour > web_configuration['hours_of_operation'][week_day][1]:
        is_currently_open = False

    return is_currently_open


def is_lunch():
    '''
    ::return:: boolean

    Read configuration file to determine if it is lunch time
    '''
    lunch_time = True
    week_day, day_hour, day_minute = get_day_hour_minute()

    if web_configuration['lunch_hours'][week_day] is False:
        lunch_time = False
    elif (day_hour < web_configuration['lunch_hours'][week_day][0] 
        or day_hour >= web_configuration['lunch_hours'][week_day][1]):
        lunch_time = False

    return lunch_time


def is_not_checkout_page(view):
    '''
    DECORATOR

    # TODO: add app_teardown_context that turns this False as well so that
    a user cannot leave the silk thai domain from the summary page, preserving the True

    Ensures that the 'from_checkout' parameter is false as soon as you are not on the checkout
    page. This ensures that you cannot proceed to confirmation without coming directly from the
    checkout page.
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):
        session['from_checkout'] = False

        return view(*args, **kwargs)

    return wrapped


def is_not_summary_page(view):
    '''
    DECORATOR

    # TODO: add app_teardown_context that turns this False as well so that
    a user cannot leave the silk thai domain from the summary page, preserving the True

    Ensures that the 'from_summary' parameter is false as soon as you are not on the summary
    page. This ensures that you cannot proceed to checkout without coming directly from the
    summary page.
    '''
    @wraps(view)
    def wrapped(*args, **kwargs):
        session['from_summary'] = False

        return view(*args, **kwargs)

    return wrapped


class CustomCurrency(object):
    '''
    ::param:: int_or_string -> integer (in cents) or a string representation as Dollar.Cents '2.24'
    with always 2 decimal places and at least the 1's place: '0.00' '1.00' '0.01'

    ::Methods::
    is_larger
    create_integer_cents_form
    add_string
    add_int_cents
    multi_string_scalar
    multi_int_scalar
    export_string

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
        '''
        Allows you to compare CustomCurrency instances
        '''
        if self.int_cents_form > other.int_cents_form:

            return True

        return False

    def __add__(self, other):
        return CustomCurrency(self.int_cents_form + other.int_cents_form)

    def __sub__(self, other):
        return CustomCurrency(self.int_cents_form - other.int_cents_form)

    def _create_integer_cents_form_from_standard(self, string_form):
        '''
        Convert a universal representation 'X.XX' into cents

        ::param string_form:: string of form 'X.XX'
        '''
        left_right = string_form.split('.')
        left_side = int(left_right[0]) * 100

        # '0.2' becomes 20
        if len(left_right[1]) == 1:
            right_side = int(left_right[1]) * 10

        # '0.20' stays 20
        elif len(left_right[1]) == 2:
            right_side = int(left_right[1])

        result = left_side + right_side

        return result

    def _create_integer_cents_standard_form(self, string_form):
        '''
        Convert non-standard string representations of money into standard string form

        ::param string_form:: string of form '.XX' '.X' 'X.X' 
        '''
        result = ''
        # Form '.20' or '0.2' or '.2'
        if '.' in string_form:
            # Form '0.2'
            if len(string_form[string_form.index('.') + 1:]) < 2:
                result = string_form + '0'

            # Form '.2' becomes '0.2'
            if len(string_form[:string_form.index('.')]) < 1:
                result = '0' + string_form

        else:
            if len(string_form) == 3:
                result = string_form[0] + '.' + string_form[1:]

            if len(string_form) == 2:
                result = '0.' + string_form

            if len(string_form) == 1:
                result = '0.0' + string_form

        return result

    def create_integer_cents_form(self, string_form):
        '''
        string_form = '239023.23432' 'LEFT_SIDE.RIGHT_SIDE'

        ::param string_form:: string representation of money

        Parse a string representation of dollar and cents '0.00' or '.14' or '2'
        and return integer cents representation
        '''
        # Form '0.00'
        if len(string_form) >= 4 and '.' in string_form:
            result = self._create_integer_cents_form_from_standard(string_form)

        # First convert to a universal format 'X.XX' then same process as above
        elif len(string_form) <= 3:
            result = self._create_integer_cents_standard_form(string_form)
            result = self._create_integer_cents_form_from_standard(result)

        return result

    def add_string(self, string_number):
        '''
        Add together a string representation of money and this instance

        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        add_this = self.create_integer_cents_form(string_number)
        result = current_amount + add_this

        return CustomCurrency(result)

    def add_int_cents(self, int_cents):
        '''
        Add together a integer cents of money and this instance

        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        result = current_amount + int_cents

        return CustomCurrency(result)

    def multi_string_scalar(self, string_scalar):
        '''
        Multiply currency by a scalar string

        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        scalar = int(string_scalar)
        result = current_amount * scalar

        return CustomCurrency(result)

    def multi_int_scalar(self, int_scalar):
        '''
        Multiply currency by a scalar int

        Return CustomCurrency instance
        '''
        current_amount = self.int_cents_form
        scalar = int_scalar
        result = current_amount * scalar

        return CustomCurrency(result)

    def export_string(self):
        '''
        Return a string representation in dollar form of this instance
        326 --> '3.26'
        300 --> '3.00'
        '''
        current_amount = str(self.int_cents_form)
        if self.int_cents_form <= 9:
            current_amount = '00' + current_amount

        elif self.int_cents_form <= 99:
            current_amount = '0' + current_amount

        left_side = current_amount[:-2]
        right_side = current_amount[-2:]
        result = '{}.{}'.format(left_side, right_side)

        return result


class SilkCustomer(object):

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.street_address = None
        self.email_address = None
        self.phone_number = None

    def export_customer_details(self):
        pass


class SilkOrder(object):

    '''
    ::param:: self.order_time -> Datetime oject
    ::param:: self.estimated_ready_duration -> Minutes integer
    '''

    def __init__(self):
        self.order_number = None
        self.total_price_cents = None
        self.total_items = None
        self.cart = None
        self.order_type = None # Takeout / delivery
        self.special_instructions = None # For driver?

        self.order_time = None
        self.estimated_ready_duration = None

    def export_order_details(self):
        '''
        
        '''
        pass


class OrderInterface(object):
    '''
    Interfaces with SilkOrder, SilkCustomer, email, database, silk resturaunt printer
    -Send email
    -Prepare full string (order and customer details)
    -Iterfa
    '''

    def __init__(self):
        pass

    def record_details(self):
        '''
        Put order details in database
        '''
        pass

    def export_details(self):
        '''
        Prepare customer / order details for email
        '''
        pass


if __name__ == '__main__':

    a = CustomCurrency('2.0')
    c = CustomCurrency(1232)
    d = '2.4'
    e = 14
    z = CustomCurrency('0')

    print(CustomCurrency(4).export_string())
    test1 = c + a
    test2 = c.add_string(d)
    test3 = a.add_int_cents(e)
    test4 = a.add_string(d)
    print(test1.export_string())
    print(test2.export_string())
    print(test3.export_string())
    print(test4.export_string())

    test5 = z.add_int_cents(e)
    print(test5.export_string())
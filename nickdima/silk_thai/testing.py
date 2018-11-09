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
        # what if the string '300' or '0' comes in?
        if len(string_form) >= 4 and '.' in string_form:
            left_right = string_form.split('.')
            left_side = int(left_right[0]) * 100
            if len(left_right[1]) == 1:
                right_side = int(left_right[1]) * 10
            elif len(left_right[1]) == 2:
                right_side = int(left_right[1])
            result = left_side + right_side
        elif len(string_form) <= 3:
            if '.' in string_form:
                if len(string_form[string_form.index('.') + 1:]) < 2:
                    result = string_form + '0'
                if len(string_form[:string_form.index('.')]) < 1:
                    result = '0' + string_form
            else:
                if len(string_form) == 3:
                    result = string_form[0] + '.' + string_form[1:]
                if len(string_form) == 2:
                    result = '0.' + string_form
                if len(string_form) == 1:
                    result = '0.0' + string_form


            left_right = result.split('.')
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

        if self.int_cents_form <= 9:
            current_amount = '00' + current_amount

        elif self.int_cents_form <= 99:
            current_amount = '0' + current_amount

        left_side = current_amount[:-2]
        right_side = current_amount[-2:]

        result = '{}.{}'.format(left_side, right_side)

        return result

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
'''
DB Entry:
{ 'base_food_name_found_in_urls' : {'ATTRIBUTES'} }

Attributes: 
'Base' : Drunken Noodles
'Base Price' : 10.95
'Description' : Thick noodles topped with onions, tomates, etc...
'Img_URL' : /path/to/img
'Ingredients' : [Every, Single, Ingredient, To, Be, Used, For, Allergies, And, Exclude, Feature]
'Category' : Curry/Main Dish/Rice-Noodle
'Comes_With' : [Rice, Peanut Sauce]
'Toppings' : [],
'Change_Spice' : True if you can change it
'Lunch_Version' : True if can be ordered for lunch
'''

'''
Copy Paste Template ---
'base_food_name_for_urls': {
    'Base' : '',
    'Base Price': 
    'Description' : '',
    'Img_URL' : '',
    'Ingredients' : [],
    'Category' : '',
    'Comes_With' : [],
    'Toppings' : [],
    'Change_Spice' : True,
    'Lunch_Version' : True
'''


db = {
    'Drunken_noodles': {
        'Base' : 'Drunken Noodles',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : 'assets/images/pad-thai2-2000x2000.jpg',
        'Ingredients' : ['Thick Noodles', 'Tomatoes', 'Onion'],
        'Category' : 'Rice and Noodles',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : True,
        'Lunch_Version' : True
    },

    'Green_curry': {
        'Base' : 'Green Curry',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/yellow-curry2-680x965.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Curries',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },

    'Pad_thai_1': {
        'Base' : 'Pad Thai 1',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/pad-thai1-940x528-800x449.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Noodles',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },

    'Pad_thai_2': {
        'Base' : 'Pad Thai 2',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/pad-thai2-2000x2000-800x800.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Noodles',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },

    'Calamari': {
        'Base' : 'Calamari',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari2-896x504-800x450.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },

    'Silk_calamari': {
        'Base' : 'Silk Calamari',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },

    'Yellow_curry': {
        'Base' : 'Yellow Curry',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/yellow-curry1-725x483-725x483.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Curries',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },

    'Pad_se_ew': {
        'Base' : 'Pad Se Ew',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Noodles',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Change_Spice' : False,
        'Lunch_Version' : False
    },
}

def get_db():
    global db
    return db
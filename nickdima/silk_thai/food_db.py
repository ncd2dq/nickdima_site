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
    'Drunken_Noodles': {
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

    'Green_Curry': {
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
}

def get_db():
    global db
    return db
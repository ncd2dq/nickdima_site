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
'Toppings' : []
'Can_Remove' : []
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
    'Can_Remove' : []
},
'''


db = {
    'Drunken_Noodles': {
        'Base' : 'Drunken Noodles',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : '',
        'Ingredients' : ['Thick Noodles', 'Tomatoes', 'Onion'],
        'Category' : 'Rice and Noodles',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Can_Remove' : ['Tomatoes', 'Onion']
    },

    'Green_Curry': {
        'Base' : 'Green Curry',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/drunken-noodle-510x383.jpg',
        'Ingredients' : ['Red Bell Pepper', 'Green Bell Pepper'],
        'Category' : 'Curries',
        'Comes_With' : [],
        'Toppings' : ['Pork', 'Beef', 'Shrimp', 'Crispy Duck'],
        'Can_Remove' : ['Red Bell Pepper', 'Green Bell Pepper']
    },
}

def get_db():
    global db
    return db
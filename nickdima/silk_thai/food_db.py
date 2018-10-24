'''
DB Entry:
{ 'base_food_name_found_in_urls' : {'ATTRIBUTES'} }
#THE BASE URL MUST MATCH THE "ITEM=" in the URL_FOR on the menu page
Attributes: 
'Base' : Drunken Noodles
'Base Price' : 10.95
'Description' : Thick noodles topped with onions, tomates, etc...
'Img_URL' : /path/to/img
'Ingredients' : [Every, Single, Ingredient, To, Be, Used, For, Allergies, And, Exclude, Feature]
'Category' : Curry/Main Dish/Rice-Noodle
'Comes_With' : [Rice, Peanut Sauce]
'Toppings' : TUPLE OF TOPPING IN INDEX 0 AND ADDED PRICE IN INDEX 1,
'Extra' : What you are allowed to add on to the dish
'Spice' : RANGE IF POSSIBLE TO CHANGE SPACE, FALSE IF NOT
'Lunch_Version' : {'Base Price' : ,
                    'Toppings' : } or false if no lunch
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
    'Extra' : [],
    'Spice' : True,
    'Lunch_Version' : True
'''

FULL_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2), ('Seafood', 3), ('Crispy Duck', 3)]
EXTRA_DINNER_TOPPINGS = [('None', 0), ('Chicken', 3), ('Pork', 3), ('Beef', 3), ('Veggie', 3), ('Rice', 2), ('Shrimp', 5), ('Seafood', 5), ('Crispy Duck', 4)]
CURRY_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 3), ('Seafood', 3)]
FULL_LUNCH_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2)]
SPICE_RANGE = ['Default', 0, 1, 2, 3, 4, 5] 

db = {
    'Drunken_noodles': {
        'Base' : 'Drunken Noodles',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : 'assets/images/pad-thai2-2000x2000.jpg',
        'Ingredients' : ['Fresh cut wide rice noodles', 'chili', 'onions', 'tomatoes', 'basil'],
        'Category' : 'Noodles & Fried Rice',
        'Comes_With' : ['Rice'],
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Green_curry': {
        'Base' : 'Green Curry',
        'Base Price' : 11.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/yellow-curry2-680x965.jpg',
        'Ingredients' : ['Creamy coconut milk curry', 'bamboo shoots', 'chili', 'basil'],
        'Category' : 'Curries',
        'Comes_With' : ['Rice'],
        'Toppings' : CURRY_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Pad_thai_1': {
        'Base' : 'Pad Thai 1',
        'Base Price' : 10.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/pad-thai1-940x528-800x449.jpg',
        'Ingredients' : ['Rice noodles', 'bean sprouts', 'scallions', 'egg', 'roasted peanuts'],
        'Category' : 'Noodles & Fried Rice',
        'Comes_With' : [],
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Pad_thai_2': {
        'Base' : 'Pad Thai 2',
        'Base Price' : 10.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/pad-thai2-2000x2000-800x800.jpg',
        'Ingredients' : ['Rice noodles', 'bean sprouts', 'scallions', 'egg', 'roasted peanuts'],
        'Category' : 'Noodles & Fried Rice',
        'Comes_With' : [],
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Calamari': {
        'Base' : 'Calamari',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari2-896x504-800x450.jpg',
        'Ingredients' : ['Sweet & sour', 'spicy mayo duo'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Silk_calamari': {
        'Base' : 'Silk Calamari',
        'Base Price' : 7.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Lightly breaded calamari', 'onions', 'scallions', 'chili', 'sweet & sour dip'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Chicken_yellow_curry': {
        'Base' : 'Chicken Yellow Curry',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/yellow-curry1-725x483-725x483.jpg',
        'Ingredients' : ['Chicken', 'potatoes', 'carrots', 'creamy coconut milk'],
        'Category' : 'Curries',
        'Comes_With' : ['Rice'],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Pad_se_ew': {
        'Base' : 'Pad See Ew',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Fresh cut wide rice noodles', 'egg', 'dark soy', 'broccoli'],
        'Category' : 'Noodles & Fried Rice',
        'Comes_With' : False,
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },
}


def get_db():
    global db
    return db
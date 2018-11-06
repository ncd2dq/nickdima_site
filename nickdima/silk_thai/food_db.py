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
EXTRA_DINNER_TOPPINGS = [('None', 0), ('Chicken', 3), ('Pork', 3), ('Beef', 3), ('Veggie', 3), ('Shrimp', 5), ('Seafood', 5), ('Crispy Duck', 4)]
CURRY_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 3), ('Seafood', 3)]
FULL_LUNCH_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2)]
SPICE_RANGE = ['Normal', 0, 1, 2, 3, 4, 5] 

db = {
    'Drunken_noodles': {
        'Base' : 'Drunken Noodles',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : 'assets/images/pad-thai2-2000x2000.jpg',
        'Ingredients' : ['Fresh cut wide rice noodles', 'chili', 'onions', 'tomatoes', 'basil'],
        'Category' : 'Noodles',
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
        'Category' : 'Noodles',
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
        'Category' : 'Noodles',
        'Comes_With' : [],
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
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

    'Pad_see_ew': {
        'Base' : 'Pad See Ew',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Fresh cut wide rice noodles', 'egg', 'dark soy', 'broccoli'],
        'Category' : 'Noodles',
        'Comes_With' : False,
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    # APPETIZERS 
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

    'Basil_wings': {
        'Base' : 'Basil Wings',
        'Base Price' : 7.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Chili basil glaze'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Chicken_wings': {
        'Base' : 'Chicken Wings',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Thai herbs', 'sriracha'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Edamame': {
        'Base' : 'Edamame',
        'Base Price' : 4.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Steamed', 'sea salt'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Tempura': {
        'Base' : 'Edamame',
        'Base Price' : 7.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Sweet n sour dip'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : [('Veggie', 0), ('Shrimp', 0)],
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Duck_roll': {
        'Base' : 'Duck Roll',
        'Base Price' : 7.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Sliced simmered duck', 'kirby cucumber', 'scallion', 'roti'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Shrimp_rolls': {
        'Base' : 'Shrimp Rolls',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Crispy shrimp rolls', 'sweet n sour dip'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Summer_rolls': {
        'Base' : 'Summer Rolls',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Shrimp', 'cucumber', 'carrots', 'lettuce', 'vermicelli noodles', 'peanut sauce'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Crispy_fried_bean_curd': {
        'Base' : 'Crispy Fried Bean Curd',
        'Base Price' : 5.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Firm tofu', 'roasted peanut', 'sweet n sour dip'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Vegetable_spring_roll': {
        'Base' : 'Vegetable Spring Roll',
        'Base Price' : 4.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Mushrooms', 'bean thread', 'carrots', 'cabbage', 'sweet n sour dip'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Chicken_satay': {
        'Base' : 'Chicken Satay',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Grilled coconut milk-turmeric chicken on skewers', 'peanut sauce'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Kanom_jeeb': {
        'Base' : 'Kanom Jeeb',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Crabmeat', 'pork', 'ginger soy dip'],
        'Category' : 'Appetizer',
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

}


def get_db():
    global db
    return db
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
MAIN_DISH_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 3), ('Seafood', 3)]
EXTRA_DINNER_TOPPINGS = [('None', 0), ('Chicken', 3), ('Pork', 3), ('Beef', 3), ('Veggie', 3), ('Shrimp', 5), ('Seafood', 5), ('Crispy Duck', 4)]
CURRY_DINNER_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 3), ('Seafood', 3)]
SOUP_DINNER_TOPPINS = [('Veggie', 0), ('Chicken', 1), ('Shrimp', 5), ('Seafood', 5)]
FULL_LUNCH_TOPPINGS = [('Chicken', 0), ('Pork', 0), ('Beef', 0), ('Veggie', 0), ('Shrimp', 2)]
SPICE_RANGE = ['Normal', 0, 1, 2, 3, 4, 5] 

APPETIZERS = 'Appetizers'
SALADS = 'Salads'
SOUPS = 'Soups'
MAIN_DISHES = 'Main Dishes'
CURRIES = 'Curries'
NOODLES = 'Noodles'
FRIED_RICE = 'Fried Rice'
BEVERAGES = 'Beverages'

db = {
    'Drunken_noodles': {
        'Base' : 'Drunken Noodles',
        'Base Price' : 10.95,
        'Description' : 'Thick Noodle Goodness',
        'Img_URL' : 'assets/images/pad-thai2-2000x2000.jpg',
        'Ingredients' : ['Fresh cut wide rice noodles', 'chili', 'onions', 'tomatoes', 'basil'],
        'Category' : NOODLES,
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
        'Category' : CURRIES,
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
        'Category' : NOODLES,
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
        'Category' : NOODLES,
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
        'Category' : CURRIES,
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
        'Category' : NOODLES,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
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
        'Category' : APPETIZERS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    # SALADS
    'House_green_salad': {
        'Base' : 'House Green Salad',
        'Base Price' : 5.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Peanut or Chili-cream dressing'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : [('Peanut Dressing', 0), ('Chili Cream Dressing', 0)],
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Larb_gai': {
        'Base' : 'Larb Gai',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Ground chicken or tofu', 'onions', 'lettuce', 'cilantro', 'ground toasted rice', 'chili-lime dressing'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : [('Chicken', 0), ('Tofu', 0)],
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Nam_tok_beef': {
        'Base' : 'Nam Tok Beef',
        'Base Price' : 6.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Isann style sliced grilled beef', 'onions', 'lettuce', 'chili-lime dressing', 'ground toasted rice', 'cilantro'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Yum_talay': {
        'Base' : 'Yum Talay',
        'Base Price' : 9.95,
        'Description' : 'Seafood salad',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Shrimp', 'scallop', 'squid', 'onions', 'lettuce', 'chili-lime dressing'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Squid_salad': {
        'Base' : 'Squid Salad',
        'Base Price' : 7.95,
        'Description' : 'Seafood salad',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Tender squid', 'onions', 'lettuce', 'lemongrass', 'chili-lime dressing'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Plah_goong': {
        'Base' : 'Plah Goong',
        'Base Price' : 8.95,
        'Description' : 'Seafood salad',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Shrimp', 'onions', 'lettuce', 'fresh lemongrass', 'chili-lime dressing'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Yum_woonsen': {
        'Base' : 'Yum Woonsen',
        'Base Price' : 7.95,
        'Description' : 'Seafood salad',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Bean thread', 'mined chicken', 'shrimp', 'mushrooms', 'onions', 'lettuce', 'chili-lime dressing'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Som_tum': {
        'Base' : 'Yum Woonsen',
        'Base Price' : 7.95,
        'Description' : 'Green Papaya Salad',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Spicy chili-lime-fish sauce dressing', 'green papaya', 'shrimp', 'green beans', 'tomatoes', 'roasted peanuts'],
        'Category' : SALADS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    # SOUPS
    'Tom_yum_soup': {
        'Base' : 'Tom Yum Soup',
        'Base Price' : 3.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Mushrooms', 'lemongrass', 'a touch of Thai pepper'],
        'Category' : SOUPS,
        'Comes_With' : [],
        'Toppings' : SOUP_DINNER_TOPPINS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Tom_kha_soup': {
        'Base' : 'Tom Kha Soup',
        'Base Price' : 3.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Creamy coconut milk', 'galanga', 'mushrooms', 'lemongrass', 'kaffir lime leaves'],
        'Category' : SOUPS,
        'Comes_With' : [],
        'Toppings' : SOUP_DINNER_TOPPINS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Wonton_soup': {
        'Base' : 'Wonton Soup',
        'Base Price' : 4.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Green vegetable wontons', 'chicken broth'],
        'Category' : SOUPS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Bean_curd_soup': {
        'Base' : 'Bean Curd Soup',
        'Base Price' : 4.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Bean curd', 'seaweed', 'light broth'],
        'Category' : SOUPS,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    # Main Dishes
    'Pad_kra_prow': {
        'Base' : 'Pad Kra Prow',
        'Base Price' : 10.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Chili', 'basil', 'fresh green beans'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : MAIN_DISH_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Pad_khing_ginger': {
        'Base' : 'Pad Khing Ginger',
        'Base Price' : 10.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Fresh ginger', 'yellow bean sauce', 'onions', 'scallions', 'bell peppers'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : MAIN_DISH_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Chicken_cashew_nuts': {
        'Base' : 'Chicken Cashew Nuts',
        'Base Price' : 11.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Chicken', 'cashew nuts', 'carrots', 'onions', 'scallions'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Wild_pork': {
        'Base' : 'Wild Pork',
        'Base Price' : 11.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Sliced pork', 'baby corns', 'green peppercorns', 'green bean chili', 'sweet basil', 'touch of red curry'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Siam_beef': {
        'Base' : 'Siam Beef',
        'Base Price' : 12.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Marinated flank steak', 'fresh gingers', 'a dash of sesame oil'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Beef_with_oyster_sauce': {
        'Base' : 'Beef With Oyster Sauce',
        'Base Price' : 11.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Flank steak', 'oyster sauce', 'mushrooms', 'carrots', 'onions', 'green peppers'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Pad_prik_khing': {
        'Base' : 'Pad Prik Khing',
        'Base Price' : 10.95,
        'Description' : 'A creamy, green curry',
        'Img_URL' : 'assets/images/calamari1-960x640-800x533.jpg',
        'Ingredients' : ['Chili ginger paste', 'chili', 'green beans'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : MAIN_DISH_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },
}


def get_db():
    global db
    return db
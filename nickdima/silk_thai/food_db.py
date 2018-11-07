'''
DB Entry:
{ 'base_food_name_found_in_urls' : {'ATTRIBUTES'} }
#THE BASE URL MUST MATCH THE "ITEM=" in the URL_FOR on the menu page
Attributes: 
'Base' : Drunken Noodles
'Base Price' : 10.95
'Description' : Thick noodles topped with onions, tomates, etc...####Can be false####
'Img_URL' : /path/to/img
'Ingredients' : [Every, Single, Ingredient, To, Be, Used, For, Allergies, And, Exclude, Feature]
'Category' : Curry/Main Dish/Rice-Noodle
'Comes_With' : [Rice, Peanut Sauce] #############ARCHAIC PLEASE REMOVE###############
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
TOGO_BEVERAGES = 'To-Go Beverages'

PLACE_HOLDER_IMAGE = 'assets/images/calamari1-960x640-800x533.jpg'

db = {
    # TEST ITEMS START
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
        'Description' : False,
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
        'Description' : False,
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
        'Description' : False,
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
        'Description' : False,
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
    # TEST ITEMS END

    # APPETIZERS 
    'Calamari': {
        'Base' : 'Calamari',
        'Base Price' : 6.95,
        'Description' : False,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
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
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Chili ginger paste', 'chili', 'green beans'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : MAIN_DISH_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Mixed_vegetables': {
        'Base' : 'Mixed Vegetables',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Mixed vegetables', 'light soy'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Mixed_vegetables': {
        'Base' : 'Beef With Oyster Sauce',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Mixed vegetables', 'light soy'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Garlic_sauce': {
        'Base' : 'Garlic Sauce',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Fresh garlic & herb sauce', 'steamed broccoli aside'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : MAIN_DISH_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Siam_duck': {
        'Base' : 'Siam Duck',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Boneless crispy duck', 'chef\'s spicy sauce', 'onion', 'carrots', 'scallions', 'cashew nuts'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Silk_crispy_duck': {
        'Base' : 'Silk Crispy Duck',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Boneless duck', 'chili & basil'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Pineapple_duck': {
        'Base' : 'Pineapple Duck',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Crispy boneless duck', 'pineapple', 'ginger', 'scallions', 'onions', 'wine sauce'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Seafood_prik_pow': {
        'Base' : 'Seafood Prik Pow',
        'Base Price' : 17.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Shrimp', 'scallops', 'squid', 'vegetables','basil leaves', 'sweet spicy chili mixture'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Seafood_pad_cha': {
        'Base' : 'Seafood Pad Cha',
        'Base Price' : 17.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Shrimp', 'scallops', 'squid', 'mussel', 'mushrooms', 'green beans', 'spicy garlic sauce'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Eggplant_basil_sauce': {
        'Base' : 'Eggplant Basil Sauce',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Eggplant', 'thai spices', 'sweet basil'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Spicy_garden': {
        'Base' : 'Spicy Garden',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Mixed vegetables', 'fresh chili', 'yellow bean sauce'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Flounder_fillet': {
        'Base' : 'Flounder Fillet',
        'Base Price' : 18.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Golden brown flounder fillet', 'sweet basil', 'spicy chili sauce'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Tilapia_fillet': {
        'Base' : 'Tilapia Fillet',
        'Base Price' : 18.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Crispy tilapia fillet', 'creamy peanut curry', 'steamed broccoli'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Shrimp_chili_salt': {
        'Base' : 'Flounder Fillet',
        'Base Price' : 17.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Lightly battered shrimp', 'spicy garlic sauce', 'tempura green beans'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Crispy_whole_fish': {
        'Base' : 'Crispy Whole Fish (Seasonal)',
        'Base Price' : 18.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Choice of sauce'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : [('Spicy Chili & Basil', 0), ('Ginger & Mushrooms', 0)],
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Bangkok_shrimp': {
        'Base' : 'Bangkok Shrimp',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Grilled shrimp', 'fried rice', 'salad with creamy dressing'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Bangkok_steak': {
        'Base' : 'Bangkok Steak',
        'Base Price' : 18.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['NY Steak', 'grilled vegetables', 'Isann style spicy sauce'],
        'Category' : MAIN_DISHES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    # CURRIES
    'Green_curry': {
        'Base' : 'Green Curry',
        'Base Price' : 11.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Creamy coconut milk curry', 'bamboo shoots', 'chili', 'basil'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : CURRY_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Red_curry': {
        'Base' : 'Red Curry',
        'Base Price' : 11.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Creamy coconut milk curry', 'bamboo shoots', 'chili', 'basil'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : CURRY_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Panang_curry': {
        'Base' : 'Panang Curry',
        'Base Price' : 11.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Coconut milk', 'panang curry', 'peanut sauce', 'chili', 'kaffir lime leaves'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : CURRY_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Duck_red_curry': {
        'Base' : 'Duck Red Curry',
        'Base Price' : 14.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Boneless simmered duck', 'thai red curry', 'coconut milk', 'pineapple', 'tomatoes', 'chili', 'basil'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Shrimp_pineapple_curry': {
        'Base' : 'Shrimp Pineapple Curry',
        'Base Price' : 15.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Classic thai red curry', 'shrimp', 'pineapple', 'coconut milk'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Massaman_curry': {
        'Base' : 'Massaman Curry',
        'Base Price' : 12.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Chicken', 'cubed potatoes', 'onions', 'roasted peanuts', 'rich-flavored massaman curry'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    'Chicken_yellow_curry': {
        'Base' : 'Chicken Yellow Curry',
        'Base Price' : 12.95,
        'Description' : False,
        'Img_URL' : PLACE_HOLDER_IMAGE,
        'Ingredients' : ['Chicken', 'potato', 'carrot', 'coconut milk'],
        'Category' : CURRIES,
        'Comes_With' : [],
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : False
    },

    # NOODLES & FRIED RICE
    'Pad_thai': {
        'Base' : 'Pad Thai',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-thai2-2000x2000.jpg',
        'Ingredients' : ['Rice noodles', 'bean sprouts', 'scallions', 'eggs', 'roasted peanuts'],
        'Category' : NOODLES,
        'Comes_With' : [],
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Drunken_noodles': {
        'Base' : 'Drunken Noodles',
        'Base Price' : 10.95,
        'Description' : False,
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

    'Pad_see_ew': {
        'Base' : 'Pad See Ew',
        'Base Price' : 10.95,
        'Description' : False,
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

    'Chefs_fried_rice': {
        'Base' : 'Chef\'s Fried Rice',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Thai style fried rice', 'egg', 'scallions', 'tomatoes', 'light soy'],
        'Category' : FRIED_RICE,
        'Comes_With' : False,
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Guay_tiew_kau_gai': {
        'Base' : 'Guay Tiew Kau Gai',
        'Base Price' : 11.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Fresh wide rice noodles', 'chicken', 'egg', 'scallions'],
        'Category' : NOODLES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Ka_prow_fried_rice': {
        'Base' : 'Ka Prow Fried Rice',
        'Base Price' : 10.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Thai hot peppers', 'basil', 'jasmine rice'],
        'Category' : FRIED_RICE,
        'Comes_With' : False,
        'Toppings' : FULL_DINNER_TOPPINGS,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Pineapple_fried_rice': {
        'Base' : 'Pineapple Fried Rice',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Shrimp', 'chicken', 'raisins', 'cashew nuts', 'broccoli', 'a touch of curry powder', 'dried shredded pork'],
        'Category' : FRIED_RICE,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Crab_fried_rice': {
        'Base' : 'Crab Fried Rice',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Lump crabmeat', 'egg', 'scallions'],
        'Category' : FRIED_RICE,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Lobster_fried_rice': {
        'Base' : 'Lobster Fried Rice',
        'Base Price' : 16.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Lobster', 'egg', 'scallions'],
        'Category' : FRIED_RICE,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Kao_soi_chicken': {
        'Base' : 'Kao Soi Chicken',
        'Base Price' : 12.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Northern-style chicken curry broth', 'egg noodle', 'red onions', 'pickled mustard greens', 'cilantro'],
        'Category' : NOODLES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Red_curry_noodle_soup': {
        'Base' : 'Red Curry Noodle Soup',
        'Base Price' : 12.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Creamy red curry soup', 'big wonton noodles', 'curry fish balls'],
        'Category' : NOODLES,
        'Comes_With' : False,
        'Toppings' : [('Veggie', 0), ('Chicken', 0)],
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Green_curry_noodle_soup': {
        'Base' : 'Green Curry Noodle Soup',
        'Base Price' : 12.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Creamy green curry soup', 'big wonton noodles', 'curry fish balls'],
        'Category' : NOODLES,
        'Comes_With' : False,
        'Toppings' : [('Veggie', 0), ('Chicken', 0)],
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Tom_tum_noodle_soup': {
        'Base' : 'Tom Tum Noodle Soup',
        'Base Price' : 11.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Shrimp', 'ground chicken', 'rice noodles', 'bean sprouts', 'scallions', 'cilantro', 'roasted peanut', 'thai style hot & sour broth'],
        'Category' : NOODLES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    'Crispy_duck_noodle_soup': {
        'Base' : 'Crispy Duck Noodle Soup',
        'Base Price' : 13.95,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : ['Boneless crispy duck', 'egg noodles'],
        'Category' : NOODLES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : EXTRA_DINNER_TOPPINGS,
        'Spice' : SPICE_RANGE,
        'Lunch_Version' : {'Base Price' : 8.95,
                            'Toppings' : FULL_LUNCH_TOPPINGS}
    },

    # TO-GO BEVERAGES
    'Thai_ice_tea': {
        'Base' : 'Thai Ice Tea',
        'Base Price' : 2.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Thai_ice_coffee': {
        'Base' : 'Thai Ice Coffee',
        'Base Price' : 2.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Vitamin_water': {
        'Base' : 'Vitamin Water',
        'Base Price' : 2.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Gold_peak_tea': {
        'Base' : 'Gold Peak Tea',
        'Base Price' : 2.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : [('Green', 0), ('Unsweetened', 0), ('Sweet', 0)],
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Minute_maid_juice': {
        'Base' : 'Minute Maid Juice',
        'Base Price' : 2.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : [('Lemonade', 0), ('Orange', 0)],
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Bottled_water': {
        'Base' : 'Bottled Water',
        'Base Price' : 0.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : False,
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

    'Can_soda': {
        'Base' : 'Can Soda',
        'Base Price' : 0.99,
        'Description' : False,
        'Img_URL' : 'assets/images/pad-see-ew-610x458-610x458.jpg',
        'Ingredients' : False,
        'Category' : TOGO_BEVERAGES,
        'Comes_With' : False,
        'Toppings' : [('Coke', 0), ('Diet Coke', 0), ('Sprite', 0), ('Ginger Ale', 0), ('Pibb Xtra', 0)],
        'Extra' : False,
        'Spice' : False,
        'Lunch_Version' : False
    },

}


def get_db():
    global db
    return db
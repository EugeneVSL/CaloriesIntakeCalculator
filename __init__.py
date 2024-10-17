import json

nutrition_dict = {
    "Cornstarch": {
                    "calories": 381,
                    "total_fat": 0.1,
                    "protein": 0.26,
                    "carbohydrate": 91.27,
                    "sugars": 0.0,
                },
    "Nuts, pecans": {
            "calories": 691,
            "total_fat": 72.0,
            "protein": 9.17,
            "carbohydrate": 13.86,
            "sugars": 3.97,
        },
    "Eggplant, raw": {
            "calories": 25,
            "total_fat": 0.2,
            "protein": 0.98,
            "carbohydrate": 5.88,
            "sugars": 3.53,
        }
}

def nutritional_summary(food: dict):

     #declare an empty dictionary
    total_nutritional_values = {
        'calories':0,
        'total_fat':0,
        'protein':0,
        'carbohydrate':0,
        'sugars':0
    }
    
    non_existing_keys = [key for key in food.keys() if key not in nutrition_dict.keys()]

    if len(non_existing_keys) > 0:
        return non_existing_keys[0]

    for key, value in food.items():

        # get the food item
        food_item = nutrition_dict[key]

        # calculate calories
        total_nutritional_values['calories'] += value / 100 * food_item['calories']

        # calculate total fat
        total_nutritional_values['total_fat'] += value / 100 * food_item['total_fat']

        # calculate protein
        total_nutritional_values['protein'] += value / 100 * food_item['protein']

        # calculate carbohydrate
        total_nutritional_values['carbohydrate'] += value / 100 * food_item['carbohydrate']

        # calculate sugar
        total_nutritional_values['sugars'] += value / 100 * food_item['sugars']

    return total_nutritional_values
                         
# test = nutritional_summary({"Croissants, cheese": 150, "Orange juice, raw": 250})
test = nutritional_summary({"Eggplant, raw": 150, "Nuts, pecans": 250})
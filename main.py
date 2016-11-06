import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

preferences = {}


def userTastesCollector():
    for taste,question in questions.items():
            user_input = input(question)
            if (user_input == 'y') or (user_input == 'yes'): 
                preferences[taste] = True
            else:
                preferences[taste] = False


def drinkMaker(userResponses):
    for taste,ingredient in ingredients.items():
        if userResponses[taste] == True:
            print(random.choice(ingredients[taste]))


if __name__ == '__main__':
    userTastesCollector()
    drinkMaker(preferences)




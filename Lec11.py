# Nested Loop Practice Problem
def recipe_generator(styles, ingredients):
    for style in styles:
        for ingredient in ingredients:
            print(style, ingredient)


recipe_generator(["fried", "boiled", "smoked"], ["onion", "tofu", "banana"])

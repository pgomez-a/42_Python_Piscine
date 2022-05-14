class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = str()):
        """Initializes Recipe() class"""
        if not type(name) == str:
            print("Error: name parameter should be a string.")
            exit(1)
        self.name = name
        if not type(cooking_lvl) == int or cooking_lvl < 1 or cooking_lvl > 5:
            print("Error: cooking_lvl parameter should be an int between 1 and 5.")
            exit(1)
        self.cooking_lvl = cooking_lvl
        if not type(cooking_time) == int or cooking_lvl < 0:
            print("Error: cooking_time parameter should be a non-negative number.")
            exit(1)
        self.cooking_time = cooking_time
        if not type(ingredients) == list:
            print("Error: ingredients parameter should be a list of strings.")
            exit(1)
        for item in ingredients:
            if not type(item) == str:
                print("Error: ingredients parameter should be a list of strings.")
                exit(1)
        self.ingredients = ingredients
        if not type(recipe_type) == str or recipe_type not in ["starter", "lunch", "dessert"]:
                print("Error: recipe_type should be 'starter', 'lunch' or 'dessert'.")
                exit(1)
        self.recipe_type = recipe_type
        if not type(description) == str:
            print("Error: description parameter should be a string.")
            exit(1)
        self.description = description
        return

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "[name: " + self.name + "] "
        txt += "[level: " + str(self.cooking_lvl) + "] "
        txt += "[time: " + str(self.cooking_time) + "] "
        txt += "[ingred: |"
        for item in self.ingredients:
            txt += item + "|"
        txt += "] [type: " + self.recipe_type + "] "
        txt += "[desc: " + self.description + "]"
        return txt

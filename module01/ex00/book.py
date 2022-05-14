from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        """Initializes Book() class with a given name"""
        if not type(name) == str:
            print("Error: name parameter should be a string.")
            exit(1)
        self.name = name
        self.last_update = datetime.now()
        self.creation_data = datetime.now()
        self.recipes_list = {"starter" : list(), "lunch" : list(), "dessert" : list()}
        return

    def get_recipe_by_name(self, name):
        """Prints a recipe with the given name and returns the instance"""
        for recipes_type in self.recipes_list:
            for recipe in self.recipes_list[recipes_type]:
                if type(recipe) ==  Recipe and recipe.name == name:
                    print(recipe)
                    return recipe
        return False

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        recipes_names = list()
        if recipe_type in self.recipes_list:
            recipes_list = self.recipes_list[recipe_type]
            for recipe in recipes_list:
                recipes_names.append(recipe.name)
        return recipes_names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) == Recipe and recipe.recipe_type in self.recipes_list and recipe.name not in self.get_recipes_by_types(recipe.recipe_type):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
            return True
        return False

    def __str__(self):
        """Return the string to print with the book info"""
        txt = ""
        txt += str(self.last_update)
        return txt

def cookbook_details(cookbook):
    print("The available recipes are:")
    for item in cookbook:
        print("    {}".format(item))
    print("")
    return

def recipe_details(recipe, cookbook):
    try:
        recipe_dict = cookbook[recipe]
        print("Recipe for {}:".format(recipe))
        print("    Ingredients list: {}".format(recipe_dict['ingredients']))
        print("    To be eaten for {}.".format(recipe_dict['meal']))
        print("    Takes {} minutes of cooking.\n".format(recipe_dict['prep_time']))
    except:
        print("{} recipe is not in cookbook.\n".format(recipe))
    return

def remove_recipe(recipe, cookbook):
    try:
        recipe_dict = cookbook.pop(recipe)
        print("Removing {} recipe from cookbook.\n".format(recipe))
    except:
        print("{} recipe is not in cookbook.\n".format(recipe))
    return

def add_recipe(cookbook):
    name = input("Enter a name:\n>> ")
    print("")
    ingredients = input("Enter ingredients:\n>> ")
    ingredients_list = list()
    while len(ingredients) != 0:
        ingredients_list.append(ingredients)
        ingredients = input(">> ")
    print("")
    meal = input("Enter a meal type:\n>> ")
    print("")
    prep_time = input("Enter a preparation time:\n>> ")
    print("")
    while prep_time.isdigit() == False:
        prep_time = input("Error. Enter a preparation time:\n>> ")
        print("")
    recipe_dict = {'ingredients' : ingredients_list,
                   'meal' : meal,
                   'prep_time' : prep_time}
    cookbook[name] = recipe_dict
    return


if __name__ == '__main__':
    sandwich = {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal' : 'lunch',
                'prep_time' : 10}

    cake = {'ingredients' : ['flour', 'sugar', 'eggs'],
            'meal' : 'dessert',
            'prep_time' : 60}

    salad = {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
             'meal' : 'lunch',
             'prep_time' : 15}

    cookbook = dict()
    cookbook['sandiwch'] = sandwich
    cookbook['cake'] = cake
    cookbook['salad'] = salad
    print("Welcome to the Python Cookbook !")
    while True:
        print("List of available option:")
        print("    1: Add a recipe")
        print("    2: Delete a recipe")
        print("    3: Print a recipe")
        print("    4: Print the cookbook")
        print("    5: Quit\n")
        user = input("Please select an option:\n>> ")
        print("")
        if user.isdigit() == False or int(user) < 1 or int(user) > 5:
            print("Sorry, this option does not exist.\n")
        elif int(user) == 1:
            add_recipe(cookbook)
        elif int(user) == 2:
            recipe = input("Please enter a recipe name to remove it:\n")
            print("")
            remove_recipe(recipe, cookbook)
        elif int(user) == 3:
            recipe = input("Please enter a recipe name to get its details:\n")
            print("")
            recipe_details(recipe, cookbook)
        elif int(user) == 4:
            cookbook_details(cookbook)
        else:
            break

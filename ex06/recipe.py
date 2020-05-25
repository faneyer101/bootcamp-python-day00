cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def print_recipe(recipe):
    try:
        print()
        print("Recipe for", recipe + ":")
        print("Ingredients list:", cookbook[recipe]['ingredients'])
        print("To be eaten for", cookbook[recipe]['meal'] + ".")
        print("Takes", cookbook[recipe]['prep_time'], "minutes of cooking.")
        print()
    except KeyError:
        print("This recipe don't exist\n\n")


def remove_recipe(recipe):
    try:
        del cookbook[recipe]
        print("Recipe of", recipe, "is delete\n")
    except KeyError:
        print("This recipe don't exist\n\n")


def add_recipe(recipe, ingredients, meal, prep_time):
    cookbook[recipe] = {}
    cookbook[recipe]['ingredients'] = ingredients
    cookbook[recipe]['meal'] = meal
    cookbook[recipe]['prep_time'] = prep_time


def print_all_recipe():
    print()
    for recipe_id, recipe in cookbook.items():
        print("Recipe for", recipe_id + ":")
        for key in recipe:
            if key == 'ingredients':
                print("Ingredients list:", recipe[key])
            elif key == 'meal':
                print("To be eaten for", recipe[key])
            elif key == 'prep_time':
                print("Takes", recipe[key], "minutes of cooking")
        print()


def choose_utility(choose):
    input_name = "Please enter the recipe's name\n>> "
    input_ing = "Please enter ingredient separate with ','\n>> "
    input_meal = "Please enter the type of recipe\n>> "
    input_time = "Please enter the time of preparation recipe\n>> "
    input_rm = "Please enter the recipe's name to delete of cookbook:\n>> "
    input_print = "Please enter the recipe's name to get its details:\n>> "
    try:
        key = int(choose)
        if key == 1:
            name = input(input_name)
            ingredient = input(input_ing)
            meal = input(input_meal)
            time = input(input_time)
            add_recipe(name, ingredient.split(","), meal, time)
        elif key == 2:
            remove_recipe(input(input_rm))
        elif key == 3:
            print_recipe(input(input_print))
        elif key == 4:
            print_all_recipe()
        elif key == 5:
            print("\nCookbook closed")
            quit()
        else:
            print("This option does not exist,", end='')
            print(" please type the corresponding number.")
            print("To exit, enter 5\n\n")
    except ValueError:
        print("This option does not exist,", end='')
        print(" please type the corresponding number.")
        print("To exit, enter 5\n\n")


def main():
    legend = "Please select an option by typing the corresponding number:\n"
    one = "1: Add a recipe\n"
    two = "2: Delete a recipe\n"
    three = "3: Print a recipe\n"
    four = "4: Print the cookbook\n"
    five = "5: Quit\n"
    wait = ">> "
    while 1:
        choose_utility(input(legend + one + two + three + four + five + wait))


if __name__ == "__main__":
    main()

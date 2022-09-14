# Let's get cooking!

ingredient_1 = "milk"
ingredient_2 = "eggs"
ingredient_3 = "flour"
ingredient_4 = "sugar"


def print_ingredients():
    ingredients = f"{ingredient_1} {ingredient_2} {ingredient_3} {ingredient_4}"
    print(ingredient_1 + " " + ingredient_2 + " " + ingredient_3 + " " + ingredient_4)
    print("milk eggs flour sugar")
    print(ingredients)


print_ingredients()


def confirm_ingredients():
    ingredients = f"{ingredient_1} {ingredient_2} {ingredient_3} {ingredient_4}"
    print(ingredients.replace("milk", "butter"))
    print(ingredients.count("milk"))
    print(ingredients)
    print(ingredients.replace("milk", "butter"))
    print(ingredients.replace("milk", "butter").upper())


confirm_ingredients()


def favorite_bake():

    baked_good = "brownie"

    frequency = "4"

    print(type(frequency))

    print(f"Ooooh, {baked_good}s are delicious!")
    print(
        f"We recommend you eat {baked_good}s at least {int(frequency) * 2} times a month!"
    )


favorite_bake()

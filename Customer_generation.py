import random

def customer():
    primary_food = ["1 hamburger", '1 cheeseburger', '1 order of chicken nuggets']
    secondary_food = ['1 order of fries']
    drinks = ['1 water']

    order = []

    while len(order) < 1:
        choice = random.randint(0, len(primary_food))
        if choice != 0:
            order.append(primary_food[choice - 1])

        choice = random.randint(0, len(secondary_food))
        if choice != 0:
            order.append(secondary_food[choice - 1])

        choice = random.randint(0, len(drinks))
        if choice != 0:
            order.append(drinks[choice - 1])
    return order
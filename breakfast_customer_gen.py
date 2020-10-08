import random

def customer():
    primary_food = ['pancakes', 'waffles']
    secondary_food = ['1 toast', '1 sausage', '1 hashbrown', '1 bagel']
    drinks = ['1 orange juice', '1 tea', '1 coffee']

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
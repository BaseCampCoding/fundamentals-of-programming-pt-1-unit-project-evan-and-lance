import random

primary_food = ['hamburger', 'cheeseburger', 'chicken nuggets']
secondary_food = ['fries']
drinks = ['water']

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

if __name__ == "__main__":
    print(order)
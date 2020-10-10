import random

def customer():
    # List of main food items
    primary_food = ["1 hamburger", '1 cheeseburger', '1 order of chicken nuggets']
    # List of side food items
    secondary_food = ['1 order of fries']
    # List of drinks
    drinks = ['1 water', '1 sweet tea']

    # Initialize order list for computer to generate order
    order = []

    # Repeat body until there is at least 1 food item in order list
    while len(order) < 1:
        # Choose random number from 0 to amount of items in primary_food
        choice = random.randint(0, len(primary_food))
        # If choice = 0, the computer does not choose anything from the list
        if choice != 0:
            # [choice - 1] means if choice = 1, then primary_food[0] is chosen
            order.append(primary_food[choice - 1])

        # Same as primary_food comments, but with secondary_food
        choice = random.randint(0, len(secondary_food))
        if choice != 0:
            order.append(secondary_food[choice - 1])

        # Same as primary_food comments, but with drinks
        choice = random.randint(0, len(drinks))
        if choice != 0:
            order.append(drinks[choice - 1])
    return order
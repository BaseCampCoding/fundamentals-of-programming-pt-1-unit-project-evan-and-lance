# Pizza station
    # User chooses toppings, then cooks pizza for 15 seconds
# Grill station
    # User grills Steaks, ribs, or baked potatoes for 20 seconds
# Stove station
    # User cooks green peas, mashed potatoes, corn, or broccoli
# Drink station
    # Sweet tea, Water, or Chocolate milk

import time

def kitchen(order: list, demo: float) -> list:
    # Initialize prepared food list for when player starts cooking
    prepared_food = []

    while True:
        # Prints each item from the customer's order
        print("\nCustomer's order:")
        for i in order:
            print(f'- {i}')
        # Prints the name of each station
        print("""Stations:
    - Pizza Station
    - Grill Station
    - Stove Station
    - Drink Station
        """)
        # Shows the items in prepared_food list if there is at least one item in it
        if len(prepared_food) > 0:
            print('You have prepared:')
            for i in prepared_food:
                print(f'- {i}')
        # Asks the player what station they need to go to
        station_choice = input("Which station do you need? (Type 'c' to confirm order): ").lower()
        # Ensures that the player at least typed something. Otherwise, there would be an IndexError
        if len(station_choice) > 0:
            if station_choice[0] == 'p':
    # Pizza Station
                print("You are at the Pizza Station")
                # Lists the ingredients needed to make the pizzas
                ingredients = [
                    'dough', 'tomato sauce', 'cheese', 'pepperoni', 'sausage'
                    ]
                # Initialize pizza list for when the player makes the pizza
                pizza = []
                # Prints each pizza ingredient
                print('Pizza Ingredients:')
                for i in ingredients:
                    print(f'- {i}')
                    time.sleep(0.05)
                time.sleep(0.25)
                # Tells the user to add ingredients to pizza list
                print('Assemble pizza: (Type ingredients to add)')
                print("Add ingredient or type 'c' to confirm")
                # Input validation and addition loop
                while True:
                    addition = input()
                    if len(addition) > 0:
                        # Add inputted string until user enters 'c'
                        if addition != 'c':
                            pizza.append(addition)
                        else:
                            break
                    else:
                        print('Please choose a valid ingredient')
                # Initalize progress to tell if pizza has all ingredients
                progress = 0
                for i in ingredients:
                    if i != 'pepperoni' and i != 'sausage':
                        if i in pizza:
                            progress += 1
                        else:
                            print(f'You forgot the {i}!')
                # Starts cooking pizza
                print('Cooking Pizza...')
                time.sleep(20 * demo)
                # Initialize complete to determine if pizza combination is valid
                complete = False
                if progress >= 3:
                    complete = True
                if ('pepperoni' in pizza and 'sausage' in pizza) and complete:
                    prepared_food.append('1 pepperoni and sausage pizza')
                elif 'pepperoni' in pizza and complete:
                    prepared_food.append('1 pepperoni pizza')
                elif 'sausage' in pizza and complete:
                    prepared_food.append('1 sausage pizza')
                elif complete:
                    prepared_food.append('1 cheese pizza')

            if station_choice[0] == 'g':
    # Grill Station
                print('You are at the Grill Station')
                while True:
                    # List of the foods available to cook
                    items = ['steak', 'ribs', 'baked potato']
                    # Prints each food item
                    print('Foods to grill:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    # Asks the player what food they want to grill
                    food_choice = input('What do you need to grill? ').lower()
                    # Cook timings
                    # Baked potato does not need to be flipped
                    if food_choice == 'baked potato':
                        print(f'Grilling {food_choice}...')
                        time.sleep(20 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        # Add food item to prepared_food
                        prepared_food.append('1 baked potato')
                        break
                    # Other two items need to be flipped
                    elif food_choice in items:
                        print(f'Grilling {food_choice}...')
                        time.sleep(10 * demo)
                        input('Press Enter to flip')
                        print(f'Grilling {food_choice}...')
                        time.sleep(10 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        # Add food item to prepared_food
                        if food_choice == 'steak':
                            prepared_food.append('1 steak')
                            break
                        elif food_choice == 'ribs':
                            prepared_food.append('a serving of ribs')
                            break
                    else:
                        print("We don't have that")
                        time.sleep(0.75)

            if station_choice[0] == 's':
    # Stove Station
                print('You are at the Stove Station')
                while True:
                    # List of items to cook
                    items = ['green peas', 'mashed potatoes', 'corn', 'broccoli']
                    # Prints each food item
                    print('Foods to cook:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    # Asks the player what food they want
                    food_choice = input('What do you need to cook? ').lower()
                    # Cook timings
                    if food_choice in items:
                        print(f'Cooking {food_choice}...')
                        time.sleep(15 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        # Add food item to prepared_food
                        prepared_food.append(f'a side of {food_choice}')
                        break
                    else:
                        print("We don't have that")
                        time.sleep(0.75)
            if station_choice[0] == 'd':
    # Drink Station
                print('You are at the Drink Station')
                # Initialize filled to tell if drink has been filled
                filled = False
                while True: 
                    # List of items to choose
                    drinks = ['water', 'sweet tea', 'chocolate milk']
                    # Prints each beverage
                    print('Drinks to dispense:')
                    for i in drinks:
                        print(f'- {i}')
                    # Asks the player what drink they want to choose
                    drink_choice = input("What drink do you want? ").lower()
                    # Check if drink_choice is in drinks list
                    if drink_choice in drinks:
                        if not filled:
                            # Fill timings
                            input("Press enter to fill cup")
                            print("Cup is filling")
                            time.sleep(3 * demo)
                            input('Press enter to put top on cup')
                            print('Cup is being prepared...')
                            time.sleep(2 * demo)
                            print('Drink is done')
                            time.sleep(0.75)
                            filled = True
                            # Add drink to prepared_food
                            prepared_food.append(f'1 {drink_choice}')
                            break
                        else:
                            print("Drink is already prepared")
                    else: 
                        print("Make sure we have that drink first!")
                        time.sleep(0.5)
            if station_choice[0] == 'c':
    # Confirm order
                return prepared_food
        else:
            print("Please choose one of the provided stations")
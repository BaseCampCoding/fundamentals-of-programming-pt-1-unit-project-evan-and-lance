# Burger station
    # Burger patties will cook for 20 seconds
# Frier station
    # Frier takes 15 seconds to cook items
# Drink station
    # Water or sweet tea

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
    - Burger Station
    - Frier Station
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
            if station_choice[0] == 'b':
    # Burger Station
                print('You are at the Burger Station')
                time.sleep(0.5)
                # Cook timings
                input('Press Enter to start grilling pattie')
                print('Pattie is cooking...')
                time.sleep(10 * demo)
                input('Press Enter to flip pattie')
                print('Pattie is cooking...')
                time.sleep(10 * demo)
                print('Pattie is done')
                time.sleep(0.25)
                # List of ingredients in burger
                ingredients = [
                    'top bun', 'mayonaise', 'onion', 'lettuce', 'tomato', 
                    'cheese', 'pattie', 'pickles', 'mustard', 'bottom bun'
                ]
                # Initialize burger list for player to make burger
                burger = []
                # Prints burger ingredients
                print('Burger Ingredients:')
                for i in ingredients:
                    print(f'- {i}')
                    time.sleep(0.05)
                time.sleep(0.25)
                # Let player assemble burger
                print('Assemble burger: (Type ingredients to add)')
                print("Add ingredient or type 'c' to confirm")
                # Input validation and addition loop
                while True:
                    addition = input()
                    if len(addition) > 0:
                        # Add inputted string until user enters 'c'
                        if addition != 'c':
                            burger.append(addition)
                        else:
                            break
                    else:
                        print('Please choose a valid ingredient')
                # Initalize progress to tell if burger has all ingredients
                progress = 0
                for i in ingredients:
                    if i != 'cheese':
                        if i in burger:
                            progress += 1
                        else:
                            print(f'You forgot the {i}!')
                # Initialize complete to determine if burger combination is valid
                complete = False
                if progress >= 9:
                    complete = True
                if 'cheese' in burger and complete:
                    prepared_food.append('1 cheeseburger')
                elif 'cheese' not in burger and complete:
                    prepared_food.append('1 hamburger')
                else:
                    print('Make sure to have a pattie cooked first!')
                    time.sleep(0.75)

            if station_choice[0] == 'f':
    # Frier Station
                print('You are at the Frier Station')
                # Initialize fried to tell if food item has been fried
                fried = False
                while True and not fried:
                    # List of food items to fry
                    items = ['fries', 'chicken nuggets']
                    # Print items to fry
                    print('Foods to fry:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    # Asks the player what food they want to fry
                    food_choice = input('What do you need to fry? ').lower()
                    if food_choice in items:
                        # Cook timings
                        print(f'Frying {food_choice}...')
                        time.sleep(15 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        fried = True
                        # Add food to prepared_food
                        prepared_food.append(f'1 order of {food_choice}')
                        break
                    else:
                        print("We don't have that")
                        time.sleep(0.75)

            if station_choice[0] == 'd':
    # Drink Station
                print('You are at the Drink Station')
                filled = False
                while True: 
                    # List of items to choose
                    drinks = ['water', 'sweet tea']
                    # Prints each beverage
                    print('Drinks to dispense:')
                    for i in drinks:
                        print(f'- {i}')
                    # Asks the player what drink they want
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
# Skillet Station
    # Cooks Sausage, Hashbrowns, and all four pancakes
# Toaster Station
    # Cooks Waffles, Toast, and Bagel
# Drink Station
    # Dispense Orange Juice, Tea, and Coffee

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
    - Skillet Station
    - Toaster Station
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
            if station_choice[0] == 's':
    # Skillet Station
                print('You are at the Skillet Station')
                while True:
                    # List of foods to cook
                    items = ['pancakes', 'sausage', 'hashbrown']
                    # Print foods to cook
                    print('Foods to cook:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    # Asks the player what food they want to cook
                    food_choice = input('What do you need to cook? ').lower()
                    # Cook timings
                    if food_choice in items:
                        print(f'Cooking {food_choice}...')
                        time.sleep(10 * demo)
                        input('Press Enter to flip')
                        print(f'Cooking {food_choice}...')
                        time.sleep(10 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        # If pancakes, ask player for toppings
                        if food_choice == 'pancakes':
                            # List of toppings
                            toppings = ['butter', 'blueberries', 'strawberries', 'bacon']
                            # Initialize pancake list for when the player makes the pancake
                            pancake = []
                            # Print toppings
                            print('Pancake Toppings:')
                            for i in toppings:
                                print(f'- {i}')
                                time.sleep(0.05)
                            time.sleep(0.25)
                            # Let the player add toppings
                            print('Assemble pancakes: (Type toppings to add)')
                            print("Add a topping or type 'n' for no toppings")
                            # Input validation and addition loop
                            while True:
                                addition = input()
                                if len(addition) > 0:
                                    # Add the inputted string
                                    if addition in toppings:
                                        pancake.append(addition)
                                        break
                                    elif addition == 'n':
                                        break
                                    else:
                                        print('Please choose a valid topping')
                                else:
                                    print('Please choose a valid topping')
                            # Logic to determine what pancake has been made
                            if 'butter' in pancake:
                                prepared_food.append('buttered pancakes')
                                break
                            elif 'blueberries' in pancake:
                                prepared_food.append('blueberry pancakes')
                                break
                            elif 'strawberries' in pancake:
                                prepared_food.append('strawberry pancakes')
                                break
                            elif 'bacon' in pancake:
                                prepared_food.append('bacon pancakes')
                                break
                            else:
                                prepared_food.append('plain pancakes')
                                break
                        # Adds other foods to prepared_food
                        elif food_choice == 'sausage':
                            prepared_food.append('1 sausage')
                            break
                        elif food_choice == 'hashbrown':
                            prepared_food.append('1 hashbrown')
                            break

            if station_choice[0] == 't':
    # Toaster Station
                print('You are at the Toaster Station')
                # Initialize toasted to tell if food has been toasted
                toasted = False
                while True and not toasted:
                    # List of items to choose
                    items = ['waffles', 'toast', 'bagel']
                    # Prints each food item
                    print('Foods to Toast:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    # Asks the player what drink they want to toast
                    food_choice = input('What do you need to toast? ').lower()
                    # Cook timings
                    # Waffles has different prepared_food format
                    if food_choice == 'waffles':
                        print(f'Toasting {food_choice}...')
                        time.sleep(15 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        toasted = True
                        # Waffles has different prepared_food format than other food items
                        prepared_food.append('waffles')
                    elif food_choice in items:
                        print(f'Toasting {food_choice}...')
                        time.sleep(15 * demo)
                        print('Done!')
                        time.sleep(0.5)
                        toasted = True
                        # Other food item format:
                        prepared_food.append(f'1 {food_choice}')
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
                    drinks = ['orange juice', 'tea', 'coffee']
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
# Burger station
    # Burger patties will cook for 20 seconds
# Frier station
    # Frier takes 15 seconds to cook items
# Drink station
    # Water or sweet tea

import time

def kitchen(order: list) -> list:
    prepared_food = []
    while True:
        print("\nCustomer's order:")
        for i in order:
            print(f'- {i}')
        print("""Stations:
    - Burger Station
    - Frier Station
    - Drink Station
        """)
        if len(prepared_food) > 0:
            print('You have prepared:')
            for i in prepared_food:
                print(f'- {i}')
        station_choice = input("Which station do you need? (Type 'c' to confirm order): ").lower()
        if len(station_choice) > 0:
            if station_choice[0] == 'b':
    # Burger Station
                print('You are at the Burger Station')
                cooked = False
                progress = 0
                while True and progress < 2:
                    choice = input('Grill or Assembly? ')
                    choice = choice .lower()
                    if len(choice) > 0:
                        if choice[0] == 'g':
                            if not cooked:
                                input('Press Enter to start grilling')
                                print('Pattie is cooking...')
                                while True:
                                    time.sleep(10)
                                    input('Press Enter to flip pattie')
                                    print('Pattie is cooking...')
                                    time.sleep(10)
                                    break
                                print('Pattie is done')
                                time.sleep(0.25)
                                cooked = True
                                progress += 1
                            else:
                                print('Pattie is already cooked')
                        elif choice[0] == 'a' and cooked:
                            ingredients = [
                                'top bun', 'mayonaise', 'onion', 'lettuce', 'tomato', 
                                'cheese', 'pattie', 'pickles', 'mustard', 'bottom bun'
                            ]
                            burger = []
                            print('Burger Ingredients:')
                            for i in ingredients:
                                print(f'- {i}')
                                time.sleep(0.05)
                            time.sleep(0.25)
                            print('Assemble burger: (Type ingredients to add)')
                            print("Add ingredient or type 'c' to confirm")
                            while True:
                                addition = input()
                                if len(addition) > 0:
                                    if addition != 'c':
                                        burger.append(addition)
                                    else:
                                        progress += 1
                                        break
                                else:
                                    print('Please choose a valid ingredient')
                            complete = False
                            progress = 0
                            for i in ingredients:
                                if i != 'cheese':
                                    if i in burger:
                                        progress += 1
                                    else:
                                        print(f'You forgot the {i}!')
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
                fried = False
                while True and not fried:
                    items = ['fries', 'chicken nuggets']
                    print('Foods to fry:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    food_choice = input('What do you need to fry? ').lower()
                    if food_choice in items:
                        print(f'Frying {food_choice}...')
                        time.sleep(15)
                        print('Done!')
                        time.sleep(0.5)
                        fried = True
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
                    drink_choice = input("Sweet Tea or Water? ").lower()
                    if drink_choice == 'sweet tea' or drink_choice == 'water':
                        if not filled:
                            input("Press enter to fill cup")
                            print("Cup is filling")
                            while True:
                                time.sleep(3)
                                input('Press enter to put top on cup')
                                print('Cup is being prepared...')
                                time.sleep(3)
                                break
                            print('Drink is done')
                            time.sleep(0.75)
                            filled = True
                            prepared_food.append(f'1 {drink_choice}')
                            break
                        else:
                            print("Drink is already prepared")
                    else: 
                        print("Make sure we have that drink first!")
            if station_choice[0] == 'c':
                return prepared_food
        else:
            print("Please choose one of the provided stations")
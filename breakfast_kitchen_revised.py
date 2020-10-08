# Skillet Station
    # Cooks Sausage, Hashbrowns, and all four pancakes
# Toaster Station
    # Cooks Waffles, Toast, and Bagel
# Drink Station
    # Dispense Orange Juice, Tea, and Coffee

import time

def kitchen(order: list) -> list:
    prepared_food = []
    while True:
        print("\nCustomer's order:")
        for i in order:
            print(f'- {i}')
        print("""Stations:
    - Skillet Station
    - Toaster Station
    - Drink Station
        """)
        if len(prepared_food) > 0:
            print('You have prepared:')
            for i in prepared_food:
                print(f'- {i}')
        station_choice = input("Which station do you need? (Type 'c' to confirm order): ").lower()
        if len(station_choice) > 0:
            if station_choice[0] == 's':
    # Skillet Station
                print('You are at the Skillet Station')
                while True:
                    items = ['pancakes', 'sausage', 'hashbrown']
                    print('Foods to cook:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    food_choice = input('What do you need to cook? ').lower()
                    if food_choice in items:
                        print(f'Cooking {food_choice}...')
                        time.sleep(10)
                        input('Press Enter to flip')
                        print(f'Cooking {food_choice}...')
                        time.sleep(10)
                        print('Done!')
                        time.sleep(0.5)
                        if food_choice == 'pancakes':
                            toppings = ['butter', 'blueberries', 'strawberries']
                            pancake = []
                            print('Pancake Toppings:')
                            for i in toppings:
                                print(f'- {i}')
                                time.sleep(0.05)
                            time.sleep(0.25)
                            print('Assemble pancakes: (Type toppings to add)')
                            print("Add a topping or type 'n' for no toppings")
                            while True:
                                addition = input()
                                if len(addition) > 0:
                                    if addition in toppings:
                                        pancake.append(addition)
                                        break
                                    elif addition == 'n':
                                        break
                                    else:
                                        print('Please choose a valid topping')
                                else:
                                    print('Please choose a valid topping')
                            if 'butter' in pancake:
                                prepared_food.append('buttered pancakes')
                                break
                            elif 'blueberries' in pancake:
                                prepared_food.append('blueberry pancakes')
                                break
                            elif 'strawberries' in pancake:
                                prepared_food.append('strawberry pancakes')
                                break
                            else:
                                prepared_food.append('plain pancakes')
                                break
                        elif food_choice == 'sausage':
                            prepared_food.append('1 sausage')
                            break
                        elif food_choice == 'hashbrown':
                            prepared_food.append('1 hashbrown')
                            break

            if station_choice[0] == 't':
    # Toaster Station
                print('You are at the Toaster Station')
                toasted = False
                while True and not toasted:
                    items = ['waffles', 'toast', 'bagel']
                    print('Foods to Toast:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    food_choice = input('What do you need to toast? ').lower()
                    if food_choice == 'waffles':
                        print(f'Toasting {food_choice}...')
                        time.sleep(15)
                        print('Done!')
                        time.sleep(0.5)
                        toasted = True
                        prepared_food.append('waffles')
                    elif food_choice in items:
                        print(f'Toasting {food_choice}...')
                        time.sleep(15)
                        print('Done!')
                        time.sleep(0.5)
                        toasted = True
                        prepared_food.append(f'1 {food_choice}')
                        break
                    else:
                        print("We don't have that")
                        time.sleep(0.75)

            if station_choice[0] == 'd':
    # Drink Station
                print('You are at the Drink Station')
                filled = False
                while True: 
                    drinks = ['orange juice', 'tea', 'coffee']
                    print('Drinks to dispense:')
                    for i in drinks:
                        print(f'- {i}')
                    drink_choice = input("What drink do you want? ").lower()
                    if drink_choice in drinks:
                        if not filled:
                            input("Press enter to fill cup")
                            print("Cup is filling")
                            while True:
                                time.sleep(3)
                                input('Press enter to put top on cup')
                                print('Cup is being prepared...')
                                time.sleep(2)
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
                        time.sleep(0.5)
            if station_choice[0] == 'c':
                return prepared_food
        else:
            print("Please choose one of the provided stations")
# Burger station
    # Burger patties will cook for 20 seconds
# Frier station
    # Frier takes 15 seconds to cook items
# Drink station
    # Only water for now

import time

# print('start')
# begin = time.time()
# input()
# end = time.time()
# elapsed = int(end - begin)
# print(elapsed)
# input()

prepared_food = []
while True:
    print("""Stations:
- Burger Station
- Frier Station
- Drink Station
    """)
    if len(prepared_food) > 0:
        print('You have prepared:')
        for i in prepared_food:
            print(f'- {i}')
    station_choice = input("Which station do you need? (Type 'c' to confirm): ").lower()
    if len(station_choice) > 0:
        if station_choice[0] == 'b':
            # Burger station
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
                            time.sleep(0.75)
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
                        print("Add ingredient or type 'q' to quit")
                        while True:
                            addition = input()
                            if len(addition) > 0:
                                if addition != 'q':
                                    burger.append(addition)
                                else:
                                    progress += 1
                                    break
                            else:
                                print('Please choose a valid ingredient')
                    else:
                        print('Make sure to have a pattie cooked first!')
                        time.sleep(0.75)
            prepared_food.append(burger)

        if station_choice[0] == 'f':
            # Frier station
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
                    prepared_food.append(food_choice)
                    break
                else:
                    print("We don't have that")
                    time.sleep(0.75)

        if station_choice[0] == 'd':
            # Drink Station ###############################################
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
                        prepared_food.append(drink_choice)
                        break
                    else:
                        print("Drink is already prepared")
                else: 
                    print("Make sure we have that drink first!")
    else:
        print("Please choose one of the provided stations")
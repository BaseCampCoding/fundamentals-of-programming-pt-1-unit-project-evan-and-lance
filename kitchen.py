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
    station_choice = input('Which station do you need? ').lower()
    if station_choice[0] == 'b':
        # Burger station
        print('You are at the Burger Station')
        cooked = False
        progress = 0
        while True and progress < 2:
            choice = input('Grill or Assembly? ')
            choice = choice .lower()
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
                    if addition != 'q':
                        burger.append(addition)
                    else:
                        progress += 1
                        break
            else:
                print('Make sure to have a pattie cooked first!')
                time.sleep(0.75)
        print(burger)
    if station_choice[0] == 'f':
        pass
    if station_choice[0] == 'd':
        print('You are at the Drink Station')
        break
        

                
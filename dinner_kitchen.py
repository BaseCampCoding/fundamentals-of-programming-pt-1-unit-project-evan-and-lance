# Pizza station
    # User chooses toppings, then cooks pizza for 15 seconds
# Grill station
    # User grills Steaks, ribs, or baked potatoes for 20 seconds
# Stove station
    # User cooks green peas, mashed potatoes, corn, or broccoli
# Drink station
    # Sweet tea, Water, or Chocolate milk

import time

def kitchen(order: list) -> list:
    prepared_food = []
    while True:
        print("\nCustomer's order:")
        for i in order:
            print(f'- {i}')
        print("""Stations:
    - Pizza Station
    - Grill Station
    - Stove Station
    - Drink Station
        """)
        if len(prepared_food) > 0:
            print('You have prepared:')
            for i in prepared_food:
                print(f'- {i}')
        station_choice = input("Which station do you need? (Type 'c' to confirm order): ").lower()
        if len(station_choice) > 0:
            if station_choice[0] == 'p':
    # Pizza Station
                print("You are at the Pizza Station")
                ingredients = [
                    'dough', 'tomato sauce', 'cheese', 'pepperoni', 'sausage'
                    ]
                pizza = []
                print('Pizza Ingredients:')
                for i in ingredients:
                    print(f'- {i}')
                    time.sleep(0.05)
                time.sleep(0.25)
                print('Assemble pizza: (Type ingredients to add)')
                print("Add ingredient or type 'c' to confirm")
                while True:
                    addition = input()
                    if len(addition) > 0:
                        if addition != 'c':
                            pizza.append(addition)
                        else:
                            break
                    else:
                        print('Please choose a valid ingredient')
                complete = False
                progress = 0
                for i in ingredients:
                    if i != 'pepperoni' and i != 'sausage':
                        if i in pizza:
                            progress += 1
                        else:
                            print(f'You forgot the {i}!')
                if progress >= 3:
                    complete = True
                if ('pepperoni'in pizza and 'sausage' in pizza) and complete:
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
                    items = ['steak', 'ribs', 'baked potato']
                    print('Foods to grill:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    food_choice = input('What do you need to grill? ').lower()
                    if food_choice == 'baked potato':
                        print(f'Grilling {food_choice}...')
                        time.sleep(20)
                        print('Done!')
                        time.sleep(0.5)
                        prepared_food.append('1 baked potato')
                        break
                    elif food_choice in items:
                        print(f'Grilling {food_choice}...')
                        time.sleep(10)
                        input('Press Enter to flip')
                        print(f'Grilling {food_choice}...')
                        time.sleep(10)
                        print('Done!')
                        time.sleep(0.5)
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
                    items = ['green peas', 'mashed potatoes', 'corn', 'broccoli']
                    print('Foods to cook:')
                    for i in items:
                        print(f'- {i}')
                        time.sleep(0.05)
                    food_choice = input('What do you need to cook? ').lower()
                    if food_choice in items:
                        print(f'Cooking {food_choice}...')
                        time.sleep(15)
                        print('Done!')
                        time.sleep(0.5)
                        prepared_food.append(f'a side of {food_choice}')
                        break
                    else:
                        print("We don't have that")
                        time.sleep(0.75)
            if station_choice[0] == 'd':
    # Drink Station
                print('You are at the Drink Station')
                filled = False
                while True: 
                    drinks = ['water', 'sweet tea', 'chocolate milk']
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

if __name__ == "__main__":
    print(kitchen(['pizza', 'yeet']))
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
                pass
            if station_choice[0] == 's':
                pass
            if station_choice[0] == 'd':
                pass
            if station_choice[0] == 'c':
                return prepared_food

if __name__ == "__main__":
    print(kitchen(['pizza', 'yeet']))
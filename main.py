# main file to run

import lunch_customer_gen
import lunch_kitchen
import dinner_customer_gen
import dinner_kitchen
import time

def confirm_food() -> bool:
    while True:
        confirm = input('Are you ready to give this to the customer? ')
        if len(confirm) > 0:
            if confirm[0] == 'y':
                return True
            elif confirm[0] == 'n':
                return False
            else:
                print('Please type yes or no') 
        else:
            print('Please type yes or no')

name = input("What is your name?: ")

print(f'Welcome Chef {name.strip()},')

confirm = False
while True and not confirm: 
    cuisine_type = input("Breakfast, lunch, or dinner?: ").lower()
    if len(cuisine_type) > 0:
        if cuisine_type[0] == 'b':
            pass
        elif cuisine_type[0] == 'l':
            # Lunch
            order = lunch_customer_gen.customer()
            print("Here's a customer! Their order is written on this list: ")
            for i in order:
                print(f'- {i}')
            input("Press Enter to start cooking ")
            begin = time.time()
            while True:
                food = lunch_kitchen.kitchen(order)
                if confirm_food():
                    end = time.time()
                    confirm = True
                    break
        elif cuisine_type[0] == 'd':
            order = dinner_customer_gen.customer()
            print("Here's a customer! Their order is written on this list: ")
            for i in order:
                print(f'- {i}')
            input("Press Enter to start cooking ")
            begin = time.time()
            while True:
                food = dinner_kitchen.kitchen(order)
                if confirm_food():
                    end = time.time()
                    confirm = True
                    break

elapsed = int(end - begin)

if True:
    print('---dev_info---')
    print(order)
    print(food)
    print(elapsed)
    print(60 + (60 * len(order)))
    print('--------------')

confirmation = 0
for i in food:
    if i in order:
        confirmation += 1
if len(order) == confirmation:
    correct_food = 'The customer got his food'
else:
    correct_food = 'The customer did not get his food'
if elapsed < 60 + (60 * len(order)):
    in_time = 'it was in time'
else:
    in_time = 'it was not in time'

win = False
if correct_food == 'The customer did not get his food' and in_time == 'it was not in time':
    between_word = 'and'
elif correct_food == 'The customer got his food' and in_time == 'it was in time':
    between_word = 'and'
    win = True
else:
    between_word = 'but'

print('')
print(correct_food, between_word, in_time)
if win:
    print('You Win!')
else:
    print('You Lose.')
print('')

# order = str(lunch_customer_gen.customer())[1:-1]
# print("Their order is written on this list: " + order.replace("'", ''))
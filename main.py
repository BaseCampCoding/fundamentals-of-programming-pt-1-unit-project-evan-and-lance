# main file to run

import breakfast_customer_gen
import breakfast_kitchen
import lunch_customer_gen
import lunch_kitchen
import dinner_customer_gen
import dinner_kitchen
import time

# Allows user to reset prepared_food if mistakes were made
def confirm_food() -> bool:
    # Input validation
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

# Demo logic: variable demo is multipied to cook timings
demo = 1.0
if name == 'demo':
    demo = 0.1

print(f'Welcome Chef {name.strip()},')

#main loop for game replay
while True:
    # Initialize confirm to break "while True and not confirm" loop
    confirm = False
    while True and not confirm: 
        # Ask user which level they want
        cuisine_type = input("Breakfast, lunch, or dinner?: ").lower()
        # Ensures that the player at least typed something. Otherwise, there would be an IndexError
        if len(cuisine_type) > 0:
            if cuisine_type[0] == 'b':
    # Breakfast
                # Call breakfast_customer_gen file to generate order
                order = breakfast_customer_gen.customer()
                # Print customer's order
                print("Here's a customer! Their order is written on this list: ")
                for i in order:
                    print(f'- {i}')
                # Timer for player to beat
                # Player gets 1 minute flat, and 1 extra minute per item in order
                timer = 60 + (60 * len(order))
                # Convert timer from seconds to minutes
                timer_display = timer / 60
                # Print timer amount
                print(f'The customer expects his order in {timer_display:.1f} minutes or less\n')
                input("Press Enter to start cooking ")
                # Start timer
                begin = time.time()
                while True:
                    # Call breakfast_kitchen to get player created food
                    food = breakfast_kitchen.kitchen(order, demo)
                    # Call confirm_food to see if the player wants to keep or trash their food
                    if confirm_food():
                        # End timer
                        end = time.time()
                        confirm = True
                        break
            elif cuisine_type[0] == 'l':
    # Lunch
                # Call lunch_customer_gen file to generate order
                order = lunch_customer_gen.customer()
                # Print customer's order
                print("Here's a customer! Their order is written on this list: ")
                for i in order:
                    print(f'- {i}')
                # Timer for player to beat
                # Player gets 1 minute flat, and 1 extra minute per item in order
                timer = 60 + (60 * len(order))
                # Convert timer from seconds to minutes
                timer_display = timer / 60
                # Print timer amount
                print(f'The customer expects his order in {timer_display:.1f} minutes or less\n')
                input("Press Enter to start cooking ")
                # Start timer
                begin = time.time()
                while True:
                    # Call lunch_kitchen to get player created food
                    food = lunch_kitchen.kitchen(order, demo)
                    # Call confirm_food to see if the player wants to keep or trash their food
                    if confirm_food():
                        # End timer
                        end = time.time()
                        confirm = True
                        break
            elif cuisine_type[0] == 'd':
    # Dinner/Supper
                # Call lunch_customer_gen file to generate order
                order = dinner_customer_gen.customer()
                # Print customer's order
                print("Here's a customer! Their order is written on this list: ")
                for i in order:
                    print(f'- {i}')
                # Timer for player to beat
                # Player gets 1 minute flat, and 1 extra minute per item in order
                timer = 60 + (60 * len(order))
                # Convert timer from seconds to minutes
                timer_display = timer / 60
                # Print timer amount
                print(f'The customer expects his order in {timer_display:.1f} minutes or less\n')
                input("Press Enter to start cooking ")
                # Start timer
                begin = time.time()
                while True:
                    # Call lunch_kitchen to get player created food
                    food = dinner_kitchen.kitchen(order, demo)
                    # Call confirm_food to see if the player wants to keep or trash their food
                    if confirm_food():
                        # End timer
                        end = time.time()
                        confirm = True
                        break
    
    # Get the total time taken by subtracting begin time from end time
    elapsed = int(end - begin)

    # Dev info used for debugging
    if False:
        print('---dev_info---')
        print(order)
        print(food)
        print(elapsed)
        print(60 + (60 * len(order)))
        print('--------------')

    # Initialize confirmation to count correct number of food items
    confirmation = 0
    # For each item the player made...
    for i in food:
        # ...Check if that item is in the customer's order
        if i in order:
            confirmation += 1
    # If the player created food is what the customer ordered...
    if len(order) == confirmation:
        # ...Print the following:
        correct_food = 'The customer got his food'
    # If the player created food does not match the order...
    else:
        # ...Print the following:
        correct_food = 'The customer did not get his food'
    # If the player beat the timer...
    if elapsed < timer:
        # ...Print the following:
        in_time = 'it was in time'
    # If the player took too long...
    else:
        # ...Print the following:
        in_time = 'it was not in time'

    # Initialize win to determine if the player wins
    win = False
    # Logic to determine between word and win conditions
    if correct_food == 'The customer did not get his food' and in_time == 'it was not on time':
        between_word = 'and'
    elif correct_food == 'The customer got his food' and in_time == 'it was on time':
        between_word = 'and'
        win = True
    else:
        between_word = 'but'

    # Print win sentence
    print('')
    print(correct_food, between_word, in_time)
    # Print official, You Win or You Lose, statement
    if win:
        print('You Win!')
    else:
        print('You Lose.')
    print('')
    
    # Asks the player if they want to play again
    again = input('Do you want to play again? [Y/N] ').lower()
    if again == 'y':
        pass
    # If the player chooses no, break main loop
    if again == 'n':
        break
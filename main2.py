# main file to run
 

name = input("What is your name?: ")

print("Welcome Chef", name.strip(), "Looks like there's a customer at the desk. Lets see what he wants.")

import Customer_generation


print(Customer_generation.customer)
# while True: 
#     cuisine_type = input("Breakfast, lunch, or dinner?: ")
#     if cuisine_type.upper() == 'BREAKFAST':
#      input("The breakfast menu for today includes...\nPancakes \nWaffles \nFrench Toast \nWhich would you like to cook Chef " + name + "? ")
#      break
#     if cuisine_type.upper() == 'LUNCH':
#      input("The lunch menu for today includes... \nBurger \nBBQ Ribs \nFries \nWhich would you like to cook Chef " + name + "? ")
#      break
#     if cuisine_type.upper() == 'DINNER':
#      input("The dinner menu for today includes...\nSteak \nLobster \nFettuccine alfredo. \nWhich would you like to cook Chef " + name + "? ")
#      break

# difficulty = input("(Easy or Hard?) ")
# if difficulty == 'Easy' or 'easy':
#     print("You come into work, and you feel today is going to be easy as pie!")
# elif difficulty == 'Hard' or 'hard':
#     print("You come into work, and you feel today is going to be hard day!")
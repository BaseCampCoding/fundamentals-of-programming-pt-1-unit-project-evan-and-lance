import time

prepared_food = []
while True:
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
        #skillet station#
        if station_choice[0] == 's':
            print('You are at the Skillet Station')
        while True:
            skillet_or_assembly = input("Use skillet or go to assembly? ")
            if skillet_or_assembly.strip().lower() == "use skillet":
                print("Sausage, Hashbrowns or Pancakes.")
                breakfast_item_tocook = input("What will you cook? ")
                if breakfast_item_tocook.lower() == "hashbrowns":
                  input("Press Enter to start cooking")
                  print("Hashbrowns are cooking...")
                  while True:
                      time.sleep(3)
                      input("press enter to flip hashbrowns")
                      print("Hashbrowns are cooking...")
                      time.sleep(3)
                      print("Hashbrowns are done.")
                      time.sleep(2)
                      break
                else: 
                    print("Hashbrowns are already cooked.")
            elif skillet_or_assembly.strip().lower() == 'assembly':
                print("cool")
            else: 
                print("Make sure to have your Hashbrowns ready!")
            pancake_toppings = [
                'Butter', 'Blueberries', 'Strawberries'
            ]
            pancakes = []
            sausage_toppings = [
                'Syrup', 'Gravy', 
            ]
            sausage = []
          ## Toaster Station ####
    elif station_choice[0] == 't':
        print("You are in the toaster station")
                

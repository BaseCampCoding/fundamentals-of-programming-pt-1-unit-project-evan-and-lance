import random

food_choices = ['hamburger', 'cheeseburger', 'fries', 'water']
order = []

while len(order) < 0:
    for item in food_choices:
        choice = random.randint(0,2)
        if choice == 1:
            order.append(item)

# This is an update

if __name__ == "__main__":
    print(order)
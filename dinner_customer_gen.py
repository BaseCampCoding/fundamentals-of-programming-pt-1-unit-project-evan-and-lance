import random

def customer():
    primary_food = [
        '1 pepperoni pizza', '1 sausage pizza', '1 cheese pizza', 
        '1 pepperoni and sausage pizza', '1 steak', 'a serving of ribs', 
        '1 baked potato'
        ]
    secondary_food = [
        'a side of green peas', 'a side of mashed potatoes', 'a side of corn', 
        'a side of broccoli'
        ]
    drinks = ['1 water', '1 sweet tea', '1 chocolate milk']

    order = []

    while len(order) < 1:
        choice = random.randint(0, len(primary_food))
        if choice != 0:
            order.append(primary_food[choice - 1])

        choice = random.randint(0, len(secondary_food))
        if choice != 0:
            order.append(secondary_food[choice - 1])

        choice = random.randint(0, len(drinks))
        if choice != 0:
            order.append(drinks[choice - 1])
    return order

if __name__ == "__main__":
    print(customer())
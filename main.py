# main file to run
 

name = input("What is your name?: ")

print("Welcome Chef", name.strip(), "Looks like there's a customer at the desk. Lets see what he wants.")

import lunch_customer_gen

order = str(lunch_customer_gen.customer())[1:-1]
print("Their order is written on this list: " + order.replace("'", ''))
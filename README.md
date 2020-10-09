# Unit Project for Week 5, By Evan and Lance

## Text Based Tastes
Our program is a spin off of the famous franchise, Papa's Restaurant, a web 
based kitchen tycoon. Instead of being a visual game, we made it text based.

## Overview
Our program can serve breakfast, lunch, and dinner; each with their own 
"_kitchen.py" files and "_customer_gen.py" files. The player will recieve the 
customer's order, and will have to run through the kitchen to make the 
customer's order in a timely fashion.

## Features
- Breakfast, lunch, and dinner levels
- Randomized customer orders
- Unique food and drinks for each level
- Replay function at game end

## Usage
To start the game, run "main.py"

### File Purposes
**Main.py**: The control center. Ties together all other files and contains 
logic to determine if the player wins

**"_kitchen.py" Files**: Each level has its own _kitchen file. This is where 
the player recieves the order from the customer and lets the player prepare 
the food. Within each kitchen, there are stations. Each station will let the 
player cook different foods, requiring the player to think about where they 
would cook each food item.

**"_customer_gen.py" Files**: Each level has its own _customer_gen file. This 
is where the program generates a random order for the customer.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to 
discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
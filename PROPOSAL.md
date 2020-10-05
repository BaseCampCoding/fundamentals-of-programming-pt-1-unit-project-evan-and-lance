# Project Proposal

## Text Based Restaurant

### Description and Motivation
In this project, we want to build a Kitchen Tycoon game, but text-based. In 
this game, we want to have a fully functioning kitchen game, similar to the 
flash game "Papa's Burgeria", where customers will "enter", order what items 
they want, and will only leave once their order is complete. With us making 
the game text based, the player won't be able to click and drag ingredients 
on a screen, so we will have to come up with a way to interact with the kitchen 
and ingredients using only the keyboard. Our goal is to create a program where 
the player will have to take orders from a single customer and cook their food 
in a timely manner. We do not intend to include multiple customers at a time.

## Prior Art
Kitchen Tycoon games have been quite prevalent in the past. Specifically the 
"Papa's Restaurant" series, which is a flash game that has had many entries, 
from "Papa's Pizzaria" to "Papa's Freezeria". The only game that would sort of 
resemble this concept would be "Too Many Chefs", a text based kitchen game 
where you control multiple chefs at a time using only the keyboard. This is 
similar to what we intend to make, except we intend to have one "chef" in the 
kitchen.

## Core User Workflows
- Customer Generation: Our game will require randomly generated customers that 
order random meals everytime. These customers should at least order 1 item 
each time.
- Cooking: Once the customer has given their order, the player will need to 
decide which stations they will need to go to. We will have three stations: 
the burger station, the frier station, and the beverage station. Each station 
will have all needed ingredients and should produce the desired food item.
- Customer Satisfaction
	- Time: Customers will not wait hours for their food. If the player does not 
	produce the order in time, the customer will get angry and leave.
	- Correct Food: If the player gives the customer the wrong food, the customer 
	will get angry and leave.

## Daily Goals
- **Tuesday: The program should generate a customer that says what their order is**
Our first goal is to have a list of items that the customer can order and have 
the customer say what it is they want. Once we do this, we at least have a 
foundation for building up the kitchen and what we need the player to do.
- **Wednesday: The player should have a way to create the food for the customer**
Once we have a hungry customer, we will need a way to make the requested food.
We will start off building the burger station, then the frier station, and 
finally, the beverage station. For those that need to cook ingredients, we 
will have a timer that tracks for how long a given item needs to be cooked.
- **Thursday: The program should determine the customer's satisfaction**
Now that we have a hungry customer and a way to make the food, we need to 
have the program determine the customer's satisfaction given the time the 
player took, and whether or not the customer got the right food. If the 
customer is happy, the player wins. If the customer is not happy, the player 
loses.

## Students
- Evan
- Lance

## Github Repository
https://github.com/BaseCampCoding/fundamentals-of-programming-pt-1-unit-project-evan-and-lance

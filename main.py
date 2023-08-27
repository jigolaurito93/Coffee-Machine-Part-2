from menu import menu, resources

import math

# Flag to indicate whether the loop runs 
machine_on = True

money_inside = None

# Function to display the amount of resources in the coffee machine
def show_resources():
    # Variable to represent the current state of the resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    
    # condition to show if report is called from the prompt
    if not money_inside:
        print(f"\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g\n")
    elif money_inside:
                print(f"\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g\n")
                # print(f"Money: {cost}")    




# While machine_on is True, loop through the prompt
while machine_on:
    choice = input(f"  What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
    
    elif choice == "report":
          show_resources()
    

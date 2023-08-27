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

def check_enough_resources(order_ingredients):
        for item in order_ingredients:
            if order_ingredients[item] > resources[item]:
                  print(f"Sorry, there is not enough {item}.")
                  return False
        return True


# While machine_on is True, loop through the prompt
while machine_on:
    choice = input(f"  What would you like? (espresso/latte/cappuccino): ").lower()

    # If choice is off, exit while loop
    if choice == "off":
        machine_on = False
    
    # If choice is report, display the amount of resources in the coffee machine
    elif choice == "report":
          show_resources()
    
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
          drink = menu[choice]

          if check_enough_resources(drink['ingredients']):
                
          
    
    else:
          print("Invalid input, please try again.")

    




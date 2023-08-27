from menu import menu

import math

# Flag to indicate whether the loop runs 
machine_on = True


# While machine_on is True, loop through the prompt
while machine_on:
    choice = input(f"  What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False
    
    elif choice == "report" 
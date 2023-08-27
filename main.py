from menu import menu, resources

# Flag to indicate whether the loop runs 
machine_on = True

# Money inside the machine
money_inside = 0

# Function to display the amount of resources in the coffee machine
def show_resources():
    # Variable to represent the current state of the resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    global money_inside
    
    # condition to show if report is called from the prompt
    if not money_inside:
        print(f"\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g\n")
    elif money_inside:
                print(f"\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g")
                print(f"Money: ${money_inside:.2f}")    

def check_enough_resources(order_ingredients):
# Function to compare the current state of the resources and the requirement for the chosen coffee
        for item in order_ingredients:
            if order_ingredients[item] > resources[item]:
                  print(f"Sorry, there is not enough {item}.")
                  return False
        return True

def coins():
    # Returns total amount of coins inserted
    print(f"\nPlease insert coins.")
    total = float(input(f"  how many quarters?: ")) * 0.25
    total += float(input(f"  how many dimes?: ")) * 0.1
    total += float(input(f"  how many nickels?: ")) * 0.05
    total += float(input(f"  how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(payment, drink_cost):
    # Function to check if money inserted is sufficient
    if payment < drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        machine_online = False
    else:
        #If payment is more than the cost, refund the change
         global money_inside
         money_inside += payment
         user_change = payment - drink_cost
         money_inside -= user_change
         print(f"\nHere is ${user_change:.2f} dollars in change.")


def make_coffee(drink_name, order_ingredients):
    #  Deduct the required amount of ingredients from the resources
     for item in order_ingredients:
          resources[item] -= order_ingredients[item]
    # Display message saying coffee is served
     print(f"Here is your {choice} ☕. Enjoy!\n")




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
                payment = coins()
                drink_cost = drink['cost']
                is_transaction_successful(payment, drink_cost)
                make_coffee(choice, drink['ingredients'])

    else:
          # If user input something else, display this message
          print("Invalid input, please try again.")

    




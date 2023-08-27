from menu import menu

import math

machine_off = False

while not machine_off:
    choice = input(f"  What would you like? (espresso/latte/cappuccino): ").lower()
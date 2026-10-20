"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# Assignment: The Resilient Pizza Engine
# File Name: pizza_engine.py
# Date: October 20, 2026

# Define Global Tuple
TOPPINGS = ("Pepperoni", "Sausage", "Canadian Bacon", "Pineapple")


def make_pizza(customer, size, topping, is_delivery = False):
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    if is_delivery:
       print("Delivery: Yes")
    else:
       print("Delivery: No")

def main():
    customer = input("Please Enter your Name: ")
    size = input("What size pizza would you like? ")
    topping = input(f"Which topping would you like? \nYour choices are: {TOPPINGS}\n")
    delivery = input("Delivery or Pickup? ").lower()

    if delivery == "delivery":
      is_delivery = True
    elif delivery == "pickup":
       is_delivery = False

    make_pizza(customer, size, topping, is_delivery)
      


main()

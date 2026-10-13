"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# ℹ️ Assignment name: The Smoothie Sprint
# ℹ️ Date: October 13, 2026
# ℹ️ File Name: smoothie_bar.py


# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# Define get_price(size)
def get_price(size):
    # Calculate the price based on size
    if size.lower() == "small":
        return 3.00
    elif size.lower() == "medium":
        return 5.00
    elif size.lower() == "large":
        return 7.00
    else:
        print("Please enter small medium or large.")
        return 0


# Define blend(size, base, fruit, scoops) 
def blend(size, base, fruit, scoops):
    price = get_price(size)
    
    # Calculates the total based on size and scoops
    total = price * scoops
    print(f"Your {size} {fruit} smoothie with {base} "
    f"and {scoops} scoop(s) will be ${total:.2f}.")


# Define main() to collect input and call your logic
def main(): 
    # Get the user inputs of size base and fruit choices
    size = input("What size smoothie would you like (small, medium, large)? ")
    base = input(f"What base would you like {BASES}? ")
    fruit = input(f"What fruit would you like {FRUITS}? ")

    # Catches invalid scoop entries
    try:
        scoops = int(input("How many scoops would you like? "))

        if scoops <= 0:
            print("Please enter a positive number of scoops")
            return
    except ValueError:
        print("Please enter a whole number of scoops.")

    blend(size, base, fruit, scoops)

main()
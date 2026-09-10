"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Assignment: The Nag & The Song
# File Name: loops.py
# Date: September 10, 2026

# While loop

# Set arrived to false
arrived = False

# Set the while loop while arrived is False
while arrived == False:
    # Get yes or no from the user
    answer = input("Are we there yet? ").lower()

    # Check if the answer is yes 
    if answer == "yes":
        arrived = True

# For loop

# Set the start stop and step using the range function
for num_beer in range(99,1,-1):

    # Print the number of bottles of beer on the wall
    print(f"{num_beer} bottles of beer on the wall!")
print("1 bottle of beer on the wall!")

"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# Assignment Name: Madlibs
# Date: August 25, 2026
# File Name: madlibs.py


# ℹ️ Madlibs program

# ℹ️Get input from user and store in variables

print("\t\t\t\tMadlibs Program\n\n")
name = input("Enter a person's name: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
color = input("Enter a color: ")
item = input("Enter an item: ")


# ℹ️Output using the variables from user input

print(f"\n\n{name} was a {adjective} fellow")
print(f"{name} had a {color} {animal}")
print(f"Who was just as {adjective} as {name}")
print(f"They both went to {place}")
print(f"and got {color} {item}s")
print(f"and used them to {verb} the local {place}")

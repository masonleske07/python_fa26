"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Assignment: The Logic Gate
# File Name: logic.py
# Date: September 8, 2026

# Ask user for integers

num1 = int(input("Please enter any number: "))
num2 = int(input("Please enter any number: "))

# Logic tests

# First number 0 test
if not num1 == 0:
    print(f"\nYour first number: {num1}, is not 0")
else:
    print(f"\nYour first number: {num1}, is 0")

# Second number 0 test
if not num2 == 0:
    print(f"\nYour second number: {num2}, is not 0")
else:
    print(f"\nYour second number: {num2}, is 0")

# First number greater than second number test
if not num1 > num2:
    print(f"\nYour first number: {num1}, is not greater than your second number")
else:
    print(f"\nYour first number: {num1}, is greater than your second number")

# Second number greater than first number test
if not num2 > num1:
    print(f"\nYour second number: {num2}, is not greater than your first number: {num1}")
else:
    print(f"\nYour second number: {num2}, is greater than your first number: {num1}")

# Positive number test
if num1 and num2 > 0:
    print("\nBoth of your numbers are positive")
elif num1 or num2 > 0:
    print("\nOne of your numbers are positive")
else:
    print("\nNone of your numbers are positive")

# Even number test
if num1 % 2 == 0 and num2 % 2 == 0:
    print("\nBoth of your numbers are even")
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("\nOne of your numbers is even")
else:
    print("\nNeither of your numbers are even")

# Categorizing num1 as positive, negative, or zero

if num1 > 0:
    print(f"\n\nYour first number: {num1}, is positive")
elif num1 < 0:
    print(f"\n\nYour first number: {num1}, is negative")
else:
    print(f"\n\nYour first number: {num1}, is 0")


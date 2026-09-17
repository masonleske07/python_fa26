"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a loop (using a state flag or while True) to remain awake.
[ ] 3. Main menu uses match-case logic with a wildcard (case _) for selections.
[ ] 4. Inputs are validated using try-except blocks to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
# Assignment: ATM Logic Test
# File Name: atm.py
# Date: September 17, 2026

# Create a variable for the balance in the user's account
balance = 0

# Creates the loop to run the code until break command is used
while True:

    # Display the options for the user
    print("1.  Make a Deposit")
    print("2.  Make a Withdrawl")
    print("3.  Check your Balance")
    print("4.  Exit")

    # Checks the input for text or invalid numbers
    try:
        choice = int(input("Please enter the number of your choice: "))
    except ValueError:
        print("Please enter one of the number choices")
        continue

    match choice:
        case 1:
            # Checks for non numbers
            try:
                # Asks the user for the deposit amount
                deposit = float(input("How much would you like to deposit? "))
            except ValueError:
                print("Please enter a number.\n")
                continue
            # Checks for negative numbers
            if deposit < 0:
                print("You cannot deposit a negative amount\n")
                continue
            else:
                # Adds the deposit amount to the total balance ammount
                balance += deposit
                # Displays the new balance
                print(f"Your balance is now ${balance:.2f}\n")
            continue
        case 2:
            # Checks for non numbers
            try:
                # Asks the user for the withdrawal amount
                withdrawal = float(input("How much would you like to withdraw? "))
            except ValueError:
                print("Please enter a number.\n")
                continue
            # Checks for negaitve number inputs
            if withdrawal < 0:
                print("You cannot withdraw a negative amount\n")
                continue
            else:
                # Checks if the user has enough funds to withdrawal entered amount
                if withdrawal > balance:
                    print(f"You have insufficient funds, you only have ${balance:.2f}\n")
                    continue
                else:
                    # Subtracts the withdrawal amount from the total balance
                    balance -= withdrawal
                    # Displays the new balance
                    print(f"Your balance is now ${balance:.2f}\n")
                continue
        case 3:
            # Displays the balance for the user
            print(f"Your balance is ${balance:.2f}\n")
            continue
        case 4:
            print("Goodbye")
            # Ends the "While True" loop
            break
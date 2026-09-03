"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""
# Assignment: The Personal Budget
# File Name: budget.py
# Date: September 1, 2026

# Get user monthly income
income = float(input("\nWhat is your monthly income? "))

# Ask user for monthly uses of their money
rent = float(input("\nHow much do you pay per month for housing? "))

utilities = float(input("\nHow much do you pay per month for water, electric, sewer, etc. ? "))

food = float(input("\nHow much do you pay per month for food? "))

fun = float(input("\nHow much do you pay per month for entertainment? "))

gas = float(input("\nHow much do you pay per month for gas in your car? "))

# Calculate the amount of money the user spends and how much they have left and print it out
monthly_expense = rent + utilities + food + fun + gas
remaining_balance = income - monthly_expense
print(f"\nYour monthly expense is ${monthly_expense:,.2f}")
print(f"\nYour remaining balance is ${remaining_balance:,.2f}")

# Calculate the percent use of the user's monthly income and print it out
income_use = monthly_expense / income
print(f"\nYou use approximately {income_use:,.2f}% of your monthly income")



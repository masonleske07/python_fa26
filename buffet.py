"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: September 3, 2026
FILE: buffet.py
-----------------------------------------------------------------------
"""

# 1: Ask the user for the day of the week.
day = input("Please enter the day of the week, do not abbreviate: ").lower()

#  2: Use .lower() with the day input.


# 3: Use match/case to set child_price_per_year.
# Tuesday: $0.50 per year.
# Sunday: $1.00 per year and print the free-drinks notice.
# Every other day: $1.00 per year using the default case (case _).
match day.lower():
    case "sunday":
        child_price_per_year = 1
        print("\nFree drinks today!")
    case "tuesday":
        child_price_per_year = 0.50
    case _:
        child_price_per_year = 1


# 4: Ask the user for their age and convert it to an integer.
child_age = int(input("\nHow old are you? "))

# 5: Use if/elif/else to calculate the price.
# Under 1: FREE ($0.00)
# Ages 1 to 12: age multiplied by child_price_per_year
# Ages 13 to 64: $16.95
# Age 65 and older: $12.95
if child_age < 1:
    price = 0
elif child_age <= 12:
    price = child_age * child_price_per_year
elif child_age <= 64:
    price = 16.95
else:
    price = 12.95


# 6: Print the final price formatted as currency.
print(f"\n\nYour total will be ${price}")

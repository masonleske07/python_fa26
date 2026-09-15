"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined 
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# Assignment: Input Validation
# File Name: registration.py
# Date: September 15, 2026

# Start the try except statement
try:
       # Setting a while loop to restart the program for additional tickets
       restart = ""
       while not restart:
              
              # Getting the user's first name and checking with while loop
              first_name = ""
              while not first_name:
                     first_name = input("Please enter your first name: ").strip()
                     first_name = first_name.capitalize()

              # Getting the user's last name and checking with while loop
              last_name = ""
              while not last_name:
                     last_name = input("Please enter your last name: ").strip()
                     last_name = last_name.capitalize()
              print(f"Hello, {first_name} {last_name}")

              # Getting the user's age and checking if they are old enough for a drinking ticket
              age = -1
              while age < 0:
                     age = int(input("How old are you? "))
              if age >= 21:
                     print("You are old enough to get a drink ticket!")


              # Getting the user's phone number and checking it with a while loop
              phone_number = -1
              while phone_number < 0:
                     phone_number = int(input("Please enter your phone number: "))
              
              # Getting the amount of tickets the user wants and checking it with a while loop
              ticket_count = -1
              while ticket_count < 0:
                     ticket_count = int(input("How many tickets would you like? "))
              
              # Ask the user if they would like additional tickets
              add_tickets = input("Would you like additional tickets? ").lower()

              # Used an if statement to set restart to true to stop the while loop
              if add_tickets == "no":
                     restart = "No"
              
# Print out a statement for the user if they do not type a valid integer
except ValueError:
       print("Sorry that is not a valid number")

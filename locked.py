"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

# ℹ️ Assignment name: The Department Security Terminal
# ℹ️ Date: September 24, 2026
# ℹ️ File Name: locked.py

# Define department constant
DEPARTMENT = "IT"

# Define usernames tuple
USER_NAMES = (
    "joshrosen7",
    "anthonyB",
    "RogerGooden99",
    "alexcarlson$",
    "westfieldT",
    "IndigoFlo9",
    "BlazinRaisin",
    "rydog34"
)

# Define passwords list
passwords = [
    "charlie727",
    "Alpine2!",
    "window6$",
    "south24?",
    "playerz7#",
    "Hazel29_",
    "jomboy65>",
    "winter111!"
]

# starts the loop

while True:
    
# prints the options for the user and asks for a choice
    print("1. Look up Username ")
    print("2. Change Username")
    print("3. Change Password")
    print("4. Quit")

    choice =int(input("Please enter the number corresponding with your choice of action: "))

    # checks if the user entered one of the options
    if choice < 1 or choice > 5:
        print("Please enter one of the numbers listed above")
        

    match choice:

        case 1:
            # checks that the user has a correct password
            password = input("Please enter your password: ")
            
            if password in passwords:
                username = passwords.index(password)
                # prints out the username corresponding with the password
                print(f"Your Username is {USER_NAMES[username]}")
            else:
                print("Your password is incorrect")
        case 2:
                # Asks the user for a username
                username = input("Please enter your current username: ")
                # gets the index # for the username
                idx = USER_NAMES.index(username)
                try:
                    # attempts to change the user name
                    if username in USER_NAMES:
                        new_username = input("What would you like to change the username to? ")
                        USER_NAMES[idx] = new_username
                    else:
                        print("Your username is incorrect")
                except TypeError:
                    print("Usernames cannot be changed please email the help desk")
        case 3:
            # asks the user for a password and gets the index number for it
            password = input("Please enter your current password: ")
            idx = passwords.index(password)
            # checks if the password is in the list and then asks for new password and changes it
            if password in passwords:
                new_password = input("What would you like your new password to be? ")
                passwords[idx] = new_password
            else:
                print("Your password is incorrect")
        
        case 4:
            # Ends the while loop
            break



                    


            




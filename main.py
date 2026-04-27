# LIST REQUIREMENT:
# This list stores all the special symbols the program checks for.
symbols = ["!", "@", "#", "$", "%", "&", "*"]

# PROCEDURE REQUIREMENT:
# This is the student-developed procedure.
# It has a name (check_password), a parameter (password),
# and contains sequencing, selection, and iteration inside.
def check_password(password):

    # SEQUENCING: setting up variables step-by-step
    length = len(password)
    symbol_count = 0
    uppercase_count = 0
    number_count = 0

    # ITERATION REQUIREMENT:
    # Loop goes through each character in the password
    for c in password:

        # SELECTION REQUIREMENT:
        # These if-statements check different character types
        if c in symbols:          # Checks if character is a symbol
            symbol_count += 1
        if c.isupper():           # Checks if character is uppercase
            uppercase_count += 1
        if c.isdigit():           # Checks if character is a number
            number_count += 1

    # OUTPUT REQUIREMENT:
    # Program outputs information to the user
    print("Password length:", length)
    print("Symbols used:", symbol_count)
    print("Uppercase letters:", uppercase_count)
    print("Numbers:", number_count)

    # SEQUENCING + SELECTION:
    # Score increases based on password strength rules
    score = 0

    if length >= 8:
        score += 1
    if length >= 12 and (number_count > 0 or symbol_count > 0):
        score += 1
    if length >= 12 and uppercase_count > 0 and number_count > 0 and symbol_count > 0:
        score += 1

    # Final output based on score
    if score == 3:
        print("Password Strength: Strong")
    elif score == 2:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Weak")

# INPUT REQUIREMENT:
# Program takes input from the user
password_input = input("Enter a password to check: ")

# PROCEDURE CALL REQUIREMENT:
# Calls the student-developed procedure
check_password(password_input)
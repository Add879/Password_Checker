# List of symbols we want to check for in the password
symbols = ["!", "@", "#", "$", "%", "&", "*"]

# This function checks the password the user types
def check_password(password):

    # These variables start at 0 and will count things in the password
    length = len(password)          # counts how long the password is
    symbol_count = 0                # counts how many symbols
    uppercase_count = 0             # counts how many uppercase letters
    number_count = 0                # counts how many numbers


    for character in password:

        if character in symbols:
            symbol_count += 1
        
        if character.isupper():
            uppercase_count += 1

        if character.isdigit():
            number_count += 1

    # Print out all the counts
    print("Password length:", length)
    print("Symbols used:", symbol_count)
    print("Uppercase letters:", uppercase_count)
    print("Numbers:", number_count)

    # Score starts at 0 and increases if the password meets requirements
    score = 0

    # Add points based on password strength rules
    if length >= 8:
        score += 1
    if symbol_count >= 1:
        score += 1
    if uppercase_count >= 1:
        score += 1
    if number_count >= 1:
        score += 1

    # Decide if the password is Strong, Medium, or Weak
    if score == 4:
        print("Password Strength: Strong")
    elif score == 2 or score == 3:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Weak")


# Ask the user to type a password
password_input = input("Enter a password to check: ")

# Call the function to check the password
check_password(password_input)

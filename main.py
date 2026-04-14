symbols = ["!", "@", "#", "$", "%", "&", "*"]

def check_password(password):

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

    score = 0

    if length >= 8:
        score += 1
    if symbol_count >= 1:
        score += 1
    if uppercase_count >= 1:
        score += 1
    if number_count >= 1:
        score += 1

    if score == 4:
        print("Password Strength: Strong")
    elif score == 2 or score == 3:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Weak")

password_input = input("Enter a password to check: ")

check_password(password_input)

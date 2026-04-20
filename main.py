symbols = ["!", "@", "#", "$", "%", "&", "*"]

def check_password(password):

    length = len(password)
    symbol_count = 0
    uppercase_count = 0
    number_count = 0

    for character in password:

        if character in symbols:
            symbol_count += 1
        
        if character.isupper():
            uppercase_count += 1

        if character.isdigit():
            number_count += 1

    print("Password length:", length)
    print("Symbols used:", symbol_count)
    print("Uppercase letters:", uppercase_count)
    print("Numbers:", number_count)

    score = 0

    if length >= 8:
        score += 1

    if length >= 12 and (number_count > 0 or symbol_count > 0):
        score += 1

    if length >= 12 and uppercase_count > 0 and number_count > 0 and symbol_count > 0:
        score += 1

    if score == 3:
        print("Password Strength: Strong")
    elif score == 2:
        print("Password Strength: Medium")
    elif score == 1:
        print("Password Strength: Weak")
    elif score == 0:
        print("Password Strength: Weak")

password_input = input("Enter a password to check: ")

check_password(password_input)

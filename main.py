import secrets
import string

def password_generator(length, digit, special):
    """
    Generates a password with specified length and optional inclusion of digits and special characters.

    Parameters:
    - length (int): Total length of the password.
    - digit (str): 'y' if including digits, otherwise empty string.
    - special (str): 'y' if including special characters, otherwise empty string.

    Returns:
    - None: Prints the generated password.
    """

    pass_letters = string.ascii_letters
    pass_digits = string.digits
    pass_special = string.punctuation

    password = ''

    if digit == "y" and special == "y":
        pass_characters = pass_letters + pass_digits + pass_special
    elif digit == "y" and special != "y":
        pass_characters = pass_letters + pass_digits
    elif special == "y" and digit != "y":
        pass_characters = pass_letters + pass_special
    else:
        print("Error: You must select letters and at least one more criterion to generate a password.")
        return

    for i in range(length):
        password += secrets.choice(pass_characters)
    print("Your password is: ")
    print(password)

pass_length = int(input("Enter the total password length you want: "))
print("Warning: You must select letters and at least one more criterion to generate a password.")
want_digit = input("Press 'y' if you want numbers or press enter: ")
want_special = input("Press 'y' if you want special characters or press enter: ")

password_generator(pass_length, want_digit, want_special) 

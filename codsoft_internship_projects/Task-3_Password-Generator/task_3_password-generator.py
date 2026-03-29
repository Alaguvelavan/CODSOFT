import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    
    matches_requirements = False
    has_number = False
    has_special = False

    while not matches_requirements or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        matches_requirements = True
        if numbers:
            matches_requirements = has_number
        if special_characters:
            matches_requirements = matches_requirements and has_special
    
    return password
min_length = int(input("Enter the minimum length of char-based Password you require :"))
print("password is being generating...\n")

has_number = input("\nDo you want to add some numbers in it (yes/no)?: ").lower() == "yes"
has_special = input("Do you want to add some special characters in it (yes/no)?: ").lower() == "yes"


password = generate_password( min_length, has_number, has_special)
print("\nThe Generated password is : ", password)
print("\n")

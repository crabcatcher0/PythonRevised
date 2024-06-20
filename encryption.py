#takes a plain passord and hash it and give hashed.txt file 
#validation .. compares the hashed

import hashlib
import os

name = input("Enter your name: ")
print(f"Welcome to Password Manager.({name})")

def encrypt(password):
    encoded = password.encode('utf-8')
    data = hashlib.md5(encoded).hexdigest()

    with open("hashed.txt", "w") as file:
        file.write(data)
    file_path = os.path.realpath("hashed.txt")
    return f"Hashed completed check the 'hashed.txt' file in {file_path}"


def validation(input_pass):
    with open("hashed.txt", "r") as file:
        hashed_pass = file.read().strip()
    input_hashed = hashlib.md5(input_pass.encode('utf-8')).hexdigest()

    if input_hashed == hashed_pass:
        return "Password matched."
    else:
        return "Password didn't matched."
    


def check_strength(user_pass):
    length_pass = len(user_pass)
    
    if length_pass < 8:
        return f"Weak! Password is less than 8.\nYour password length: {length_pass}.\nRecommendation:\nPassword length should be more than 8 character.\nMust contain one alphabate\nMust contain one special character."
    else:
        return f"Strong! Your password length is {length_pass}."
        
    
    


while True:
    choice = input("***Options:***\n'E' to encrypt \n'V' to check \n'S' to check strength \n'Q' to exit : ").upper()

    if choice == 'E':
        user_pass = input("Enter Password: ")
        enc = encrypt(user_pass)
        print(enc)

    elif choice == 'V':
        dec_pass = input("Enter the password you want to check: ")
        dec = validation(dec_pass)
        print(dec)

    elif choice == 'S':
        input_pass = input("Enter your password: ")
        input_password = check_strength(input_pass)
        print(input_password)

    elif choice == 'Q':
        print("Exiting.... Thank you!")
        break

    else:
        print("Invalid input. Choose(E/V/Q).")

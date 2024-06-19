#takes a plain passord and  hash it

import hashlib
name = input("Enter your name: ")
print(f"Welcome to Password Manager.({name})")

def encrypt(password):
    encoded = password.encode('utf-8')
    data = hashlib.md5(encoded).hexdigest()

    with open("hashed.txt", "w") as file:
        file.write(data)
    return "Hashed completed check the 'hashed.txt' file."


def validation(input_pass):
    with open("hashed.txt", "r") as file:
        hashed_pass = file.read().strip()
    input_hashed = hashlib.md5(input_pass.encode('utf-8')).hexdigest()

    if input_hashed == hashed_pass:
        return "Password matched."
    else:
        return "Password didn't matched."


while True:
    choice = input("Enter 'E' to encrypt and 'V' to check and 'Q' to exit : ").upper()

    if choice == 'E':
        user_pass = input("Enter Password: ")
        enc = encrypt(user_pass)
        print(enc)

    elif choice == 'V':
        dec_pass = input("Enter the password you want to check: ")
        dec = validation(dec_pass)
        print(dec)

    elif choice == 'Q':
        print("Exiting.... Thank you!")
        break

    else:
        print("Invalid input. Choose(E/V/Q).")

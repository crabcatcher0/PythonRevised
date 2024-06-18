import random

choices = ["rock", "paper", "scissor"]

while True:
    user_input = input("Choose (Rock, Paper and Scissor): ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}.")


    if user_input == computer_choice:
        print("***It is a tie.***")
    
    elif (user_input == "rock" and computer_choice == "scissor") or \
        (user_input == "paper" and computer_choice == "rock") or \
        (user_input == "scissor" and computer_choice == "paper"):
        print("***You Won!!***")
        

    else:
        print("***Computer Won!!***")
    
    play_again = input("Do you wanna play again? (y/n): ").lower()
    if play_again != "y":
        print("Thank You For Playing..")
        break




import random

#this will help understand scoping

def playagain():
    global play, chances, word, guesses
    play = input("Do you want to play again? (Yes/No): ").strip().lower()
    if play == "yes":
        chances = 10
        word = random.choice(words)
        indexes = random.sample(range(len(word)), 3)
        guesses = ""
        for i in indexes:
            guesses += word[i]
  

# List of possible words
words = ["guessing", "apple", "earphones", "macbook", "python", 
         "television", "sunset", "opensource"]

# Initial setup
name = input("Enter your name: ")
print(f"Hello {name}! Welcome to the Guessing game..")
play = "yes"

while play == "yes":
    word = random.choice(words)
    indexes = random.sample(range(len(word)), 3)
    guesses = ""
    for i in indexes:
        guesses += word[i]
    
    chances = 10

    while chances > 0:
        won = True
        print("\nCurrent guess: ", end="")
        for ch in word: # the person has guessed
            if ch in guesses:
                print(ch, end=" ")
            else:
                print("_", end=" ")
                won = False

        if won:
            print("\nYou won..")
            print(f"Your score is {chances * 10}.")
            playagain()
            break

        #take a guess from the user
        guess = input("\nGuess a character: ").lower()
        if guess in guesses:
            print("You already guessed that character. Try a different one.")
            continue

        guesses += guess

        if guess not in word:
            chances -= 1
            print("\nWrong answer!!")
            print(f"You have {chances} chances left!")

            if chances == 0:
                print("You Lose!")
                playagain()
                break
print(f"Thanks for playing!! Byee.. {name}")

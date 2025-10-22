# Project-1.Zeus
import random

print("Hello user! I hope you're doing wonderful!")
print("I wanted to play rock paper scissors and just so happened to run into you")

# Asking if the user wants to play
while True:
    choice = input("Do you wanna play? Yes or No: ").strip().lower()
    if choice == "yes":
        print("Great!")
        break
    elif choice == "no":
        print("Ok:/ Maybe next time!")
        exit()
    else:
        print("I can't understand you. Please type 'Yes' or 'No'.")

play_again = "yes"
options = ["rock", "paper", "scissors"]

while play_again == "yes":
    # Get valid user move
    while True:
        user_move = input("Please type either 'Rock', 'Paper', or 'Scissors': ").strip().lower()
        if user_move in options:
            print(f"You chose {user_move.capitalize()}!")
            break
        else:
            print("You didn't enter a valid input.")
    
    computer_move = random.choice(options)
    print(f"The computer chose {computer_move.capitalize()}!")

    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        print("You win!")
    else:
        print("You lose!")
    
    play_again = input("\nAwesome!! Do you want to play again? (Yes or No): ").strip().lower()
    if play_again not in ["yes", "no"]:
        print("I'll take that answer as a 'no'. Thanks for playing!")
        break

print("Goodbye!")

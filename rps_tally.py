# rps_tally.py
import random

user_win = 0
computer_win = 0
ties = 0


def ask_to_play():
    while True:
        choice = input("Do you want to play Rock, Paper, Scissors with me? 'Yes' or 'No': ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("I can't understand you. Please type 'Yes' or 'No'.")


if not ask_to_play():
    print("Maybe next time. Goodbye!")
    exit()

play_again = "yes"
options = ["rock", "paper", "scissors"]

while play_again == "yes":
    print("\nCurrent tallies:")
    print("User wins:", user_win)
    print("Computer wins:", computer_win)
    print("Ties:", ties)

    # Get a valid user move
    while True:
        user_move = input("Please type either 'Rock', 'Paper', or 'Scissors': ").strip().lower()
        if user_move in options:
            print(f"You chose {user_move.capitalize()}!")
            break
        else:
            print("You didn't enter a valid input.")

    # Computer move
    computer_move = random.choice(options)
    print(f"The computer chose {computer_move.capitalize()}!")

    # Determine winner
    if user_move == computer_move:
        ties += 1
        print("It's a tie!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        user_win += 1
        print("You win!")
    else:
        computer_win += 1
        print("You lose!")

    # Ask if user wants to play again
    play_again = input("\nAwesome!! Do you want to play again? (Yes or No): ").strip().lower()

    if play_again not in ["yes", "no"]:
        print("I'll take that answer as a 'no'. Thanks for playing!")
        break

# Game over
print("\nFinal Tallies:")
print("User wins:", user_win)
print("Computer wins:", computer_win)
print("Ties:", ties)
print("Goodbye!")

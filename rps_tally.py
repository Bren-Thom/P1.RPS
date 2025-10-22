#rps_tally.py
import random

user_win = 0
computer_win = 0
ties = 0 


def ask_to_play():
  while True:
    choice = input("Do want to play Rock, Paper, Scissors with me? 'Yes' or 'No' ").strip().lower()
    if choice == "yes":
      return True 
    elif choice == "no":
      return False
    else:
      print("I can't understand you. Please type 'Yes' or 'No'.")

play_again = "yes"
options = ["rock", "paper", "scissors"]

while play_again == "yes":
  while True:
    print("\n Current tallies: ")
    print("User_wins:", user_win)
    print("Computer_wins:", computer_win)
    print("Ties:", ties)
    user_move = input("Please type either 'Rock', 'Paper', or 'Scissors': ").strip().lower()
        if user_move in options:
            print(f"You chose {user_move.capitalize()}!")
            break
        else:
            print("You didn't enter a valid input.")
          
  computer_move = random.choice(options)
  print(f"The computer chose {computer_move.capitalize()}!")
  if user_move == computer_move:
    ties += 1
    print("It's a tie!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        user_win += 1
        print("You win!")
    else:
        computer_wins += 1
        print("You lose!")
      
  play_again = input("\nAwesome!! Do you want to play again? (Yes or No): ").strip().lower()
  print("\nFinal Tallies: ")
      print("User_wins: ", user_win)
      print("Computer_win: ", computer_win)
      print("Ties: ", ties)
    if play_again not in ["yes", "no"]:
        print("I'll take that answer as a 'no'. Thanks for playing!")
        break

print("Goodbye!")




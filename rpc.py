# Project-1.Zeus
import random

print("Hello user! I hope you're doing wonderful!")
print("I wanted to play rock paper scissors and just so happened to run into you")

'''Asking if the user wants to play'''
while True:
  choice = str(input("Do you wanna play? Yes or No: "))
  if choice.lower() == "yes":
    print("Great!")
    break
  elif choice.lower() == "no":
    print("Ok:/ Maybe next time!")
    exit()
  else:
    print("I cant understand you. Please type 'Yes' or 'No'.")
'''This is my first time using break and .lower in coding so It may not be the most optimized. Its supposed to loop until the user says 'yes' or 'no'.'''

play_again = "yes"
options = ["rock", "paper", "scissors"]

while play_again == "yes": 
  while True:
  user_move = input("Please type either 'Rock', 'Paper', or 'scissors'.").lower()
  if user_move == "rock":
    print("You choose Rock!")
    break
  elif user_move == "paper":
    print("You choose Paper!")
    break
  elif user_move == "scissors":
    print("You choose Scissors!")
    break
  else:
    print("You didnt enter a valid input")

computer_move = random.choice(options)
if user_move == "rock" and computer_move == "scissors":
  print("You win!")
elif user_move == "paper" and computer_move == "rock":
  print("You win!")
elif user_move == "scissors" and computer_move == "paper":
  print("You win!")
elif user_move == computer_move:
  print("Its a tie!")
else:
  print("You lose!")

play_again = input("\nAwsome!! Do you want to play again? (Yes or No): ").lower()
if play again not in ["yes", "no"]:
  print("I'll take that answer as a 'no'. Thanks for playing!")
  break

print("Goodbye!")

  

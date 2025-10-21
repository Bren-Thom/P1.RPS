# Project-1.Zeus
print("Hello user! I hope your doing wonderful!\nI wanted to play rock paper scissors and just so happened to run into you")
choice = str(input("Do you wanna play? Yes or No."))

while True:
  if choice.lower() == "yes":
    print("Great!")
    break
  elif choice.lower() == "no":
    print("Ok:/")
    break
  else:
    print("I cant understand you. Please type 'Yes' or 'No'.")
'''This is my first time using break and .lower in coding so It may not be the most optimized. Its supposed to loop until the user says 'yes' or 'no'.'''

import random
options = ["rock", "paper", "scissors"]

while True
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
if user_move = 

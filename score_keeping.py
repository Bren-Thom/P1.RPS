#Score keeping Test

'''This is the initial count of every choice'''
rock = 0 
paper = 0
scissors = 0

'''This is supposed to display the tallies'''
while true
print("\n Current tallies: ")
print("Rock:", rock)
print("Paper:", paper)
print("Scissors:", scissors)

'''This is explaining to the user how to add to wach tally'''
user_choice = str(input("\nType out 'Rock', 'Paper, or 'Scissors' to add to each respective tally, or type 'Quit' to stop: ").lower()
  if user_choice == "rock":
      rock += 1
      print("You added one rock!")
  elif user_choice == "paper":
      paper += 2
      print("You added one paper!")
  elif user_choice == "scissors":
      print("You added one scissors!")
'''this is when the user wants to end the counting and the loop will end'''
  elif user_choice == "quit":
      print("\nFinal Tallies: ")
      print("Rock: ", rock)
      print("Paper: ", paper)
      print("Scissors: ", scissors)
      break 
else:
  print("Please type 'Rock', 'Paper, 'Scissors', or 'Quit'")
          
                    

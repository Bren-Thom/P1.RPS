#Random number generator 

import random

one = 0
two = 0
three = 0
four = 0 
five = 0
six = 0 

def ask_to_play():
  while True:
    question = input("Do you wanna roll some dice with me? Yes or No: ").strip().lower():
      if question == "yes":
        return True
      elif question == "no":
        return False
      else:
        print("I cant understand you. Yes or No.")

if not ask_to_play():
    print("Maybe next time. Goodbye!")
    exit()


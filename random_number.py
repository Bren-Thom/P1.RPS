# Random number generator(Dice Roller)

import random

# Tallies for each dice number
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

def ask_to_play():
    while True:
        question = input("Do you wanna roll some dice with me? Yes or No: ").strip().lower()
        if question == "yes":
            return True
        elif question == "no":
            return False
        else:
            print("I can't understand you. Please type 'Yes' or 'No'.")

# Ask if user wants to play
if not ask_to_play():
    print("Maybe next time. Goodbye!")
    exit()

play_again = "yes"

# Main game loop
while play_again == "yes":
    # Roll a dice (random number 1-6)
    roll = random.randint(1, 6)
    print(f"\nYou rolled a {roll}!")

    # Add to tally
    if roll == 1:
        one += 1
    elif roll == 2:
        two += 1
    elif roll == 3:
        three += 1
    elif roll == 4:
        four += 1
    elif roll == 5:
        five += 1
    elif roll == 6:
        six += 1

    # Show current tallies
    print("\nCurrent tallies:")
    print(f"1: {one}")
    print(f"2: {two}")
    print(f"3: {three}")
    print(f"4: {four}")
    print(f"5: {five}")
    print(f"6: {six}")

    # Ask to roll again
    play_again = input("\nDo you want to roll again? Yes or No: ").strip().lower()

print("\nThanks for playing! Final tallies:")
print(f"1: {one}")
print(f"2: {two}")
print(f"3: {three}")
print(f"4: {four}")
print(f"5: {five}")
print(f"6: {six}")

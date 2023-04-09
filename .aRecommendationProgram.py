import os
import random

# Check if the history file exists, if not create one
if not os.path.exists('.aHistory.txt'):
    with open('.aHistory.txt', 'w') as f:
        f.write('')

# Read the list of files in the current directory
files = os.listdir()

# Read the history file to check for already picked items
with open('.aHistory.txt', 'r') as f:
    history = f.read().splitlines()

# Filter out the already picked items
files = [file for file in files if file not in history]

# Check if there are any files left to pick
if not files:
    print("You've already picked all the files!")
    exit()

# Pick a random file and recommend it to the user
file = random.choice(files)
print(f"We recommend picking '{file}'")

# Ask the user if they want to save the item to history
save = input("Do you want to save this item to history? (y/n) ")

# If yes, add the item to the history file
if save.lower() == 'y':
    with open('.aHistory.txt', 'a') as f:
        f.write(file + '\n')

# Ask the user what they want to do next
while True:
    next_action = input("What do you want to do next? (pick another item/goodbye) ")

    if next_action.lower() == 'pick another item':
        # Read the history file to check for already picked items
        with open('.aHistory.txt', 'r') as f:
            history = f.read().splitlines()

        # Filter out the already picked items
        files = [file for file in files if file not in history]

        # Check if there are any files left to pick
        if not files:
            print("You've already picked all the files!")
            exit()

        # Pick a random file and recommend it to the user
        file = random.choice(files)
        print(f"We recommend picking '{file}'")

        # Ask the user if they want to save the item to history
        save = input("Do you want to save this item to history? (y/n) ")

        # If yes, add the item to the history file
        if save.lower() == 'y':
            with open('.aHistory.txt', 'a') as f:
                f.write(file + '\n')

    elif next_action.lower() == 'goodbye':
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter 'pick another item' or 'goodbye'.")


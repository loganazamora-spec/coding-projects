"""
Dice Game 12 — Starter Template
Author: Logan Zamora

PSEUDOCODE (overall algorithm):
1) Print welcome text.
2) wins, losses = 0, 0
3) LOOP forever
     a) play one round → get a single result string: 'win'/'loss'/'none'/'quit'
     b) if result is 'quit' → break out of the loop
     c) if result is 'win' → wins += 1
        if result is 'loss' → losses += 1
        (ignore 'none')
     d) print "Next round!" and loop
4) print final #win and #loss and "Game Over!"
"""

import random

# ===== Constants (do not change) =====
TARGET = 12
DICE_MIN = 1
DICE_MAX = 6
rolled_dice = []

# ===== Functions =====

def print_welcome():
    """Prints the welcome/instruction line."""
    # Pseudocode:
    # 1. Print the welcome message explaining the game goal and rules.
    print("Welcome to dice game 12. You will roll 3 dice, with the goal of getting a total sum of 12 from those dice rolls.")

    play_round()



def roll_die(dice_choice):
    """Returns a random integer between DICE_MIN and DICE_MAX inclusive."""
    # Pseudocode:
    # 1. Use random.randint(DICE_MIN, DICE_MAX) to simulate rolling a die.
    roll_value = random.randint(DICE_MIN, DICE_MAX)

    rolled_dice.append(dice_choice)

    # 2. Return the rolled number  
    return roll_value and rolled_dice



def show_state(d1, d2, d3, wins, losses):
    """Displays the current dice values and totals in the required format."""
    # Pseudocode:
    # 1. Compute total = d1 + d2 + d3.
    
    # 2. Print the dice values, total, and current win/loss count.



def read_choice(rolled1, rolled2, rolled3):
    """Asks which die to roll or if the player wants to quit.
    Keeps prompting until the choice is valid and the die has not been rolled yet.
    Returns: 1, 2, 3, or 'q'.
    """
    # Pseudocode:
    # 1. Loop forever:
    #    a) Ask the user to enter '1', '2', '3', or 'q'.
    #    b) If 'q' → return 'q'.
    #    c) If not one of '1','2','3' → print invalid message and continue.
    #    d) Convert choice to int.
    #    e) Check if the selected die was already rolled → if yes, print message and continue.
    #    f) Return the valid die number.
    valid_inputs = [1, 2, 3, 'q']
    while True:
        user_input = input("Please choose which die to roll, or if you'd like to quit (with q): ")

        if user_input in valid_inputs:
            if user_input == 'q':
                print("Thanks for playing!")
                break
            else:
                dice_choice = input("Which die would you like to roll? (1, 2, 3)")
                if dice_choice.isdigit():
                    if dice_choice in rolled_dice:
                        print("You have already rolled this die")
                        continue
                    else:
                        int(dice_choice)
                        return dice_choice
                else:
                    print("Please enter 1, 2, or 3.")
                    continue
        else:
            print("Please enter a valid input")
            continue
    quit        



def play_round(wins, losses):
    """Plays one complete round and returns a single string: 'win', 'loss', 'none', or 'quit'."""
    # Pseudocode:
    # 1. Initialize d1, d2, d3 = 0 and rolled flags = False.
    d1 = 0
    d2 = 0
    d3 = 0
    rolls = 0
    # 2. Repeat while less than 3 rolls have been made:
    while rolls != 2:
    #    a) Ask which die to roll using read_choice().
        read_choice()
    #    b) If 'q' → return 'quit'.
    #    c) Roll the chosen die using roll_die().
        roll_die(dice_choice=read_choice())
    #    d) Update the die value and mark as rolled.
        print(f"First die roll number: {roll_die}")
        
    #    e) Increase rolls_done by 1.
        rolls += 1
    #    f) Display the state using show_state().
        show_state()
    # 3. After all three dice are rolled, compute total.

    # 4. If total == TARGET → print win message, return 'win'.
    #    If total > TARGET → print loss message, return 'loss'.
    #    Else → print neither message, return 'none'.


def main():
    """Main program loop that runs the game until the user quits."""
    # Pseudocode:
    # 1. Print welcome message.
    print_welcome()
    # 2. Initialize wins and losses to 0.
    # 3. Loop forever:
    #    a) Play a round and store the result.
    #    b) If result == 'quit' → print final tallies and exit.
    #    c) If result == 'win' → increment wins.
    #       If result == 'loss' → increment losses.
    #    d) Print "Next round!" and continue.

# The below two lines must always be there from now on in all assignments, please dont delete it
# A python code file can be run just as a file or a Python file can be included into another file
# Like we do import math, you can also import your own file.
# The below tells to call main() function only when it is run as a individual file and not when imported.
# This is important because Codegrade will import your file and do some tests and for that we dont want the code in main() function to run.
if __name__ == '__main__':
    main()

main()
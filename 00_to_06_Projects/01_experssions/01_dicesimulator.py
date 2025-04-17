#Dice Simulator
#Simulate rolling two dice, three times.  Prints the results of each die roll.  This program is used to show how variable scope works.
# Import the random library which lets us simulate random things like dice!

import random
NUM_SIDES = 6 # Number of sides on the die

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)
    # This function simulates rolling two dice and prints the total of the two dice.
    # The variables die1 and die2 are local to this function.

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))
    # The variable die1 in main() is not affected by the die1 in roll_dice().
    # The variable die1 in main() is local to main() and is not affected by the die1 in roll_dice().
    
if __name__ == '__main__':
    main()


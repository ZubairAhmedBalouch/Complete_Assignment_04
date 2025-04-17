import random

#No of sides on each die to roll
Num_Sides:int = 6


def main():
    #Roll the dice and return the result
    die1:int = random.randint(1, Num_Sides)
    die2:int = random.randint(1, Num_Sides)
    
    #Get their total
    total:int = die1 + die2

    #Print out the results
    print("Dice have:", Num_Sides, "sides")
    print("First Die:", die1)
    print("Second Die:", die2)
    print("Total:", total)

if __name__ == "__main__":
    main()

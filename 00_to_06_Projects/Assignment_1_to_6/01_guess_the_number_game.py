import random

def main():
    sec_num = random.randint(1, 20)
    print(sec_num)  #  only for testing purposes
    guess_num = int(input("Guess a number between 1 and 20: "))

    while sec_num != guess_num:
        if guess_num < sec_num:
            print("You guessed too low.")
        else:
            print("You guessed too high.")
        
        print("___________") # print after every guess attempt
        
        guess_num = int(input("Enter a new guess: "))
        
    print(f"Congrats! The number was: {sec_num}")

if __name__ == '__main__':
    main()

import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for _ in range(N_NUMBERS):  # Repeat 10 times
        number = random.randint(MIN_VALUE, MAX_VALUE)  # Get a random number from 1 to 100
        print(number)

if __name__ == '__main__':
    main()
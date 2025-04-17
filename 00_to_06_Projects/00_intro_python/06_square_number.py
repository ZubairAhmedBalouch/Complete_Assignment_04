def main():
    print("This program calculates the square of a number.")
    num:str = input("Enter a number: ")
    num:int = int(num)
    square:int = num * num
    print(f"The square of {num} is: \033[1m\033[3m{square}\033[0m")

if __name__ == "__main__":
    main()

    # This program calculates the square of a number.
    # The square of a number is the number multiplied by itself.
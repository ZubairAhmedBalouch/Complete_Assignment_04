
def main():
    #Get the numbers we want to divide
    dividend:float = float(input("\033[1m\033[3mplease Enter an integer to be divided:\033[0m "))
    divisor:float = float(input("\033[1m\033[3mplease Enter an integer to divide by:\033[0m "))
    
    #Calculate the remainder of the division
    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)

    #Display the result to the user
    print("The result of this division is: " + str(quotient) + " with a remainder of: " + str(remainder))

if __name__ == "__main__":
    main()
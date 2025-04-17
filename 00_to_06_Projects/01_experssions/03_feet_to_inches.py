
INCHES_IN_FOOT = 12
def main():
    # Get the number of feet from the user
    feet:float = float(input("Enter the number of feet: "))

    # Convert feet to inches
    inches:float = feet * INCHES_IN_FOOT

    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == "__main__":
    main()

# The program converts feet to inches. It prompts the user to enter a number of feet, then calculates and displays the equivalent number of inches.
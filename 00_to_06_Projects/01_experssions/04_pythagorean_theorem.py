
import math

def main():
    #Get the two side lengths from the user and cast them to be numbers
    ab:float = float(input("\033[1mEnter the length of side AB:\033[0m "))
    ac:float = float(input("\033[1mEnter the length of side AC:\033[0m "))

    #Calculate the length of side BC using the Pythagorean theorem
    bc:float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

if __name__ == "__main__":
    main()

# The program calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem. It prompts the user to enter the lengths of the two other sides, then calculates and displays the length of the hypotenuse.
# The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.
# The formula is: c^2 = a^2 + b^2, where c is the length of the hypotenuse, and a and b are the lengths of the other two sides.


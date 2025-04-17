def main():
    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')  # Print all values on the same line

if __name__ == '__main__':
    main()

# The program will keep doubling the number until it is at least 100.S
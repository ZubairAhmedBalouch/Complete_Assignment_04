def mad_libs():
    print("Welcome to Mad Libs!")
    
    
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    
    # The Mad Libs story
    story = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}. " \
            f"One day, the {adjective2} {noun2} came to visit and they had an adventure!"
    
    
    print("\nHere's your Mad Libs story:\n")
    print(story)


if __name__ == "__main__":
    mad_libs()
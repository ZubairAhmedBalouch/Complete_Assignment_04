import random

def game():
    # Game options
    options = ["rock", "paper", "scissors"]

    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
game()





        



    
    
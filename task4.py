import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win! 🎉"
    else:
        computer_score += 1
        return "Computer wins! 🤖"

while True:
    # Get user choice
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please select rock, paper, or scissors.")
        continue

    # Generate computer choice
    computer_choice = random.choice(choices)

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Display score
    print(f"\nScore: You {user_score} - {computer_score} Computer")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break

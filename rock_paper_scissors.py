import random

def play_rps():
    """Plays a game of Rock, Paper, Scissors with the user."""

    # Define the possible choices for the game
    choices = ["rock", "paper", "scissors"]

    # Get the user's choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate the user's input
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Generate the computer's choice randomly
    computer_choice = random.choice(choices)

    # Display the choices made by the user and the computer
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Start the game
if __name__ == "__main__":
    play_rps()
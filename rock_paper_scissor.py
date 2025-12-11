import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "draw"

    winning_cases = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if winning_cases[player] == computer:
        return "player"
    else:
        return "computer"

def play_game():
    print("=== Rock Paper Scissors ===")

    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

        if player_choice == "quit":
            print("Thanks for playing!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            print("🎉 You win!\n")
        elif result == "computer":
            print("💀 Computer wins!\n")
        else:
            print("😐 It's a draw.\n")

if __name__ == "__main__":
    play_game()

# HOMEWQRK 2 GAME

# ROCK OPAPER SCISOR GAME:

# START

def validity_check(choice: str) -> int:
    choice = choice.lower()
    if choice == "rock":
        return 2
    elif choice == "scissors":
        return 1
    elif choice == "paper":
        return 0
    else:
        raise ValueError("illegal choice")


def check_winner(player1_choice: int, player2_choice: int) -> int:
    if player1_choice not in [0, 1, 2] or player2_choice not in [0, 1, 2]:
        raise ValueError("illegal game option")

    if player1_choice == player2_choice:
        return 0  # Tie
    elif (player1_choice == 2 and player2_choice == 1) or \
            (player1_choice == 1 and player2_choice == 0) or \
            (player1_choice == 0 and player2_choice == 2):
        return 1  # Player 1 wins
    else:
        return 2  # Player 2 wins


def game_play():
    print("Welcome to Rock, Paper, Scissors!")

    player1 = input("Player 1, please choose Rock, Paper, or Scissors: ")
    player2 = input("Player 2, please choose Rock, Paper, or Scissors: ")

    try:
        player1_choice = validity_check(player1)
        player2_choice = validity_check(player2)

        winner = check_winner(player1_choice, player2_choice)

        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    except ValueError as e:
        print(f"Error: {e}")

# END
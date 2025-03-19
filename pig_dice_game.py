from random import randint

def roll_dice() -> int:
    return randint(1, 6)

def play_turn(player: str) -> int:
    turn_score = 0

    print(f"{player}'s turn\n")

    while True:
        roll = roll_dice()
        print(f"You rolled a {roll}")

        if roll == 1:
            return 0
        
        turn_score += roll

        choice: str = input("Roll again? (y/n): ").lower()

        if choice != "y":
            return turn_score


def main() -> None:
    player_scores = { "Player 1": 0, "Player 2": 0 }

    is_game_over = False

    while not is_game_over:

        for player, _ in player_scores.items():

            turn_score = play_turn(player)

            player_scores[player] += turn_score

            print(f"\nYou scored {turn_score} points this turn.")
            print(f"Current scores: Player 1: {player_scores['Player 1']}, Player 2: {player_scores['Player 2']}\n")

            if player_scores[player] > 30:
                print(f"{player} won the game")
                is_game_over = True
                break

if __name__ == "__main__":
    main()

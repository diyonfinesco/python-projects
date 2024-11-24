grid = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]
count = 0
current_player = 'X'

def print_table():
    for out in grid:
        print("---+---+---")
        print(f" {out[0]} | {out[1]} | {out[2]}")
    print("---+---+---\n")

print_table()

def check_winner(player: str):
    winner = False
    for i in range(3):

        if grid[i][0] == player and grid[i][1] == player and grid[i][2] == player:
            winner =  True
    
        if grid[0][i] == player and grid[1][i] == player and grid[2][i] == player:
            winner =  True
        
    if (grid[0][0] == player and grid[1][1] == player and grid[2][2] == player) or (grid[2][0] == player and grid[1][1] == player and grid[0][2] == player):
        winner =  True
    
    if winner:
        print(f"Player {player} wins!")
    
    return winner

def check_input(num: str):
        if num not in ["0", "1", "2"]:
            print("Invalid Input!\n")
            return False

        return True

def main():
    while True:
        global count, current_player

        if count == 9:
            print("Board is full")
            break

        print(f"Player {current_player}'s turn")
        row = input("Enter row (0-2): ")

        if not check_input(row):
            continue

        column = input("Enter column (0-2): ")

        if not check_input(column):
            continue

        target = grid[int(row)][int(column)]

        if target != " ":
            print("This spot is already taken!\n")
            continue

        grid[int(row)][int(column)] = f"{current_player}"
        count += 1

        print_table()

        if check_winner(current_player):
            return

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()





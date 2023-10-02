import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Tic-Tac-Toe")
    print_board(board)

    while True:
        if current_player == "X":
            row, col = -1, -1

            while row not in range(3) or col not in range(3) or board[row][col] != " ":
                try:
                    row, col = map(int, input(f"Player {current_player}, enter row (0-2) and column (0-2): ").split())
                except ValueError:
                    pass
        else:
            print("Computer's turn (O)")
            row, col = computer_move(board)

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            if current_player == "X":
                print("Player X wins!")
            else:
                print("Computer (O) wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
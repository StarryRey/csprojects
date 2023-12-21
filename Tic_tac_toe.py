def print_board(board):
    for row in board:
        print(" |"
              " ".join(row))
        print("_" * 9)

def check_winner(board, player): # Check rows and columns

    for a in range(3):
        if all(board[a][b] == player for b in range(3)) or all(board[b][a]
                                                               == player for b in range(3)):
            return True

    # Check diagonals again
    if all(board[a] == player for a in range(3)) or all(board[a][2 - a]
                                                        == player for a in range(3)):
        return True

    return False

def is_board_fill(board):
    return all(board[a][b] != ' ' for a
               in range(3) for b in range(3))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    first_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {first_player}, fill the row (0, 1, or 2): "))
        col = int(input(f"Player {first_player}, fill the column (0, 1, or 2): "))

        if board[row][col] != ' ':
            print("Wrong move.Try another cell")
            continue

        board[row][col] = first_player

        if check_winner(board, first_player):
            print_board(board)
            print(f"Player {first_player} wins!")
            break

        if is_board_fill(board):
            print_board(board)
            print("It's a draw!")
            break

        first_player = 'O' if first_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()

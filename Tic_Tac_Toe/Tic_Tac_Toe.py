# Tic Tac Toe

board = [" " for _ in range(9)]


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (
            board[combination[0]] == player
            and board[combination[1]] == player
            and board[combination[2]] == player
        ):
            return True

    return False


def check_draw():
    return " " not in board


def play_game():
    current_player = "X"

    while True:
        display_board()

        print("Player", current_player, "turn")

        try:
            position = int(input("Enter position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position] != " ":
                print("That position is already taken.")
                continue

            board[position] = current_player

        except ValueError:
            print("Please enter a valid number.")
            continue

        if check_winner(current_player):
            display_board()
            print("Player", current_player, "wins!")
            break

        if check_draw():
            display_board()
            print("It's a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


play_game()
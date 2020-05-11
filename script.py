def new_board(n):
    board = [0] * n
    return board


def display(board, n):
    # Display numbers row
    for number in range(1, n + 1):
        print(number, end=' ')

    # Break line
    print()

    # Print the board
    for case in board:
        if case == 0:
            print(".", end=' ')
        elif case == 1:
            print("X", end=' ')
        elif case == -1:
            print("O", end=' ')
        else:
            print("Error: couldn't find type of case.")

    # Break line
    print()


def possible(board, n, i):
    if board[i - 1] == 0:
        return True
    else:
        return False


def select(board, n):
    number_is_invalid = True
    while number_is_invalid:
        number = int(input("Please enter a number between {} and {}: ".format(1, n)))
        valid_number = possible(board, n, number)

        if 0 < number <= n and valid_number:
            print(number, "is valid.")
            number_is_invalid = False
            return number
        else:
            print("This number is invalid")


def put(board, n, i):
    board[i - 1] = 1
    if i-1 == 0:
        board[i] = -1
    elif i-1 == n-1:
        board[i - 2] = -1
    else:
        try:
            board[i - 2] = -1
        except:
            print("Out of range")

        try:
            board[i] = -1
        except:
            print("Out of range.")


def again(board, n):
    if 0 not in board:
        return False
    else:
        return True


def switch_player(current_player):
    if current_player == "Player 1":
        return "Player 2"
    elif current_player == "Player 2":
        return "Player 1"


def dawson(n):
    # Options
    board_length = n

    board = new_board(board_length)
    can_play_game = again(board, board_length)
    current_player = "Player 1"

    # Show the board and ask the player to select a number
    print("It's {}'s turn !".format(current_player))
    display(board, board_length)
    number = select(board, board_length)
    put(board, board_length, number)
    current_player = switch_player(current_player)

    while can_play_game:
        display(board, board_length)
        print("It's {}'s turn !".format(current_player))
        number = select(board, board_length)
        put(board, board_length, number)
        can_play_game = again(board, board_length)
        if can_play_game is True:
            current_player = switch_player(current_player)

    print("Game is over ! {} won !".format(current_player))


if __name__ == '__main__':
    dawson(8)

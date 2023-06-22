import collections
import itertools

board = [[], [], []]


def main():
    """Main function for running the game"""
    default = "Game not finished"
    get_board()
    player = 0
    win = default
    while win == default:
        print_board()
        move = "F"
        while move != "ok":
            move = make_move(player)
            if move != "ok":
                print(move)
        win = get_winner()
        if win != default:
            print_board()
            print(win)
        player = not player


def make_move(player: bool) -> str:
    """Get input from the user, error check, and play the move on the board
    :param bool player: the boolean value for what player turn it is
    :return: error string statement or "ok" if no error
    """
    try:
        user_input = input()
        user_input = user_input.split(" ")
        x_val = int(user_input[0]) - 1
        y_val = int(user_input[1]) - 1
        if 2 < x_val or x_val < 0:
            return "Coordinates should be from 1 to 3!"
        elif 2 < y_val or y_val < 0:
            return "Coordinates should be from 1 to 3!"
        elif board[x_val][y_val] != " ":
            return "This cell is occupied!"
        else:
            if player:
                board[x_val][y_val] = "O"
            else:
                board[x_val][y_val] = "X"
            return "ok"
    except ValueError:
        return "You should enter numbers!"


def get_board() -> None:
    """Fill the board with empty spaces at the start of the game"""
    global board
    for line in range(3):
        for row in range(3):
            board[line].append(" ")
    return


def print_board() -> None:
    """Print the current state of the board list"""
    global board
    print("-" * 9)
    for line in board:
        line = "| " + " ".join(line) + " |"
        print(line)
    print("-" * 9)
    return


def get_winner() -> str:
    """Determine the current state of the game based on the board list values
    return: text string of current game state
    """
    global board
    x = ["X", "X", "X"]
    o = ["O", "O", "O"]
    x_win = 0
    o_win = 0
    counter = collections.Counter(itertools.chain(*board))
    for index in range(3):
        line = board[index]
        row = [board[0][index], board[1][index], board[2][index]]
        if line == x or row == x:
            x_win += 1
        elif line == o or row == o:
            o_win += 1
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[2][0], board[1][1], board[0][2]]
    if diag1 == x or diag2 == x:
        x_win += 1
    elif diag1 == o or diag2 == o:
        o_win += 1
    if (x_win and o_win) or ((counter["X"] - counter["O"]) >= 2) or ((counter["O"] - counter["X"]) >= 2):
        return "Impossible"
    elif x_win:
        return "X wins"
    elif o_win:
        return "O wins"
    elif counter[" "] == 0:
        return "Draw"
    elif (x_win and o_win) or ((counter["X"] - counter["O"]) >= 2) or ((counter["O"] - counter["X"]) >= 2):
        return "Impossible"
    else:
        return "Game not finished"


if __name__ == "__main__":
    main()

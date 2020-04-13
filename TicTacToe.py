# ---Global variables------


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"
        ]


class player():

    def __init__(self, name):
        self.name = name


X = player("X")
O = player("O")



def play_game():
    display_board()
    print(f'Welcome to Tic-Tac-Toe! X goes first.')

    game_still_going = False
    current_player = X

    while not game_still_going:

        # handle that turn --> add to board, redraw, change player
        handle_turn(current_player)
        # check to see if the game should continue based on
        # if there is a winner or tie or not
        game_still_going = check_is_game_over(current_player)
        #flip player depending on the turn
        flip_player(current_player)
        current_player = flip_player(current_player)



def display_board():
    global board
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")


def handle_turn(current_player):

    print(current_player.name + '\'s turn.')
    position = int(input(f'Choose a position (1-9) on the board: '))

    valid = False
    while not valid:
        # make sure input is valid (1-9)
        while position < 0 or position > 9:
            position = int(input(f'Please enter a number 1-9: '))

        position = position - 1
        #add postion to the board based on player
        if board[position] == '-':
            board[position] = current_player.name
            valid = True
        else:
            position = int(input(f"You can't go there. Go again. "))

    display_board()

def flip_player(current_player):
    #Switch player depending on current player
    if current_player == X:
        current_player = O
    else:
        current_player = X
    return current_player


def check_is_game_over(current_player):
    #Check if there is a winner and stop the game
    if check_winner(current_player):
        print(current_player.name + " won!")
        game_still_going = True
    #check if there is a tie and stop the game
    elif check_tie(current_player):
        game_still_going = True
    # if neither, keep playing
    else:
        game_still_going = False
    return game_still_going


def check_winner(current_player):
    # check if there is a winner by row, column, diagnol, or if not its a tie
    if check_rows(current_player):
        return check_rows(current_player)
    elif check_columns(current_player):
        return check_columns(current_player)
    elif check_diagnols(current_player):
        return check_diagnols(current_player)

def check_rows(current_player):
    #check if all the value match across a given row
    if board[0] == board[1] == board[2] == current_player.name:
        winner = current_player

    elif board[3] == board[4] == board[5] == current_player.name:
        winner = current_player

    elif board[6] == board[7] == board[8] == current_player.name:
        winner = current_player
    else:
        winner = None

    return winner

def check_columns(current_player):
    # check if all the value match across a given column
    if board[0] == board[3] == board[6] == current_player.name:
        winner = current_player

    elif board[1] == board[4] == board[7] == current_player.name:
        winner = current_player

    elif board[2] == board[5] == board[8] == current_player.name:
        winner = current_player
    else:
        winner = None

    return winner

def check_diagnols(current_player):
    # check if all the value match across a given diagnol
    if board[0] == board[4] == board[8] == current_player.name:
        winner = current_player

    elif board[2] == board[4] == board[6] == current_player.name:
        winner = current_player
    else:
        winner = None

    return winner

def check_tie(current_player):
    # check if all the spaces in the list are either X or O (not - )
    # check to see if there are now winners
    if "-" not in board:
        if not check_columns(current_player) \
                and not check_columns(current_player) \
                and not check_diagnols(current_player):
            print(f'Its a tie!')
            return True

play_game()

 

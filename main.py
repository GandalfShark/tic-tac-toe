# tic tac toe

import random
player_move = 999
# random value so that the loops in the function will trigger
past_moves = []
# hold past moves, they can be checked against move attempts
# you can not place an X or O in square already used, duh.
current_player = 'X'


def player_x_o():
    global current_player
    match current_player:
        case 'X':
            current_player = 'O'
            return
        case 'O':
            current_player = 'X'
            return
    # flip the X or O marker to the other one


def display_board():
    print(f"""
       *** TIC TAC TOE ***
    -------------------------
    |   {grid[0][0]}   |   {grid[0][1]}   |   {grid[0][2]}   |
    -------------------------
    |   {grid[1][0]}   |   {grid[1][1]}   |   {grid[1][2]}   |
    -------------------------
    |   {grid[2][0]}   |   {grid[2][1]}   |   {grid[2][2]}   |
    -------------------------
    """)


def enter_move():
    # TODO change to validate move function so it can be passed the computers move
    # global vars so that changes here are can be stored outside and recalled again
    global player_move
    global past_moves
    global grid
    global current_player
    player_move = 999  # reset so we don't get an infinite loop
    # asks the user to enter a move
    while player_move not in range(1, 10):
        print(f'    *** {current_player} ***')
        print(f'PAST MOVES = {past_moves}')
        try:
            player_move = int(input('Enter the grid number:\n> '))
        except ValueError:
            print('Input is not valid.')
            continue
        if player_move not in range(1, 10):
            print('Please enter number between 1 and 9.')
            continue
        if str(player_move) in past_moves:
            print('That square is occupied.')
            player_x_o()
            # flip X O value an extra time so that the player stays the same
            continue
        else:
            # checks the input, and updates the board according to the user's decision.
            match player_move:
                case 1:
                    grid[0][0] = current_player
                case 2:
                    grid[0][1] = current_player
                case 3:
                    grid[0][2] = current_player
                case 4:
                    grid[1][0] = current_player
                case 5:
                    grid[1][1] = current_player
                case 6:
                    grid[1][2] = current_player
                case 7:
                    grid[2][0] = current_player
                case 8:
                    grid[2][1] = current_player
                case 9:
                    grid[2][2] = current_player
                # TODO this is clunky, there must be a better way to code this
            past_moves += str(player_move)


def make_list_of_free_fields():
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass  # WHY? I know there is a reason for this; I don't get it


def victory_for():
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    def winner():
        print(f"""

                PLAYER {current_player} WINS!

                """)
    if grid[0][0] == current_player and grid[0][1] == current_player and grid[0][2] == current_player:
        winner()
        return True
    if grid[0][0] == current_player and grid[1][1] == current_player and grid[2][2] == current_player:
        winner()
        return True
    if grid[0][0] == current_player and grid[1][0] == current_player and grid[2][0] == current_player:
        winner()
        return True
    if grid[0][1] == current_player and grid[1][1] == current_player and grid[2][1] == current_player:
        winner()
        return True
    if grid[0][2] == current_player and grid[1][1] == current_player and grid[2][0] == current_player:
        winner()
        return True
    if grid[0][2] == current_player and grid[1][2] == current_player and grid[2][2] == current_player:
        winner()
        return True
    if grid[1][0] == current_player and grid[1][1] == current_player and grid[1][2] == current_player:
        winner()
        return True
    if grid[2][0] == current_player and grid[2][1] == current_player and grid[2][2] == current_player:
        winner()
        return True
    # TODO refactor above as two nested for loops - better way to do this
    # TODO the win lines are multiples of three where [a]+[b] = n and (n1 + n2 + n3) mod 3 = 0
    if len(past_moves) == 9:
        # check to see if all the squares are occupied
        print("""
    ~~ IT IS A DRAW. ~~
            """)
        return True
    else:
        pass

def draw_move():
    comp_move = (random.randrange(0, 9))+1
    return comp_move
    # give a random number to be used as the computers move.


grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
#        row0              row 1              row 2

while True:
    display_board()
    enter_move()
    if victory_for():
        break
    player_x_o()

print('THANKS FOR PLAYING.')
# TODO refactor for playing against computer

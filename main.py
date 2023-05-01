# tic tac toe -- needs to run in *nix based terminal to display color properly
import random
player_move = 999
# arbitrary value so that the loops in the get move function will trigger
past_moves = []
# hold past moves, they can be checked against move attempts
# you can not place an X or O in square already used, duh.
current_player = 'X'
# set player one as X
grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
#        row0              row 1              row 2
# building the grid for the game board
playing = True
# set playing as true so main loop will loop


def clear_the_grid():
    global grid, past_moves
    grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    past_moves = []


def player_flip_x_o():
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
       \033[0;33m*** TIC TAC TOE ***\033[0;32m
    -------------------------
    |   {grid[0][0]}   |   {grid[0][1]}   |   {grid[0][2]}   |
    -------------------------
    |   {grid[1][0]}   |   {grid[1][1]}   |   {grid[1][2]}   |
    -------------------------
    |   {grid[2][0]}   |   {grid[2][1]}   |   {grid[2][2]}   |
    -------------------------\033[00m
    """)


def enter_move():
    # global vars so that changes here are can be stored outside and recalled again
    global player_move, past_moves, grid, current_player
    player_move = 999
    # reset var so we don't get an infinite loop
    while player_move not in range(1, 10):
        print(f'    *** {current_player} ***')
        print(f'PAST MOVES = {past_moves}')
        make_list_of_free_fields()
        try:
            player_move = int(input('Enter the grid number:\n> '))
            # asks the user to enter a move
        except ValueError:
            print('Input is not valid.')
            continue
        if player_move not in range(1, 10):
            print('Please enter number between 1 and 9.')
            continue
        if str(player_move) in past_moves:
            print('That square is occupied.')
            player_flip_x_o()
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
                # Dictionary {1 : 'grid[0][0]', etc, etc} possible?
            past_moves += str(player_move)


def make_list_of_free_fields():
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] not in ['X', 'O']:
                possible_moves += grid[i][j]
    print(f'OPEN SQUARES = {possible_moves}')
    return possible_moves


def check_for_winning_player():
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
    # refactor above as two nested for loops <-  suggested by instructor as better way to do this
    # TODO the win lines are multiples of three where [a]+[b] = n and (n1 + n2 + n3) mod 3 = 0
    # get all the index values of current player and see if any 3 added up are dividable by 3
    # that might be a cleaner way to do this?

    if len(past_moves) == 9:
        # check to see if all the squares are occupied
        print("""
    ~~ IT IS A DRAW. ~~
            """)
        return True
    else:
        pass



def create_computer_move():
    make_list_of_free_fields()
    comp_move = (random.choice(make_list_of_free_fields()))
    print(f'computer has chosen {comp_move}.')
    return comp_move
    # give a random number to be used as the computers move.
    # TODO change code so computer looks for 2 in a row and blocks


def play_the_game():
    while True:
        display_board()
        enter_move()
        if check_for_winning_player():
            break
        player_flip_x_o()


# main loop #
while playing:
    play_the_game()
    again = 'XXX'
    while again not in ['y', 'n']:
        again = input('Play again? Y/N').lower().strip()
        if again == 'y':
            clear_the_grid()
            break
        if again == 'n':
            print('Goodbye.')
            quit()

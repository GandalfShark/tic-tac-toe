# tic tac toe

import random
player_move = 999
# random value so that the loops in the function will trigger
past_moves = []
# hold past moves, they can be checked against move attempts
# you can not place an X or O in square already used, duh.
current_player = 'X'

grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
#        row0              row 1              row 2
playing = True


def clear_the_grid():
    global grid
    grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


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
        make_list_of_free_fields()
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
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] not in ['X','Y']:
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



def create_computer_move():
    make_list_of_free_fields()
    comp_move = (random.choice(make_list_of_free_fields()))
    print(f'computer has chosen {comp_move}.')
    return comp_move
    # give a random number to be used as the computers move.


def play_the_game():
    while True:
        display_board()
        enter_move()
        if check_for_winning_player():
            break
        player_x_o()


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



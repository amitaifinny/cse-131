# 1. Name:
#      Amitai Finlayson
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json
import os


# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    if os.path.exists(filename):
        with open(filename, "r") as file:
            prev_board = json.load(file)
            return prev_board["board"]

    else:
        return blank_board["board"]

def save_board(filename, board):
    '''Save the current game to a file.'''
    board_to_save = {
        "board": board
    }
    with open(filename, "w") as file:
        json.dump(board_to_save, file)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0] or ' '} | {board[1] or ' '} | {board[2] or ' '}")
    print("---+---+---")
    print(f" {board[3] or ' '} | {board[4] or ' '} | {board[5] or ' '}")
    print("---+---+---")
    print(f" {board[6] or ' '} | {board[7] or ' '} | {board[8] or ' '}")
    print()


def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_counter = 0
    o_counter = 0
    for position in board:
        if position == X:
            x_counter += 1
        elif position == O:
            o_counter += 1
    if x_counter == o_counter + 1: 
        return False
    else:
        return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    
    while True:
        display_board(board)
        
        player_turn = is_x_turn(board)
        
        if player_turn:
            player_choice = input("X> ")
        else:
            player_choice = input("O> ")
        
        if player_choice == "q":
            return False

        elif not player_choice.isdigit():
            print("Invalid input, must be a number between 1-9 or type q to quit and save.")

        else:
            player_choice_int = int(player_choice)
            
            if player_choice_int > 9 or player_choice_int < 1:
                print("Invalid range of numbers, you must enter a number between 1 and 9.")
            
            else:
                player_choice_selection = player_choice_int - 1
                if board[player_choice_selection] == BLANK:
                    if player_turn:
                        board[player_choice_selection] = X
                    else:
                        board[player_choice_selection] = O
                    if game_done(board, message=True):
                        print("Game completed.")
                        return True
                else:
                    print("The square is already occupied, choose a different square.")
        
        

    
def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
filename = "tic-tac-toe.json"
board = read_board(filename)

gameplay = play_game(board)

if gameplay:
    if os.path.exists(filename):
        os.remove(filename)
else:
    save_board(filename, board)
    
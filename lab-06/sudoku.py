# 1. Name:
#      Amitai Finlayson
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This a rough draft, program of the Sudoku game.
# 4. What was the hardest part? Be as specific as possible.
#      The program went much better than lab 04. I was able to implement
#      most things with ease. I had already put considerable effort into
#      planning, so I really understood the direction of the program.
#      The hardest part of the program was implementing the display_board
#      function. It was a little tedious to get all of the formatting correct.
# 5. How long did it take for you to complete the assignment?
#      2.5 hours.


import json


def read_file(filename):
    """Read a Sudoku board from a JSON file and return it as a 2D list."""
    
    with open(filename, "r") as file:
        board_json = json.load(file)

    # Assign the key-value pair.
    board = board_json["board"]
    
    return board


def save_file(filename, board):
    """Save the Sudoku board to keep game progress."""

    board_json = {"board": board}
    with open(filename, "w") as file:
        json.dump(board_json, file, indent=2)

    
def display_board(board):
    """Display the current Sudoku board to the console."""

    # Display column headers.
    print("   A B C D E F G H I")

    # Loop through all nine rows.
    for row in range(9):

        # Print horizontal separators after rows 3 and 6.
        if row == 3 or row == 6:
            print("   -----+-----+-----")

        # Print the row number.
        print(f"{row + 1}  ", end="")

        # Loop through all nine columns.
        for col in range(9):

            # Print vertical separators after columns C and F.
            if col == 3 or col == 6:
                print("|", end="")

            # Retrieve the value at the current square.
            value = board[row][col]

            # Display blank spaces instead of zeros.
            if value == 0:
                print(" ", end="")
            else:
                print(value, end="")

            # Add spacing between numbers, except the ends of the 3 x 3.
            if col not in (2, 5, 8):
                print(" ", end="")
        
        print()


def get_user_move():
    """Prompt the user for a move."""
    
    move = input("\n> ").strip()

    return move


def get_value(coordinate):
    """Prompt the user for the value at the specific coordinate."""

    value = int(input(f"What is the value at '{coordinate}': "))

    return value


def convert_coordinates(coordinate) -> tuple[int, int]:
    """convert a coordinate such as 'B5' into a column,row such as (1,4)."""
    
    # Create list to map to number.
    column_map = ["A", "B", "C", "D","E", "F", "G", "H", "I"]

    # Find the match for the column and map number to it.
    for column in range(len(column_map)):
        if column_map[column] == coordinate[0]:
            column_num = column
    
    # Get the right coordinate number for the row.
    row_int = int(coordinate[1])
    row_num = row_int - 1
    
    coordinate_pair = (column_num, row_num)

    return coordinate_pair


def play_game(board):
    """Deligate game structure for playing the game."""

    # Game loop to keep going.
    while True:

        display_board(board)

        print("Specify a coordinate to edit or 'Q' to save and quit")
        
        move = get_user_move()

        if move.upper() == "Q":
            return 

        value = get_value(move)

        coordinate_pair = convert_coordinates(move)

        board[coordinate_pair[1]][coordinate_pair[0]] = value
    
    


def main():
    filename = input("Where is your board located? ")
    
    board = read_file(filename)
    
    play_game(board)

    save_file(filename, board)


if __name__ == "__main__":
    main()
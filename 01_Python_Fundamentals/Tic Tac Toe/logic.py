
# Import NumPy for working with arrays and matrix operations
import numpy as np


# Create a 3x3 board filled with zeros
# 0 = empty cell
# 1 = Player X
# -1 = Player O
board = np.zeros((3, 3), dtype=int)

# Display the initial empty board
print(board)


# Function to display the board in a user-friendly format
def print_board(b):

    # Dictionary to convert numbers into game symbols
    symbols = {
        0: " ",     # Empty cell
        1: "X",     # Player X
        -1: "O"     # Player O
    }

    # Loop through each row of the board
    for r in range(3):

        # Convert each number in the row into X, O, or blank
        # Then join them using "|"
        row = " | ".join(symbols[val] for val in b[r])

        # Print the row
        print(" " + row)

        # Print a separator after the first two rows
        if r < 2:
            print("---+---+---")

    # Add an empty line after the board
    print()


# Function to check whether X or O has won
def check_winner(b):

    # Calculate the sum of every row
    # X wins if a row contains [1, 1, 1] → sum = 3
    if 3 in np.sum(b, axis=1):

        # Calculate the sum of every column
        # If any column also has sum 3, X wins
        return 'X'

    # Check columns for X
    if 3 in np.sum(b, axis=0):
        return 'X'


    # Calculate row sums for O
    # O wins if a row contains [-1, -1, -1] → sum = -3
    if -3 in np.sum(b, axis=1):
        return 'O'

    # Check columns for O
    if -3 in np.sum(b, axis=0):
        return 'O'


    # np.trace() calculates the sum of the main diagonal
    #
    # Example:
    # X  O  -
    # -  X  O
    # O  -  X
    #
    # Main diagonal = X + X + X = 3
    if np.trace(b) == 3:
        return 'X'

    if np.trace(b) == -3:
        return 'O'


    # np.fliplr() flips the board from left to right
    # This allows us to check the opposite diagonal
    #
    # Example:
    # X  O  O
    # -  X  -
    # O  -  X
    #
    # Opposite diagonal = O + X + O
    if np.trace(np.fliplr(b)) == 3:
        return 'X'

    if np.trace(np.fliplr(b)) == -3:
        return 'O'


    # If there are no zeros left, the board is full
    # and nobody has won, so the game is a draw
    if not 0 in b:
        return "DRAW"


    # If nobody has won and the board is not full,
    # the game should continue
    return None


# 1 represents Player X
# -1 represents Player O
current = 1


# Display welcome message
print("Welcome to the game")


# Display the empty board
print_board(board)


# Continue the game until a winner or draw is found
while True:

    # Decide which player's turn it is
    if current == 1:
        player = 'X'
    else:
        player = 'O'


    # Try to take input from the player
    try:

        # Ask the player for row number
        row = int(input(f"{player} - enter row: "))

        # Ask the player for column number
        col = int(input(f"{player} - enter col: "))

    # If the user enters something that isn't a number
    except ValueError:

        print("Please enter numbers only\n")

        # Restart the loop
        continue


    # Check whether row and column are within 0 to 2
    if row < 0 or row > 2 or col < 0 or col > 2:

        print("Row and column must be between 0 and 2")

        # Don't continue with an invalid position
        continue


    # Check whether the selected cell is already occupied
    if board[row, col] != 0:

        print("Cell is already taken")

        # Ask the player to choose another cell
        continue


    # Put the current player's value into the selected cell
    #
    # X → 1
    # O → -1
    board[row, col] = current


    # Display the updated board
    print_board(board)


    # Check whether somebody has won or the game is a draw
    result = check_winner(board)


    # If result is not None, the game has ended
    if result is not None:

        # Check for a draw
        if result == "DRAW":
            print("Oh! It's a draw")

        # Otherwise, someone has won
        else:
            print(f"{result} wins")

        # Stop the game
        break


    # Switch players
    #
    # X (1) → O (-1)
    # O (-1) → X (1)
    if current == 1:
        current = -1
    else:
        current = 1


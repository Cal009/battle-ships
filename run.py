from random import randint
"""
Creating the game board as the main area
"""


class Board:
    """
    This code was sourced from Knowledge Mavens on Youtube"
    """
    def __init__(self):
        self.player_board = [[" "] * 8 for _ in range(8)]
        self.computer_board = [[" "] * 8 for _ in range(8)]
        self.player_guess_board = [[" "] * 8 for _ in range(8)]
        self.computer_guess_board = [[" "] * 8 for _ in range(8)]
        self.letters_to_numbers = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7
        }

    def print_board(self, board, board_name, player_name, show_ships=False):
        """
        This will print the board to the terminal
        """
        print(f"{board_name} - {player_name}")
        print("~" * 18)
        print("  A B C D E F G H")
        row_number = 1
        for i in range(8):
            row = board[i]
            if show_ships:
                row = [cell if cell == "X" else " " for cell in row]
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1
        print("~" * 18)

    def get_ship_location(self):
        """
        Allows for input of coordinates to place ships.
        Error codes in place for incorrect inputs
        """
        while True:
            try:
                row = input("\nEnter the grid row:\n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError("Valid numbers: 1-8")
            except ValueError as e:
                print(e)

        while True:
            try:
                column = input("\nEnter the grid column:\n").upper()
                if column and column in 'ABCDEFGH':
                    column = self.letters_to_numbers[column]
                    break
                else:
                    raise ValueError("Invalid input. Valid letters: A-H")
            except ValueError as e:
                print(e)

        return row, column

    def computer_create_ships(self, board):
        """
        This creates the ships for the computer and randomises the locations
        """
        for ship in range(5):
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            while board[ship_row][ship_column] == "X":
                ship_row, ship_column = self.get_ship_location()
            board[ship_row][ship_column] = "X"

    def player_create_ships(self, board, player_name):
        """
        This gives the user the ability to choose the locations
        of their ships on the board
        """
        for ship in range(5):
            self.print_board(board, player_name, "this is your board: ",
                             show_ships=True)
            ship_row, ship_column = self.get_ship_location()
            while board[ship_row][ship_column] == "X":
                print("\nThat location is already taken, choose another")
                ship_row, ship_column = self.get_ship_location()
            board[ship_row][ship_column] = "X"

    def count_hit_ships(self, board):
        """
        This will count each hit on a ship and increment the
        count number by 1 each time
        """
        count = 0
        for row in board:
            for column in row:
                if column == "X":
                    count += 1
        return count

    def play_game(self, player_name):
        """
        This initiates creating the ships and generating the boards
        """
        self.computer_create_ships(self.computer_board)
        self.player_create_ships(self.player_board, player_name)

        turn_count = 0
        moves_left = 15

        while True:
            """
            Creates loop checking for coorinatest given by player to
            check for if a ship is hit or not
            prints if already chosen before
            """
            if moves_left == 0:
                print("Game over! You have reached the maximum \
number of turns.")
                break

            self.print_board(self.player_guess_board, player_name,
                             "This is your board: ")
            self.print_board(self.computer_guess_board, "This board is",
                             "The Computer's board: ")

            while True:
                print("\nGuess a battleship location: ")
                row, column = self.get_ship_location()
                if self.player_guess_board[row][column] == "-":
                    print("\nYou guessed that one already.")
                elif self.computer_board[row][column] == "X":
                    print("^" * 30)
                    print("Hit!")
                    print("~" * 14)
                    self.player_guess_board[row][column] = "X"
                    break
                else:
                    print("^" * 30)
                    print("You Missed!")
                    print("~" * 14)
                    self.player_guess_board[row][column] = "-"
                    break

            if self.count_hit_ships(self.player_guess_board) == 5:
                print("Congratulations, you win!")
                break

            while True:
                """
                Creates loop to check for hit ships or not
                Credit to Knowledge Mavens, Youtube.
                """
                row, column = randint(0, 7), randint(0, 7)
                while self.computer_guess_board[row][column] == "-":
                    row, column = randint(0, 7), randint(0, 7)
                if self.player_board[row][column] == "X":
                    self.computer_guess_board[row][column] = "X"
                    break
                else:
                    self.computer_guess_board[row][column] = "-"
                    break

            if self.count_hit_ships(self.computer_guess_board) == 5:
                print("Unlucky the computer one.")
                break

            turn_count += 1
            moves_left -= 1

            print(f"Moves left: {moves_left}")
            print("~" * 14)


if __name__ == "__main__":
    """
    Multiple Strings for instructions and spacing
    """
    print("~" * 30)
    print("Welcome to Battleships")
    print("~" * 30)
    print("Your objective is to sink all 5 of your opponents ships")
    print("You must enter in grid coordinates at the requested time.")
    print("~" * 30)
    print("First you will have to choose where your ships \
go on the board")
    print("This can be done by choosing the row and column value")
    print("You will see two labelled boards. These will appear \
once your\nships are in place. After each attempt \
your choices will be saved onto your own board so you can see your\n \
previous attempts")
    print("If you miss it will show as '-' if you hit it will be 'X'")
    print("\nTo get started please enter your name below...\n")

    player_name = input("Enter your name:\n")

    while not player_name.isalpha():
        print("Invalid input. Should contain only alphabetical characters.")
        player_name = input("Enter your name:\n")

    game = Board()
    print("~" * 25)
    game.play_game(player_name)

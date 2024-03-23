from random import randint
"""
Creating the game board as the main area
"""
class Board:
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
        Thsi will print the board to the terminal
        """
        print(f"\n{board_name} - {player_name}")
        print("  A B C D E F G H")
        print("~" * 30)
        row_number = 1
        for i in range(8):
            row = board[i]
            if show_ships:
                row = [cell if cell == "X" else " " for cell in row]
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

    def get_ship_location(self):
        while True:
            try: 
                row = input("Enter the row of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between A-H')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = self.letters_to_numbers[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column
            
    def computer_create_ships(self, board):
        """
        This creates the ships for the computer and randomises the locations
        """
        for ship in range(5):
            ship_row, ship_column = randint(0,7), randint(0,7)
            while board[ship_row][ship_column] == "X":
                ship_row, ship_column = self.get_ship_location()
            board[ship_row][ship_column] = "X"

    def player_create_ships(self, board, player_name):
        """
        This gives the user the ability to choose the locations of their ships on the board
        """
        for ship in range(5):
            self.print_board(board, player_name, "this is your board: ", show_ships=True)
            ship_row, ship_column = self.get_ship_location()
            while board[ship_row][ship_column] == "X":
                print("That location is already taken, choose another")
                ship_row, ship_column = self.get_ship_location()
            board[ship_row][ship_column] = "X"

    def count_hit_ships(self, board):
        """
        This will count each hit on a ship and increment the count number by 1 each time
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

        while True:
            """
            Creates loop checking for coorinatest given by player to check for if
            a ship is hit or not
            prints if already chosen before
            """
            self.print_board(self.player_guess_board, player_name, "This is your board: ")
            self.print_board(self.computer_guess_board, "Computer Board", "Computer")

            while True:
                print("\nGuess a battleship location")
                row, column = self.get_ship_location()
                if self.player_guess_board[row][column] == "-":
                    print("You guessed that one already.")
                elif self.computer_board[row][column] == "X":
                    print("Hit!")
                    self.player_guess_board[row][column] = "X"
                    break
                else:
                    print("You Missed!")
                    self.player_guess_board[row][column] = "-"
                    break

            if self.count_hit_ships(self.player_guess_board) == 5:
                print("Congratulations, you win!")
                break

            while True:
                """
                Creates loop to check for hit ships or not
                """
                row, column = randint(0,7), randint(0,7)
                while self.computer_guess_board[row][column] == "-":
                    row, column = randint(0,7), randint(0,7)
                if self.player_board[row][column] == "X":
                    self.computer_guess_board[row][column] = "X"
                    break
                else:
                    self.computer_guess_board[row][column] = "-"
                    break

            if self.count_hit_ships(self.computer_guess_board) == 5:
                print("Unlucky the computer one.")
                break

if __name__ == "__main__":
    print("~" * 30)
    print("Welcome to Battleships")
    print("~" * 30)
    print("\nYour objective is to sink all 5 of your opponents ships")
    print("To do this you must enter in grid coordinates at the requested time.")
    print("To get started please enter your name below...\n")
    player_name = input("Enter your name: ")

    game = Board()
    game.play_game(player_name)

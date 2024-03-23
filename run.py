from random import randint
"""
Creating the game board as the main area
"""
class Board:
    def __init__(self):
        self.player_board = [[" "] * 8 for _ in range(8)]
        self.computer_board = [[" "] * 8 for _ in range(8)]
        self.player_guess = [[" "] * 8 for _ in range(8)]
        self.computer_guess = [[" "] * 8 for _ in range(8)]
        self.letters_to_numbers = {
            {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        }

    def print_board(self, board, board_name, player_name, show_ships=False):
        print(f"\n{board_name} - {player_name}")
        print(" A B C D E F G H")
        print("~" * 30)
        row_number = 1
        for i in range(8):
            row = board[i]
            if show_ships:
                row = [cell if cell == "X" else "" for cell in row]
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
                print("Enter a valid letter between 1-8")
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = self.letters_to_numbers[column]
                    break
            except KeyError:
                print("Enter a valid letter between A-H")
                return row, column
            
    def computer_create_ships(self, board):
        for ship in range(5):
            ship_row, ship_column = randint(0,7), randint(0,7)
            while board[ship_row][ship_column] == "X":
                ship_row, ship_column = self.get_ship_location()
                board[ship_row][ship_column] = "X"

    def player_create_ships(self, board, player_name):
        for ship in range(5):
            self.print_board(board, player_name, "this is your board: ", show_ships=True)
            ship_row,ship_column = self.get_ship_location()
            while board[ship_row][ship_column] == "X":
                print("That location is already taken, choose another")
                ship_row, ship_column = self.get_ship_location()
            board[ship_row][ship_column] = "X"
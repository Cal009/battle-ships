import random
"""
Creating the game board as the main area
"""
class GameBoard:
    def __init__(self,board):
        self.board = board

    def print_board(self):
        """
        This creates the board itself, putting in spacers in the board grid
        """
        print("  1 2 3 4 5 6 7 8")
        print("  ~~~~~~~~~~~~~~~")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Function to create the ships
        """
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "@":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] == "@"
            return self.board
        
    def get_user_input(self):
        """
        This creates the user input options and prevents incorrect values
        being entered
        """
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print("Not an appropriate choice, please select a valid row")
                x_row = input("Enter the row of he ship: ")

            y_column = input("Enter the column of the ship: ")
            while y_column not in '12345678':
                print("Not an appropriate choice, please choose a valid column")
                y_column = input("Enter the column of the ship: ")
            return int(x_row) -1, int(y_column)
        except ValueError:
            print("Not a valid input")
            return self.get_user_input()
        
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships
    
def run_game():
    computer_board = GameBoard([" " * 8 for i in range(8)])
    user_guess_board = GameBoard([" "] * 8 for i in range((8)))
    Battleship.create_ships(computer_board)
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)
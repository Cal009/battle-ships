from random import random
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
        

# class Battleship:
#     def __init__(self, board):
#         self.board = board

#     def create_ships(self):
#         for i in range(5):
#             self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
#             while self.board[self.x_row][self.y_column] == "X":
#                 self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
#             self.board[self.x_row][self.y_column] = "X"
#         return self.board
        
#     def get_user_input(self):
#         """
#         This creates the user input options and prevents incorrect values
#         being entered
#         """
#         try:
#             x_row = input("Enter the row of the ship: ")
#             while x_row not in '12345678':
#                 print("Not an appropriate choice, please select a valid row")
#                 x_row = input("Enter the row of he ship: ")

#             y_column = input("Enter the column letter of the ship: ").upper()
#             while y_column not in 'ABCDEFGH':
#                 print("Not an appropriate choice, please choose a valid column")
#                 y_column = input("Enter the column of the ship: ").upper()
#             return int(x_row) -1, GameBoard.get_letters_to_numbers()[y_column]
#         except ValueError and KeyError:
#             print("Not a valid input")
#             return self.get_user_input()
        
#     def count_hit_ships(self):
#         hit_ships = 0
#         for row in self.board:
#             for column in row:
#                 if column == "X":
#                     hit_ships += 1
#         return hit_ships
    
# def run_game():
#     computer_board = GameBoard([[" "] * 8 for i in range(8)])
#     user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
#     Battleship.create_ships(computer_board)
#     turns = 10
#     while turns > 0:
#         GameBoard.print_board(user_guess_board)
#         """ This will get the user input """
#         user_x_row, user_y_column = Battleship.get_user_input(object)
#         """ Then checks for any duplicate choices and prints necessary feedback to the user """
#         while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
#             print("You guessed that one already, choose again.")
#             user_x_row, user_y_column = Battleship.get_user_input(object)
#             """ This checks if its a hit or miss """
#             if computer_board.board[user_x_row][user_y_column] == "X":
#                 print("You hit one of my battlehips!")
#                 user_guess_board.board[user_x_row][user_y_column] = "X"
#             else:
#                 print("You missed my battlehip!")
#                 user_guess_board.board[user_x_row][user_y_column] = "-"
#             """ This checks for a win condition, if you win or lose """
#             if Battleship.count_hit_ships(user_guess_board) == 5:
#                 print("You hit all 5 battleships")
#                 break
#             else:
#                 turns -= 1
#                 print(f"You have {turns} turns remaining")
#                 if turns == 0:
#                     print("You ran out of turns!")
#                     GameBoard.print_board(user_guess_board)
#                     break

# if __name__ == '__main__':
#     run_game()
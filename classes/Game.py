from itertools import product
from classes.Board import Board
from classes.Piece import Piece
from classes.Player import Player
import numpy as np


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player1: Player = Player("X", "Light")
        self.player2: Player = Player("O", "Dark")

        self._init_pieces()


    def _generate_pieces(self):
        attributes = [True, False]
        self.all_pieces = [Piece(tall, dark, solid, square) for tall, dark, solid, square in product(attributes, repeat=4)]


    def _dark_pieces(self) -> None:
        self.dark_set = [piece for piece in self.all_pieces if piece.dark == True]

    def _light_pieces(self) -> None:
        self.light_set = [piece for piece in self.all_pieces if piece.dark == False]

    def _init_pieces(self) -> None:
        self._generate_pieces()
        self._dark_pieces()
        self._light_pieces()


    def _select_piece(self, pieces: list[Piece]) -> Piece:
        # check if piece is valid try, add the color there
        #Select pieces from list
        print("Available pieces:")
        for index, piece in enumerate(pieces):
            print(f"{index}.")
            print(piece)

        while True:
            user_input = input("Enter a one-digit number (0–7): ")
            if user_input in "01234567":
                piece_number = int(user_input)
                print(f"You entered: {piece_number}")
                break
            else:
                print("Invalid input. Try again.")

        return pieces[piece_number]

    @staticmethod
    def letter_to_int(letter):
        return ord(letter.upper()) - ord('A')

    def place_piece(self, piece: Piece) -> tuple[int, int]:
        # check if move is legal, if not report to player try again
        # Check if winning
        placed = False
        while not placed:
            try:
                place = input("Where do you want to place the piece? e.g. [A1]")
                if len(place) != 2:
                    raise ValueError("Invalid input. Try somthing like 'A1'. ")

                col = place[0]
                col_int = self.letter_to_int(col)
                row = int(place[1])
                if row > 3:
                    raise ValueError("Invalid input. Row number higher than 3. ")
                if col_int > 3:
                    raise ValueError("Invalid input. Column number higher than D. ")

                if self.board[row, col_int] is None:
                    self.board[row, col_int] = piece
                    placed = True
                else:
                    print("This cell is already occupied. Try again.")
                    continue
            except (IndexError, ValueError) as e:
                print(f"Error occurred: {e}")

        # maybe check first if it is in the dark set
        if piece.dark:
            self.dark_set.remove(piece)
        else:
            self.light_set.remove(piece)
        return row, col_int

    def _scan_property_column(self, property_line) -> bool:
        property_line = np.array(property_line)
        for col in range(4):
            if np.all(property_line[:,col]) or not np.any(property_line[:,col]):
                return True
        return False

    def _check_win_condition(self, row, col) -> bool:
        # row
        row_line = []
        if None not in self.board[row, :]:
            for piece in self.board[row, :]:
                row_line.append(piece.properties)
            if self._scan_property_column(row_line):
                return True

        # col
        col_line = []
        if None not in self.board[:, col]:
            for piece in self.board[:, col]:
                col_line.append(piece.properties)
            if self._scan_property_column(col_line):
                return True

        # main diagonal
        main_diagonal=[]
        counter_diagonal=[]
        if None not in [self.board[i, i] for i in range(4)]:
            if row == col:
                for i in range(4):
                    main_diagonal.append(self.board[i,i].properties)
                if self._scan_property_column(main_diagonal):
                    return True

        if None not in [self.board[i, 3-i] for i in range(4)]:
            if row+col == 3:
                for i in range(4):
                    counter_diagonal.append(self.board[i, 3-i].properties)
            if self._scan_property_column(counter_diagonal):
                return True
        return False



    def player_switch(self, current_player: Player) -> Player | None:
        if current_player == self.player1:
            return self.player2
        elif current_player == self.player2:
            return self.player1

    def select_current_player_set(self, player):
        if player == self.player1:
            return self.light_set
        elif player == self.player2:
            return self.dark_set
        else:
            raise ValueError(f"Player {player.player_name} has no pieces") #this should never happen


    def turn(self, player: Player) -> bool:
        print(f"{player.player_name}'s turn")
        print(self.board)

        pieces = self.select_current_player_set(player)

        on_turn = True
        try:
            while on_turn:
                selected_piece: Piece = self._select_piece(pieces)
                row, col = self.place_piece(selected_piece)
                if self._check_win_condition(row, col):
                    return True
                on_turn = False
        except ValueError:
                print("please enter a valid piece")
        return False

    # starts and runs the actual game
    def run(self):
        game_running: bool = True
        current_player: Player = self.player1
        while game_running:
            if self.turn(current_player):
                print(f"{current_player.player_name} won!")
                print(self.board)
                game_running = False
                break
            current_player = self.player_switch(current_player)



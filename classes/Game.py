from itertools import product
from classes.Board import Board
from classes.Piece import Piece
from classes.Player import Player


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player1: Player = Player("X", "Light")
        self.player2: Player = Player("O", "Dark")

        self._init_pieces()

        #TODO make tuple for easier programming access
        self.trait_map = {
            'T': True,
            'Sh': False,
            'D': True,
            'L': False,
            'So': True,
            'H': False,
            'Sq': True,
            'R': False,
        }


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

    def parse_piece(self, piece: Piece):
        pass

    def search_piece(self, piece: Piece):
        pass

    # TODO change logic: print list of pieces and let the user input a number!!!
    def _select_piece(self, pieces: list[Piece]) -> Piece:
        # check if piece is valid try, add the color there
        #Select pieces from list
        print("Available pieces:")
        for index, piece in enumerate(pieces):
            print(f"{index}.")
            piece.emoji_print()

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

    def place_piece(self, piece: Piece) -> None:
        # check if move is legal, if not report to player try again
        # Check if winning
        #TODO make this its own function and place it below in the clause
        place = input("Where do you want to place the piece? e.g. [A1]")
        col = place[0]
        col_int = self.letter_to_int(col)
        row = int(place[1])

        placed = False
        while not placed:
            if self.board[row, col_int] is not None:
                self.board[row, col] = piece
                placed = False
            else:
                print("Invalid input. Try again.")

        # maybe check first if it is in the dark set
        if piece.dark:
            self.dark_set.remove(piece)
        else:
            self.light_set.remove(piece)





        #Also delete piece from list


    def player_switch(self, current_player: Player) -> Player:
        if current_player == self.player1:
            return self.player2
        elif current_player == self.player2:
            return self.player1


    def turn(self, player: Player) -> None:
        print(f"{player.player_name}'s turn")
        print(self.board)

        # select the correct player's set
        if player == self.player1:
            pieces = self.light_set
        elif player == self.player2:
            pieces = self.dark_set
        else:
            raise ValueError(f"Player {player.player_name} has no pieces") #this should never happen
        try:
            selected_piece: Piece = self._select_piece(pieces)
            self.place_piece(selected_piece)

        except ValueError:
                print("please enter a valid piece")

    # starts and runs the actual game
    def run(self):
        game_running: bool = True
        current_player: Player = self.player1
        while game_running:
            self.turn(current_player)
            current_player = self.player_switch(current_player)



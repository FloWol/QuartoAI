from itertools import product
from classes.Board import Board
from classes.Piece import Piece
from classes.Player import Player


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player1: Player = Player("X", "Light")
        self.player2: Player = Player("O", "Dark")

        self.init_pieces()

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


    def generate_pieces(self):
        attributes = [True, False]
        self.all_pieces = [Piece(tall, dark, solid, square) for tall, dark, solid, square in product(attributes, repeat=4)]


    def dark_pieces(self) -> None:
        self.dark_set = [piece for piece in self.all_pieces if piece.dark == True]

    def light_pieces(self) -> None:
        self.light_set = [piece for piece in self.all_pieces if piece.dark == False]

    def init_pieces(self) -> None:
        self.generate_pieces()
        self.dark_pieces()
        self.light_pieces()

    def parse_piece(self, piece: Piece):
        pass

    def search_piece(self, piece: Piece):
        pass

    # TODO change logic: print list of pieces and let the user input a number!!!
    def select_piece(self, pieces: list[Piece]) -> Piece:
        # check if piece is valid try, add the color there
        #Select pieces from list
        print("Available pieces:")
        for piece in pieces:
            piece.emoji_print()
        piece_string = input("Please enter a piece [e.g. T Sh So]: ")
        piece_attr = piece_string.strip().split()
        #for attr in piece_attr:


        #piece_string.split()


        pass

    def place_piece(self, piece: Piece) -> None:
        # check if move is legal, if not report to player try again
        # Check if winning
        pass

    def player_switch(self, current_player: Player) -> Player:
        if current_player == self.player1:
            return self.player2
        elif current_player == self.player2:
            return self.player1


    def turn(self, player: Player) -> None:
        print(f"{player.player_name}'s turn")

        # select the correct player's set
        if player == self.player1:
            pieces = self.light_set
        elif player == self.player2:
            pieces = self.dark_set
        else:
            raise ValueError(f"Player {player.player_name} has no pieces") #this should never happen
        try:
            select_piece: Piece = self.select_piece(pieces)
            self.place_piece(select_piece)

        except ValueError:
                print("please enter a valid piece")

    # starts and runs the actual game
    def run(self):
        game_running: bool = True
        current_player: Player = self.player1
        while game_running:
            self.turn(current_player)
            current_player = self.player_switch(current_player)



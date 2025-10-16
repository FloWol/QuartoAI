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

    def place_piece(self, piece: Piece) -> None:
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





        #Also delete piece from list


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


    def turn(self, player: Player) -> None:
        print(f"{player.player_name}'s turn")
        print(self.board)

        pieces = self.select_current_player_set(player)

        on_turn = True
        try:
            while on_turn:
                selected_piece: Piece = self._select_piece(pieces)
                self.place_piece(selected_piece)
                on_turn = False
        except ValueError:
                print("please enter a valid piece")

    # starts and runs the actual game
    def run(self):
        game_running: bool = True
        current_player: Player = self.player1
        while game_running:
            self.turn(current_player)
            current_player = self.player_switch(current_player)



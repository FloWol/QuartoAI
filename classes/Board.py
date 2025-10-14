from classes.Piece import Piece
import numpy as np

class Board:
    def __init__(self):
        self.board_array = np.full((4, 4), None, dtype=object)


    def __getitem__(self, indces):
        row, col = indces
        return self.board_array[row, col]
    def __setitem__(self, indces, value):
        row, col = indces
        self.board_array[row, col] = value


    def __str__(self): #TODO pretty print of the board
        lines = []
        for index, row in enumerate(self.board_array):
            line = ""
            for piece in row:
                if piece is not None: #or rather of dType piece i suppose
                    line += piece.emoji_print()
                else:
                    line += "O"
                line += " | "
            line += "\n"
            lines.append(line)
        return "\n".join(lines)



from classes.Piece import Piece
import numpy as np

class Board:
    def __init__(self):
        board_array = np.empty((4, 4), dtype=Piece)

    def __str__(self): #TODO pretty print of the board
        pass

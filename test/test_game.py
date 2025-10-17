from classes.Game import Game
from classes.Piece import Piece

def test_win_condition_row() -> None:
    game = Game()
    piece = Piece(True, False, True, False)
    for col in range(4):
        game.board[0, col] = piece
    assert game._check_win_condition(0,0), 'Win is not registered'

def test_win_condition_col() -> None:
    game = Game()
    piece = Piece(True, False, True, False)
    for row in range(4):
        game.board[row, 0] = piece
    assert game._check_win_condition(0,0), 'Win is not registered'

def test_win_condition_main_diag() -> None:
    game = Game()
    piece = Piece(True, False, True, False)
    for i in range(4):
        game.board[i, i] = piece
    assert game._check_win_condition(0,0), 'Win is not registered'

def test_win_condition_counter_diag() -> None:
    game = Game()
    piece = Piece(True, False, True, False)
    for i in range(4):
        game.board[i, 3-i] = piece
    assert game._check_win_condition(0,3), 'Win is not registered'
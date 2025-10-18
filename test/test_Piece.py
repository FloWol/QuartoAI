from classes.Piece import Piece

def test_piece() -> None:
    piece = Piece(True, True, True, True)
    assert piece.tall == True
    assert piece.dark == True
    assert piece.solid == True
    assert piece.square == True

def test_piece_str() -> None:
    piece = Piece(True, False, False, True)
    assert str(piece) == '⬜️THol'

def test_piece_emoji_print() -> None:
    piece = Piece(True, True, True, True)
    assert piece.emoji_print() == '⬛TSol'

def test_piece_property() -> None:
    piece = Piece(True, False, False, True)
    assert piece.properties == [True, False, False, True]
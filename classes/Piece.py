from dataclasses import dataclass

@dataclass(frozen=True)
class Piece:
    """Represents a single Quarto piece with four binary attributes.

    Attributes:
        tall (bool): True if tall, False if short.
        dark (bool): True if dark-colored, False if light.
        solid (bool): True if solid, False if hollow.
        square (bool): True if square, False if round.
    """

    tall: bool
    dark: bool
    solid: bool
    square: bool

    @property
    def properties(self) -> list[bool]:
        """ Returns a list of the pieces properties. """
        return [self.tall, self.dark, self.solid, self.square]

    def __str__(self) -> str:
        """Return a short emoji representation of the piece."""
        # Determine color/shape symbol
        if self.square:
            symbol = "⬛" if self.dark else "⬜️"
        else:
            symbol = "⚫" if self.dark else "⚪"

        # Height and solidity
        height = "T" if self.tall else "S"
        fill = "Sol" if self.solid else "Hol"

        return f"{symbol}{height}{fill}"

    emoji_print = __str__





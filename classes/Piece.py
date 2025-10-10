class Piece:
    def __init__(self, tall, dark, solid, square) -> None:
        self.tall: bool = tall
        self.dark: bool = dark
        self.solid: bool = solid
        self.square: bool = square

    def __str__(self) -> str:
        return f"{'Tall' if self.tall else 'Short'}, " \
        f"{'Dark' if self.dark else 'Light'}, " \
        f"{'Solid' if self.solid else 'Hollow'}, " \
        f"{'Square' if self.square else 'Round'}"

    def emoji_print(self) -> str:
        return f"{'⬛' if self.square and self.dark else '⬜️' if self.square else '⚫' if self.dark else '⚪'}" \
                f"{'T' if self.tall else 'S'}" \
                f"{'Sol' if self.solid else 'Hol'}"




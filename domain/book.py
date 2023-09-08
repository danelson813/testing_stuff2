# domain/book.py


class Book:
    def __init__(
        self,
        id: str,
        title: str,
        price: float,
    ):
        self.id = id
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.id} - " f"{self.title}: $" f"{self.price}.\n"

class BookTheme:
    def __init__(self, isbn_book : str, id_theme : int):
        """
        BookTheme class represents the relationship between a book and a theme.
        It contains the ISBN of the book and the ID of the theme.
        Args:
            isbn_book (str): ISBN of the book.
            id_theme (int): ID of the theme.
        """
        self.isbn_book = isbn_book
        self.id_theme = id_theme
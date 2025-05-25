from datetime import datetime
from repositories.models import Author, Theme

class BookDTO:
    """
    Class representing a book.
    Using datetime for the date in the class.

    This class uses the theme class and the author class.
    """
    def __init__(self, isbn : str, title : str, date : datetime, authors : list[Author], themes : list[Theme], price : float):
        """
        Initializes a new book instance.
        The unique identifier is the 'isbn' value specific to the book sector.

        Args:
            isbn (str): The ISBN of the book.
            title (str): The title of the book.
            date (datetime): The publication date of the book.
            authors (list): A list of authors of the book.
            themes (list): A list of themes associated with the book.
            price (float): The price of the book.
        """
        self.isbn = isbn
        self.title = title
        self.date = date
        self.authors = authors
        self.themes = themes
        self.price = price

    def __str__(self):
        return f"""
        isbn : {self.isbn}
        title : {self.title}
        date : {self.date}
        price : {self.price}
        authors : {[author.__dict__ for author in self.authors]}
        themes : {[theme.__dict__ for theme in self.themes]}
        """
        
    
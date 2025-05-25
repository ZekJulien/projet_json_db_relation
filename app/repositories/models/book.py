from datetime import datetime

class Book:
    """
    Class representing a book.
    Using datetime for the date in the class.

    This class uses the theme class and the author class.
    """
    def __init__(self, isbn : str, title : str, date : datetime, price : float):
        """
        Initializes a new book instance.
        The unique identifier is the 'isbn' value specific to the book sector.

        Args:
            isbn (str): The ISBN of the book.
            title (str): The title of the book.
            date (datetime): The publication date of the book.
            price (float): The price of the book.
        """
        self.isbn = isbn
        self.title = title
        self.date = date
        self.price = price
        
        
    
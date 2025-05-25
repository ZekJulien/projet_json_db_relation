#Lib
import pathlib
from datetime import datetime
#Project
##Models
from .models import Book
##Tools
from .tools import JsonStorage


class BookRepository:
    """
    Service class for managing books.
    Handles loading, saving, and adding books to a JSON file.
    """
    PATH_BOOK_DB = pathlib.Path(__file__).parent.parent.parent / "database" / "book.json"

    def __init__(self):
        """
        Initializes the BookService instance.
        Loads the book data from the JSON file if it exists.
        If the file doesn't exist, it initializes an empty list of books.
        """
        self._book_db : list[Book] = JsonStorage.load_all(self.PATH_BOOK_DB)
    
    def _save_all(self):
        """
        Saves the list of books to the JSON file.
        If the file doesn't exist, it creates a new one.
        """
        JsonStorage.save_all(self.PATH_BOOK_DB, self._book_db)     

    def get_all(self) -> list[Book]:
        """
        Returns the list of all books.
        """
        return self._book_db
    
    def check_is_isbn_exist(self, isbn : str) -> bool:
        """
        Checks if a book with the given ISBN exists in the list of books.
        
        Args:
            ISBN (str): The ISBN of the book to check.
        
        Returns:
            bool: True if the book exists, False otherwise.
        """
        return any(book.isbn == isbn for book in self._book_db)
     
    def add_book(self, isbn : str, title : str, date : datetime, price : float):
        """
        Adds a new book to the list of books and saves the updated list to the JSON file.
        """
        self._book_db.append(Book(isbn, title, date, price))
        self._save_all()
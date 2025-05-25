#Lib
import pathlib
#Project
#Models
from .models import BookAuthor, Author
from repositories import AuthorRepository
##Tools
from .tools import JsonStorage

class BookAuthorRepository:

    PATH_BOOK_AUTHOR_DB = pathlib.Path(__file__).parent.parent.parent / "database" / "book_author.json"

    def __init__(self):
        self._book_author_db : list[BookAuthor] = self._load_all()
        self._author_repository : AuthorRepository = AuthorRepository()

    def _save_all(self):
        """
        Saves the list of themes to the JSON file.
        If the file doesn't exist, it creates a new one.
        """
        JsonStorage.save_all(self.PATH_BOOK_AUTHOR_DB, self._book_author_db)

    def _load_all(self):
        return JsonStorage.load_all(self.PATH_BOOK_AUTHOR_DB)    

    def get_all(self) -> list[BookAuthor]:
        """
        Returns the list of all BookAuthor.
        """
        return self._book_author_db
     
    def add_book_author(self, isbn : str, id_author : int):
        self._book_author_db.append(BookAuthor(isbn, id_author))
        self._save_all()
    
    def get_authors_by_isbn(self, isbn) -> list[Author]:
        data : list[Author] = []
        for book_author in self._book_author_db:
            if book_author.isbn_book == isbn:
                data.append(self._author_repository.get_by_id(book_author.id_author))
        return data
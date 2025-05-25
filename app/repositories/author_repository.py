#Lib
import pathlib
#Models
from .models import Author
##Tools
from .tools import JsonStorage


class AuthorRepository:
    """
    Service class for managing authors.
    Handles loading, saving, and adding authors to a JSON file.
    """
    PATH_AUTHOR_DB = pathlib.Path(__file__).parent.parent.parent / "database" / "author.json"

    def __init__(self):
        """
        Initializes the authorService instance.
        Loads the author data from the JSON file if it exists.
        If the file doesn't exist, it initializes an empty list of authors.
        """
        self._author_db : list[Author] = JsonStorage.load_all(self.PATH_AUTHOR_DB)

    def _save_all(self):
        JsonStorage.save_all(self.PATH_AUTHOR_DB, self._author_db)
    
    def get_all(self) -> list[Author]:
        """
        Returns the list of all authors.
        """
        return self._author_db
    
    def check_is_author_exist(self, full_name : str) -> bool:
        """
        Checks if an author with the given fullName exists in the list of authors.
        
        Args:
            full_name (str): The full_name of the author to check.
        
        Returns:
            bool: True if the author exists, False otherwise.
        """
        if self._author_db:
            return any(author.full_name == full_name for author in self._author_db)
        return False
     
    def add_author(self, full_name : str):
        """
        Adds a new author to the list of authors and saves the updated list to the JSON file.
        Automatically assigns a unique ID to the new author.
        """
        self._author_db.append(Author(id=None, full_name=full_name))
        self._save_all()

    def get_by_id(self, id : int) -> Author:
        for author in self._author_db:
            if author.id == id:
                return author
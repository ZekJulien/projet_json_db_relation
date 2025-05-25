#Lib
import pathlib
#Project
#Models
from .models import BookTheme, Theme
##Tools
from .tools import JsonStorage
from repositories import ThemeRepository

class BookThemeRepository:

    PATH_BOOK_THEME_DB = pathlib.Path(__file__).parent.parent.parent / "database" / "book_theme.json"

    def __init__(self):
        self._book_theme_db : list[BookTheme] = self._load_all()
        self._theme_repository : ThemeRepository = ThemeRepository()

    def _save_all(self):
        """
        Saves the list of themes to the JSON file.
        If the file doesn't exist, it creates a new one.
        """
        JsonStorage.save_all(self.PATH_BOOK_THEME_DB, self._book_theme_db)  

    def _load_all(self):
        return JsonStorage.load_all(self.PATH_BOOK_THEME_DB) 

    def get_all(self) -> list[BookTheme]:
        """
        Returns the list of all BookAuthor.
        """
        return self._book_theme_db
     
    def add_book_theme(self, isbn : str, id_theme : int):
        try:
            self._book_theme_db.append(BookTheme(isbn, id_theme))
            self._save_all()
        except ValueError as e:
            print(f"Erreur lors de l'ajout du thème : {e}")

    def get_themes_by_isbn(self, isbn : str) -> list[Theme]:
        data : list[Theme] = []
        for book_theme in self._book_theme_db:
            if book_theme.isbn_book == isbn:
                data.append(self._theme_repository.get_by_id(book_theme.id_theme))
        return data
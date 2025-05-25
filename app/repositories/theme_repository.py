#Lib
import pathlib, os
#Project
#Models
from .models import Theme
##Tools
from .tools import JsonStorage


class ThemeRepository:
    """
    Service class for managing themes.
    Handles loading, saving, and adding themes to a JSON file.
    """
    PATH_THEME_DB = pathlib.Path(__file__).parent.parent.parent / "database" / "theme.json"

    def __init__(self):
        """
        Initializes the ThemeService instance.
        Loads the theme data from the JSON file if it exists.
        If the file doesn't exist, it initializes an empty list of themes.
        """
        self._theme_db : list[Theme] = JsonStorage.load_all(self.PATH_THEME_DB)
    
    def _save_all(self):
        """
        Saves the list of themes to the JSON file.
        If the file doesn't exist, it creates a new one.
        """
        JsonStorage.save_all(self.PATH_THEME_DB, self._theme_db)
             

    def get_all(self) -> list[Theme]:
        """
        Returns the list of all themes.
        """
        return self._theme_db
    
    def check_is_theme_exist(self, name : str) -> bool:
        """
        Checks if a theme with the given name exists in the list of themes.
        
        Args:
            name (str): The name of the theme to check.
        
        Returns:
            bool: True if the theme exists, False otherwise.
        """
        if self._theme_db:
            return any(theme.name == name for theme in self._theme_db)
        return False
     
    def add_theme(self, name : str):
        self._theme_db.append(Theme(None, name))
        self._save_all()

    def get_by_id(self, id : int):
        for theme in self._theme_db:
            if theme.id == id:
                return theme
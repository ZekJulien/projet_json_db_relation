from repositories import ThemeRepository

class ThemeService:
    def __init__(self):
        self._theme_repository = ThemeRepository()

    def add_theme(self, name : str):
        """
        Adds a new theme to the list of themes and saves the updated list to the JSON file.
        Automatically assigns a unique ID to the new theme.
        """
        try:
            if not self._theme_repository.check_is_theme_exist(name):
                self._theme_repository.add_theme(name)
            else:
                raise ValueError("Le thème existe déjà.")      
        except ValueError as e:
            print(f"Erreur lors de l'ajout du thème : {e}")

    def get_all(self):
        return self._theme_repository.get_all()
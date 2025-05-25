from repositories import AuthorRepository

class AuthorService:
    def __init__(self):
        self._author_repository = AuthorRepository()

    def add_author(self, full_name : str):
        """
        Adds a new author to the list of authors and saves the updated list to the JSON file.
        Automatically assigns a unique ID to the new author.
        """
        try:
            if not self._author_repository.check_is_author_exist(full_name):
                self._author_repository.add_author(full_name)
            else:
                raise ValueError("L'auteur existe déjà.")      
        except ValueError as e:
            print(f"Erreur lors de l'ajout de l'auteur : {e}")

    def get_all(self):
        return self._author_repository.get_all()

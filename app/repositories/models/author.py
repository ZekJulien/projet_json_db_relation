import itertools
from .base import Base

class Author(Base):
    """
    Class representing an author.
    Contains information about the author's name.

    An instance of this class can be associated with one or more Book objects.
    """
    _id_iter = itertools.count(1)

    def __init__(self, full_name : str, id : int = None):
        """
        Initializes a new author instance.
        Assigns a unique ID automatically if 'id' is None.
        
        Args:
            idAuthor (int | None): Unique identifier for the author.
            fullName (str): Full name of the author.
        """
        super().__init__(id)
        self.full_name = full_name

import itertools
from .base import Base

class Theme(Base):
    """
    Class representing a theme.
    Contains information about the theme's name.
    """

    def __init__(self, id : int | None, name : str):
        """
        Initializes a new theme instance.
        Assigns a unique ID automatically if 'id' is None.

        Args:
            id (int): Unique identifier for the theme.
            name (str): Name of the theme.
        """
        super().__init__(id)
        self.name = name
from datetime import datetime
from repositories import BookRepository, BookAuthorRepository, BookThemeRepository
from repositories.models import Author, Theme, Book
from .models import BookDTO

class BookService:
    def __init__(self):
        self._book_repository = BookRepository()
        self._book_author_repository = BookAuthorRepository()
        self._book_theme_repository = BookThemeRepository()

    def add_book(self, isbn : str, title : str, date : datetime, price : float, authors : list[Author], themes : list[Theme]):
        try:
            if not self._book_repository.check_is_isbn_exist(isbn):
                self._book_repository.add_book(isbn, title, date, price)
            else:
                raise ValueError("Le livre existe déjà.")
            if authors:
                for author in authors:
                    self._book_author_repository.add_book_author(isbn, author.id)   
            if themes:
                for theme in themes:
                    self._book_theme_repository.add_book_theme(isbn, theme.id)  
        except ValueError as e:
            print(f"Erreur lors de l'ajout du livre : {e}")

    def get_all(self) -> list[BookDTO]:
        books : list[Book] = self._book_repository.get_all()
        books_dto : list[BookDTO] = []
        for book in books:
            books_dto.append(BookDTO(book.isbn, book.title, book.date, self._book_author_repository.get_authors_by_isbn(book.isbn), self._book_theme_repository.get_themes_by_isbn(book.isbn), book.price))
        return books_dto

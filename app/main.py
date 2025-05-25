from services import ThemeService, AuthorService, BookService

class main:
    _theme_service : ThemeService = ThemeService()
    _author_service : AuthorService = AuthorService()

    _author_service.add_author("Julien")
    _author_service.add_author("Francois")
    _theme_service.add_theme("Drame")
    _theme_service.add_theme("Adventure")
    _theme_service.add_theme("SF")
    authors = _author_service.get_all()
    themes = _theme_service.get_all()

    _book_service : BookService = BookService()

    _book_service.add_book("9782070360046", "Le Petit Prince", "1943-04-06", 6.50, [authors[0]], [themes[0]])
    _book_service.add_book("9782266180319", "Vingt mille lieues sous les mers", "1943-04-06", 8.20, [authors[1]], [themes[0], themes[1]])
    _book_service.add_book("9782266120319", "Vingt mille lieues sous les terres", "1943-04-06", 9.20, [authors[1], authors[0]], [themes[0], themes[1]])
    books = _book_service.get_all()

    for book in books:
        print(book)

    _theme_service.add_theme("POUEPOUET")
    themes = _theme_service.get_all()
    for t in themes:
        print(themes)

if __name__ == "__main__":
    main()
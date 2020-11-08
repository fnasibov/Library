from LibraryAPI.domain.Book import Book


class BookView:

    def __init__(self, book: Book):
        self.id = book.id
        self.title = book.title


class BookListView:

    def __init__(self, books: list[Book]):
        self.books = []
        for book in books:
            self.books.append(BookView(book).__dict__)

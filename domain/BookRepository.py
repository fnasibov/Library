from LibraryAPI.config.db import db
from LibraryAPI.domain.Book import Book
from contextlib import closing


def save(book: Book):
    db.session.add(book)
    db.session.commit()
    return book.title

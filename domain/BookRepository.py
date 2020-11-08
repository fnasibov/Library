from LibraryAPI.config.db import db
from LibraryAPI.domain.Book import Book


def save(book: Book):
    db.session.add(book)
    db.session.commit()
    return book.title


def findAll():
    books = Book.query.all()
    return books


def findById(id: str):
    return Book.query.get(id)

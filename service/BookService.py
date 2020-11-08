from LibraryAPI.domain import BookRepository
from LibraryAPI.domain.Book import Book


def save(book: Book):
    return BookRepository.save(book)


def getAll():
    return BookRepository.findAll()


def getById(id: str):
    return BookRepository.findById(id)

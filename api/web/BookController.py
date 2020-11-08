from LibraryAPI import app
from LibraryAPI.config.decorators import request_body
from LibraryAPI.domain.Book import Book
from LibraryAPI.service import BookService


@app.route('/books', methods=['POST'])
@request_body(Book)
def save(book: Book):
    return BookService.save(book)

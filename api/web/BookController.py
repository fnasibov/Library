from flask import request, jsonify

from LibraryAPI import app
from LibraryAPI.api.dtos import BookListView, BookView
from LibraryAPI.domain.Book import Book
from LibraryAPI.service import BookService


@app.route('/books', methods=['POST', 'GET'])
def books_endpoint():
    if request.method == 'POST':
        req_json = request.get_json()
        return BookService.save(Book(**req_json))
    elif request.method == 'GET':
        view = BookListView(BookService.getAll())
        return jsonify(view.__dict__)


@app.route('/books/<id>', methods=['GET'])
def concrete_book(id: str):
    view = BookView(BookService.getById(id))
    return jsonify(view.__dict__)
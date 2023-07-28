# imports
from application import app
from application import library
from classes.book import Book
from flask import request, jsonify


"""
NOTE:
    Status codes:
        - 200 Ok 
        - 201 Created 
        - 204 No Content
        - 400 Bad Request
        - 404 Not Found
"""


@app.route("/")
def index() -> tuple:
    """Endpoint to retrieve all books in the Library.

    Returns:
        tuple: A tuple containing the JSON representation of books and the HTTP status code.
    """
    if library.books:
        books = [book.to_dict() for book in library.books]
        return jsonify(books), 200
    else:
        return jsonify(message="Library has no books"), 204


@app.route("/add")
def add_book() -> tuple:
    """Endpoint to add a Book to the Library.

    Returns:
        tuple: A tuple containing the JSON representation of the message and the HTTP status code.
    """

    # retrieving query params
    title = request.args.get("title")
    pages = request.args.get("pages")
    isbn = request.args.get("isbn")
    genre = request.args.get("genre")
    author = request.args.get("author")

    # checking that necessary params were specified
    if not title or not pages or not isbn or not genre:
        return jsonify(message="Missing required parameters"), 400

    # checking entered isbn's validity
    is_valid_isbn = Book.check_isbn(isbn)
    if not is_valid_isbn:
        return jsonify(message=f"ISBN {isbn} is not a valid ISBN"), 404

    # checking casting to int for specified pages value
    if pages:
        try:
            pages = int(pages)
        except ValueError:
            return (
                jsonify(message="Invalid value for pages, it must be digits only"),
                400,
            )

    # initialising Book instance based on presence of author param
    if not author:
        book = Book(title, pages, isbn, genre)
    else:
        book = Book(title, pages, isbn, genre, author)

    # adding Book to the Library
    library.add_book(book)

    return jsonify(message=f"Book with ISBN {isbn} succesfully added"), 201


@app.route("/search/<string:author>")
def search_book(author: str) -> tuple:
    """Search for books written by a particular author.

    Args:
        author (str): author (str): Author who we are looking for.

    Returns:
        tuple: A tuple containing the JSON representation of books and the HTTP status code.
    """

    # retrieving books by the specified author - URL param
    author_books = library.search_books_by_author(author)

    # checking if there any books were returned
    if author_books:
        books = [book.to_dict() for book in author_books]
        return jsonify(books), 200
    else:
        return jsonify(message="There are no books by the specified author"), 201


@app.route("/update/<string:isbn>")
def update_book(isbn: str) -> tuple:
    """Update a book based on its ISBN.

    Args:
        isbn (str): ISBN of the book that needs to be updated.

    Returns:
        tuple: A tuple containing the JSON representation of the message and the HTTP status code.
    """

    # checking that specified isbn is valid - URL param
    is_valid_isbn = Book.check_isbn(isbn)

    if not is_valid_isbn:
        return jsonify(message=f"ISBN {isbn} is not a valid ISBN"), 400

    # retrieving specified details that need to be update - query params
    new_title = request.args.get("title")
    new_pages = request.args.get("pages")
    new_genre = request.args.get("genre")
    new_author = request.args.get("author")

    # ensuring that at least one new param is set
    if not new_title and not new_pages and not new_genre and not new_author:
        return jsonify(message="You must specify at least one parameter to update"), 400

    # updating the Book from the Library (if found)
    if library.update_book(
        isbn=isbn,
        new_title=new_title,
        new_pages=new_pages,
        new_genre=new_genre,
        new_author=new_author,
    ):
        return jsonify(message=f"Book with ISBN {isbn} updated successfully"), 200

    return jsonify(message=f"Book with ISBN {isbn} was not found in the library"), 404


@app.route("/delete/<string:isbn>")
def delete_book(isbn: str) -> tuple:
    """Delete a book from the library based on its ISBN.

    Args:
        isbn (str): ISBN of the book to remove from the library.

    Returns:
        tuple: A tuple containing the JSON representation of the message and the HTTP status code.
    """

    # checking that specified isbn is valid - URL param
    is_valid_isbn = Book.check_isbn(isbn)

    if not is_valid_isbn:
        return jsonify(message=f"ISBN {isbn} is not a valid ISBN"), 400

    # removing Book from the Library (if found)
    if library.remove_book(isbn):
        return jsonify(message=f"Book with ISBN {isbn} removed from library"), 200

    return jsonify(message=f"Book with ISBN {isbn} was not found in the library"), 404

from application import app
from application import library
from classes.book import Book
from flask import request, jsonify


"""
Status codes:
    - 200 OK 
    - 201 CREATED 
    - 204 NO CONTENT
    - 400 BAD REQUEST
    - 404 NOT FOUND
"""

# TODO: Add more comments


@app.route("/")
def index():
    # display all books

    if library.books:
        books = [book.to_dict() for book in library.books]
        return jsonify(books), 200
    else:
        return jsonify(message="Library has no books"), 201
        # return "There are no books currently in the library"


@app.route("/add")
def add_book():
    """Add a new book to the library

    Returns:
        str: Message
    """

    # examples

    # /add?title=To Kill a Mockingbird&pages=336&isbn=978-0061120084&genre=Fiction&author=Harper Lee
    # /add?title=1984&pages=328&isbn=978-0451524935&genre=Fiction&author=George Orwell
    # /add?title=Animal Farm&pages=328&isbn=123123123&genre=Fiction&author=George Orwell
    # /add?title=Pride and Prejudice&pages=432&isbn=978-0141439518&genre=Classic&author=Jane Austen
    # /add?title=The Great Gatsby&pages=180&isbn=978-0743273565&genre=Fiction&author=F. Scott Fitzgerald
    # /add?title=The Catcher in the Rye&pages=240&isbn=978-0316769488&genre=Fiction&author=J.D. Salinger
    # /add?title=Harry Potter and the Sorcerer's Stone&pages=320&isbn=978-0590353427&genre=Fantasy&author=J.K. Rowling
    # /add?title=To All the Boys I've Loved Before&pages=384&isbn=978-1442426702&genre=Young Adult&author=Jenny Han
    # /add?title=The Lord of the Rings: The Fellowship of the Ring&pages=432&isbn=978-0618346257&genre=Fantasy&author=J.R.R. Tolkien
    # /add?title=The Hunger Games&pages=384&isbn=978-0439023528&genre=Young Adult&author=Suzanne Collins
    # /add?title=The DaVinci Code&pages=592&isbn=978-0307474278&genre=Mystery&author=Dan Brown

    title = request.args.get("title")
    pages = request.args.get("pages")
    isbn = request.args.get("isbn")
    genre = request.args.get("genre")
    author = request.args.get("author")

    if not title or not pages or not isbn or not genre:
        return jsonify(message="Missing required parameters"), 404

    is_valid_isbn = Book.check_isbn(isbn)
    if not is_valid_isbn:
        return jsonify(message=f"ISBN {isbn} is not a valid ISBN"), 404

    if pages:
        try:
            pages = int(pages)
        except ValueError:
            return (
                jsonify(message="Invalid value for pages, it must be digits only"),
                400,
            )

    if not author:
        book = Book(title, pages, isbn, genre)
    else:
        book = Book(title, pages, isbn, genre, author)

    library.add_book(book)

    return jsonify(message=f"Book with ISBN {isbn} succesfully added"), 201


@app.route("/search/<string:author>")
def search_book(author: str):
    """Search for books written by a particular author

    Args:
        author (str): Author who we are looking for

    Returns:
        list: List of the books written by the author
    """
    # search for books by a given author

    # example
    # /search/Bobby

    author_books = library.search_books_by_author(author)

    if author_books:
        books = [book.to_dict() for book in author_books]
        return jsonify(books), 200
    else:
        return jsonify(message="There are no books by the specified author"), 201


@app.route("/update/<string:isbn>")
def update_book(isbn: str):
    """Update a book based on its ISBN

    Args:
        isbn (str): ISBN of the book that needs to be updated

    Returns:
        str: Message
    """

    is_valid_isbn = Book.check_isbn(isbn)
    if not is_valid_isbn:
        return jsonify(message=f"ISBN {isbn} is not a valid ISBN"), 400

    new_title = request.args.get("title")
    new_pages = request.args.get("pages")
    new_genre = request.args.get("genre")
    new_author = request.args.get("author")

    if not new_title and not new_pages and not new_genre and not new_author:
        return jsonify(message="You must specify at least one parameter to update"), 400

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
def delete_book(isbn: str):
    """Delete a book from the library based on its ISBN

    Args:
        isbn (str): ISBN of the book to remove from the library

    Returns:
        str: Message
    """

    is_valid_isbn = Book.check_isbn(isbn)
    if not is_valid_isbn:
        return jsonify(message=f"ISBN {isbn} is not a valid ISBN"), 400

    if library.remove_book(isbn):
        return jsonify(message=f"Book with ISBN {isbn} removed from library"), 200

    return jsonify(message=f"Book with ISBN {isbn} was not found in the library"), 404

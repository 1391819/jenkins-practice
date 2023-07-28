import pytest
from application import app, library
from classes.book import Book

# TODO: Add more comprehensive comments to test units


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client


def test_index(client):
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee")
    ]

    response = client.get("/")
    assert response.status_code == 200
    assert len(response.json) == 1

    # empty library
    library.books = []

    response = client.get("/")
    assert response.status_code == 201
    assert response.json["message"] == "Library has no books"


def test_add_book(client):
    response = client.get(
        f"/add?title=To Kill a Mockingbird&pages=336&isbn=978-0061120084&genre=Fiction&author=Harper Lee"
    )

    assert response.status_code == 201
    assert response.json["message"] == "Book with ISBN 978-0061120084 succesfully added"

    # adding a book with missing parameters
    response = client.get("/add?title=Title Only")
    assert response.status_code == 404
    assert response.json["message"] == "Missing required parameters"

    # adding a book with an invalid ISBN
    response = client.get(
        "/add?title=Invalid ISBN&pages=100&isbn=invalid&genre=Unknown"
    )
    assert response.status_code == 404
    assert response.json["message"] == "ISBN invalid is not a valid ISBN"


def test_search_book(client):
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee"),
        Book("1984", 328, "978-0451524935", "Fiction", "George Orwell"),
        Book("Animal Farm", 328, "978-0451524935", "Fiction", "George Orwell"),
    ]

    # searching for books by an author with existing books
    response = client.get("/search/George%20Orwell")
    assert response.status_code == 200
    assert len(response.json) == 2

    # searching for books by an author with no books
    response = client.get("/search/aaaa")
    assert response.status_code == 201
    assert response.json["message"] == "There are no books by the specified author"


def test_update_book(client):
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee")
    ]

    # updating a book with a valid ISBN and changing the title
    response = client.get("/update/978-0061120084?title=Updated%20Book%201")
    assert response.status_code == 200
    assert (
        response.json["message"] == "Book with ISBN 978-0061120084 updated successfully"
    )

    # updating a book with an invalid ISBN
    response = client.get("/update/invalid_isbn?title=Invalid%20ISBN%20Book")
    assert response.status_code == 400
    assert response.json["message"] == "ISBN invalid_isbn is not a valid ISBN"

    # updating a book with no parameters
    response = client.get("/update/978-0061120084")
    assert response.status_code == 400
    assert (
        response.json["message"] == "You must specify at least one parameter to update"
    )

    # updating a book that does not exist
    response = client.get("/update/978-0451524935?title=Non-Existent%20Book")
    assert response.status_code == 404
    assert (
        response.json["message"]
        == "Book with ISBN 978-0451524935 was not found in the library"
    )


def test_delete_book(client):
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee")
    ]

    # deleting a book with a valid ISBN
    response = client.get("/delete/978-0061120084")
    assert response.status_code == 200
    assert (
        response.json["message"] == "Book with ISBN 978-0061120084 removed from library"
    )

    # deleting a book with an invalid ISBN
    response = client.get("/delete/invalid_isbn")
    assert response.status_code == 400
    assert response.json["message"] == "ISBN invalid_isbn is not a valid ISBN"

    # deleting a book that does not exist
    response = client.get("/delete/978-0451524935")
    assert response.status_code == 404
    assert (
        response.json["message"]
        == "Book with ISBN 978-0451524935 was not found in the library"
    )

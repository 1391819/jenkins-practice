# imports
import pytest
from application import app, library
from classes.book import Book
from flask.testing import FlaskClient


@pytest.fixture
def client() -> FlaskClient:
    """Fixture to create a test client.

    Yields:
        Flask.testing.FlaskClient: The test client.
    """

    # configuring test mode
    app.config["TESTING"] = True

    # creating testing client
    client = app.test_client()

    yield client


def test_index(client: FlaskClient) -> None:
    """Test for the / (index) route.

    Args:
        client (FlaskClient): The test client.
    """

    # testing response when there are Books in the Library
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee")
    ]

    response = client.get("/")
    assert response.status_code == 200
    assert len(response.json) == 1

    # testing response when there are no Books in the Library
    library.books = []

    response = client.get("/")
    assert response.status_code == 204
    assert (
        not response.data
    )  # there is a message, but the response is empty due to 204 status code


def test_add_book(client: FlaskClient) -> None:
    """Test for the /add route.

    Args:
        client (FlaskClient): The test client.
    """

    # testing adding a Book with all the required params
    response = client.get(
        f"/add?title=To Kill a Mockingbird&pages=336&isbn=978-0061120084&genre=Fiction&author=Harper Lee"
    )

    assert response.status_code == 201
    assert response.json["message"] == "Book with ISBN 978-0061120084 succesfully added"

    # testing adding a Book with no author specified
    response = client.get(
        f"/add?title=To Kill a Mockingbird&pages=336&isbn=978-0061120084&genre=Fiction"
    )
    assert response.status_code == 201
    assert response.json["message"] == "Book with ISBN 978-0061120084 succesfully added"

    # testing adding a Book with a pages value not convertable to an integer
    #   no need to use pytest.raises since we handled the exception
    #   with pytest.raises(ValueError):
    response = client.get(
        f"/add?title=To Kill a Mockingbird&pages=AAA&isbn=978-0061120084&genre=Fiction"
    )
    assert response.status_code == 400
    assert response.json["message"] == "Invalid value for pages, it must be digits only"

    # testing adding a Book with missing parameters
    response = client.get("/add?title=Title Only")
    assert response.status_code == 400
    assert response.json["message"] == "Missing required parameters"

    # testing adding a Book with an invalid ISBN
    response = client.get(
        "/add?title=Invalid ISBN&pages=100&isbn=invalid&genre=Unknown"
    )
    assert response.status_code == 404
    assert response.json["message"] == "ISBN invalid is not a valid ISBN"


def test_search_book(client: FlaskClient) -> None:
    """Test for the /search route.

    Args:
        client (FlaskClient): The test client.
    """

    # setting up Library with some sample books
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee"),
        Book("1984", 328, "978-0451524935", "Fiction", "George Orwell"),
        Book("Animal Farm", 328, "978-0451524935", "Fiction", "George Orwell"),
    ]

    # testing searching for Books by an author with existing books
    response = client.get("/search/George%20Orwell")
    assert response.status_code == 200
    assert len(response.json) == 2

    # testing searching for Books by an author with no books
    response = client.get("/search/aaaa")
    assert response.status_code == 201
    assert response.json["message"] == "There are no books by the specified author"


def test_update_book(client: FlaskClient) -> None:
    """Test for the /update route.

    Args:
        client (FlaskClient): The test client.
    """

    # setting up Library with some sample books
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee")
    ]

    # testing updating a Book with a valid ISBN and changing the title
    response = client.get("/update/978-0061120084?title=Updated%20Book%201")
    assert response.status_code == 200
    assert (
        response.json["message"] == "Book with ISBN 978-0061120084 updated successfully"
    )

    # testing updating a Book with an invalid ISBN
    response = client.get("/update/invalid_isbn?title=Invalid%20ISBN%20Book")
    assert response.status_code == 400
    assert response.json["message"] == "ISBN invalid_isbn is not a valid ISBN"

    # testing updating a Book with no parameters
    response = client.get("/update/978-0061120084")
    assert response.status_code == 400
    assert (
        response.json["message"] == "You must specify at least one parameter to update"
    )

    # testing updating a Book that does not exist
    response = client.get("/update/978-0451524935?title=Non-Existent%20Book")
    assert response.status_code == 404
    assert (
        response.json["message"]
        == "Book with ISBN 978-0451524935 was not found in the library"
    )


def test_delete_book(client: FlaskClient) -> None:
    """Test for the /delete route.

    Args:
        client (FlaskClient): The test client.
    """

    # setting up Library with some sample books
    library.books = [
        Book("To Kill a Mockingbird", 336, "978-0061120084", "Fiction", "Harper Lee")
    ]

    # testing deleting a Book with a valid ISBN
    response = client.get("/delete/978-0061120084")
    assert response.status_code == 200
    assert (
        response.json["message"] == "Book with ISBN 978-0061120084 removed from library"
    )

    # testing deleting a Book with an invalid ISBN
    response = client.get("/delete/invalid_isbn")
    assert response.status_code == 400
    assert response.json["message"] == "ISBN invalid_isbn is not a valid ISBN"

    # testing deleting a Book that does not exist
    response = client.get("/delete/978-0451524935")
    assert response.status_code == 404
    assert (
        response.json["message"]
        == "Book with ISBN 978-0451524935 was not found in the library"
    )

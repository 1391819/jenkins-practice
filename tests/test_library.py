# imports
import pytest
from classes.library import Library
from classes.book import Book


@pytest.fixture()
def library() -> Library:
    """Fixture to create a new Library instance for each test.

    Returns:
        Library: A new Library instance.
    """
    return Library()


@pytest.fixture()
def book() -> Book:
    """Fixture to create a new Book instance for each test.

    Returns:
        Book: A new Book instance.
    """
    return Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )


@pytest.fixture()
def book1() -> Book:
    """Fixture to create a new Book instance for each test.

    Returns:
        Book: A new Book instance.
    """
    return Book(
        "Another Book",
        300,
        "978-1234567890",
        "Mystery",
        "Kate Morton",
    )


@pytest.fixture()
def book2() -> Book:
    """Fixture to create a new Book instance for each test.

    Returns:
        Book: A new Book instance.
    """
    return Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")


def test_add_book(library: Library, book: Book) -> None:
    """Test the add_book() method of the Library class.

    Args:
        library (Library): A Library instance.
        book (Book): A Book instance.
    """

    # adding sample Book to the Library
    library.add_book(book)

    # testing that the Book has been added to the Library
    assert book in library.books
    assert len(library.books) == 1


def test_remove_book(library: Library, book: Book, book1: Book, book2: Book) -> None:
    """Test the remove_book() method of the Library class.

    Args:
        library (Library): A Library instance.
        book (Book): A Book instance.
        book1 (Book): Another Book instance.
        book2 (Book): One more Book instance.
    """

    # adding sample Book(s) to the Library
    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)

    # testing using a valid (and existing) ISBN
    assert library.remove_book("978-1416550549") == True
    assert len(library.books) == 2

    # testing using an invalid ISBN
    assert library.remove_book("1231312323123123123123123") == False


def test_update_book(library: Library, book: Book, book1: Book, book2: Book) -> None:
    """Test the update_book() method of the Library class.

    Args:
        library (Library): A Library instance.
        book (Book): A Book instance.
        book1 (Book): Another Book instance.
        book2 (Book): One more Book instance.
    """

    # adding sample Book(s) to the Library
    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)

    # testing updating title, pages, genre, and author of a valid ISBN
    assert (
        library.update_book(
            "123-4-56-789012-3",
            new_title="Updated Book",
            new_pages=200,
            new_genre="Mystery",
            new_author="John Doe",
        )
        == True
    )

    # checking that the attributes of the updated Book have been updated
    updated_book = library.books[2]
    assert updated_book.title == "Updated Book"
    assert updated_book.pages == 200
    assert updated_book.genre == "Mystery"
    assert updated_book.author == "John Doe"

    # testing updating only some attributes
    assert library.update_book("978-1416550549", new_title="New Title") == True

    # checking that only the title of the updated Book has been updated
    updated_book = library.books[0]
    assert updated_book.title == "New Title"
    assert updated_book.pages == 560  # unchanged
    assert updated_book.genre == "Historical Fiction"  # unchanged
    assert updated_book.author == "Kate Morton"  # unchanged

    # testing updating a non-existent book
    assert library.update_book("1234567890123") == False

    # testing updating with invalid ISBN
    assert library.update_book("123") == False


def test_search_books_by_author(
    library: Library, book: Book, book1: Book, book2: Book
) -> None:
    """Tes the search_books_by_author() method of the Library class.

    Args:
        library (Library): A Library instance.
        book (Book): A Book instance.
        book1 (Book): Another Book instance.
        book2 (Book): One more Book instance.
    """

    # adding sample Book(s) to the Library
    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)

    # testing that Book(s) written by an existing author are found and returned
    assert library.search_books_by_author("Kate Morton") == [book, book1]
    assert len(library.search_books_by_author("Kate Morton")) == 2

    # testing that no books are found for a non-existent author
    assert library.search_books_by_author("Fake Author") == []
    assert len(library.search_books_by_author("Fake Author")) == 0

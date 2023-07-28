from classes.library import Library
from classes.book import Book
import gc

library = Library()

book = Book(
    "The Forgotten Garden",
    560,
    "978-1416550549",
    "Historical Fiction",
    "Kate Morton",
)

book1 = Book(
    "Another Book",
    300,
    "978-1234567890",
    "Mystery",
    "Kate Morton",
)


book2 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")


def clean_library(library):
    for obj in library.books:
        del obj

    library.books.clear()

    gc.collect()


def test_add_book():
    library.add_book(book)
    assert book in library.books


def test_remove_book():
    clean_library(library)

    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)

    assert library.remove_book("978-1416550549") == True
    assert len(library.books) == 2

    assert library.remove_book("1231312323123123123123123") == False


def test_update_book():
    clean_library(library)

    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)

    # updating title, pages, genre, and author
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

    updated_book = library.books[2]
    assert updated_book.title == "Updated Book"
    assert updated_book.pages == 200
    assert updated_book.genre == "Mystery"
    assert updated_book.author == "John Doe"

    # updating only some attributes
    assert library.update_book("978-1416550549", new_title="New Title") == True

    updated_book = library.books[0]
    assert updated_book.title == "New Title"
    assert updated_book.pages == 560  # unchanged
    assert updated_book.genre == "Historical Fiction"  # unchanged
    assert updated_book.author == "Kate Morton"  # unchanged

    # updating a non-existent book
    assert library.update_book("1234567890123") == False

    # updating with invalid ISBN
    assert library.update_book("123") == False


def test_search_books_by_author():
    clean_library(library)

    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)

    real_author = "Kate Morton"
    fake_author = "Fake Author"

    # assert len(library.search_books_by_author(real_author)) == 2
    # assert len(library.search_books_by_author(fake_author)) == 0

    assert library.search_books_by_author(real_author) == [book, book1]
    # assert library.search_books_by_author(fake_author) == []

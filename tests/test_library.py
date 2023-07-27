from classes.library import Library
from classes.book import Book


def test_search_books_by_author():
    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )
    library = Library([book1, book1])
    real_author = "Kate Morton"
    fake_author = "fake author"
    assert library.search_books_by_author(real_author) == [book1, book1]
    assert library.search_books_by_author(fake_author) == []


def test_add_book():
    library = Library()

    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )

    library.add_book(book1)
    assert book1 in library.books


def test_remove_book():
    library = Library()

    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )
    book2 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")

    library.add_book(book1)
    library.add_book(book2)

    assert library.remove_book("978-1416550549") == True
    assert library.remove_book("1231312323123123123123123") == False


def test_update_book():
    library = Library()

    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )
    book2 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")

    library.add_book(book1)
    library.add_book(book2)

    assert library.update_book("123") == False
    assert library.update_book("978-1416550549") == True

    assert (
        library.update_book(
            "123-4-56-789012-3", "test_title", 1, "test_genre", "test_author"
        )
        == True
    )

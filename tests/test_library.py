from programs.library import Library
from programs.book import Book


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


def test_search_book():
    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )
    book2 = Book(
        "Fake book",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )
    library = Library([book1, book1])
    assert library.search_book(book1) == book1
    assert library.search_book(book2) == None


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

    library.remove_book(book2)
    assert book2 not in library.books

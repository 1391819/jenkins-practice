import pytest
from programs.book import Book


def test_search():
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography", "John Smith")
    assert book1.search("Alice Jones") == True
    assert book2.search("John Smith") == True
    assert book1.search("not a real author") == False


def test_check_isbn():
    assert Book.check_isbn("978-0-00-821843-0") == True
    assert not Book.check_isbn("978-0-00-821843-1") == True

    with pytest.raises(ValueError):
        assert Book.check_isbn("                         ")


def test_str():
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography")

    assert (
        str(book1)
        == "Title: Sample text\nAuthor: Alice Jones\nNumber of pages: 300\nGenre: Fantasy\nISBN: 123-4-56-789012-3"
    )

    assert (
        str(book2)
        == "Title: Generic title\nAuthor: Unknown\nNumber of pages: 125\nGenre: Biography\nISBN: 321-4-57-787812-3"
    )

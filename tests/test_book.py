import pytest
from classes.book import Book


def test_check_author():
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography", "John Smith")
    assert book1.check_author("Alice Jones") == True
    assert book2.check_author("John Smith") == True
    assert book1.check_author("not a real author") == False


def test_check_isbn():
    assert Book.check_isbn("978-0-00-821843-0") == True
    assert not Book.check_isbn("978-0-00-821843-1") == True
    assert Book.check_isbn("123") == False


def test_str():
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography")

    assert (
        str(book1)
        == "Written by Alice Jones, Sample text is a gripping 300-page Fantasy novel. ISBN: 123-4-56-789012-3"
    )
    assert (
        str(book2)
        == "Written by Unknown, Generic title is a gripping 125-page Biography novel. ISBN: 321-4-57-787812-3"
    )

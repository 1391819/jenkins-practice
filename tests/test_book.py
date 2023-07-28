# imports
from classes.book import Book


def test_check_author() -> None:
    """Test the check_author() method of the Book class."""

    # creating sample books
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography", "John Smith")

    # testing valid authors
    assert book1.check_author("Alice Jones") == True
    assert book2.check_author("John Smith") == True

    # testing invalid authors
    assert book1.check_author("not a real author") == False


def test_check_isbn() -> None:
    """Test the check_isbn() method of the Book class."""

    # .check_isbn() is static so we don't need any Book samples

    # testing valid isbn containing -
    assert Book.check_isbn("978-0-00-821843-0") == True

    # testing valid isbn, not containing -
    assert Book.check_isbn("9780008218430") == True

    # testing invalid isbn, containing non-digits and length less than 13
    assert Book.check_isbn("9780A82S8430") == False

    # testing invalid isbn, containing non-digits and length is 13
    assert Book.check_isbn("978A008218430") == False

    # testing invalid isbn, invalid check sum
    assert Book.check_isbn("978-0-00-821843-1") == False

    # testing invalid isbn, length less than 13
    assert Book.check_isbn("123") == False

    # testing invalid isbn, check sum is non-digit
    assert Book.check_isbn("978-0-00-821843-A") == False


def test_str() -> None:
    """Test the __str__() method of the Book class."""

    # creating sample Books
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography")

    # testing returned strings
    assert (
        str(book1)
        == "Written by Alice Jones, Sample text is a gripping 300-page Fantasy novel. ISBN: 123-4-56-789012-3"
    )
    assert (
        str(book2)
        == "Written by Unknown, Generic title is a gripping 125-page Biography novel. ISBN: 321-4-57-787812-3"
    )


def test_to_dict() -> None:
    """Testing the to_dict() method of the Book class."""

    # creating sample Book
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")

    # testing returned dict
    assert book1.to_dict() == {
        "isbn": "123-4-56-789012-3",
        "title": "Sample text",
        "author": "Alice Jones",
        "genre": "Fantasy",
        "pages": "300",
    }

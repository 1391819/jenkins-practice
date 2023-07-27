from book import Book, SciFiNovel, FantasyNovel


def test_setup():
    with open("test.books.list", "w") as f:
        pass
    Book(
        "Sample text",
        300,
        "123-4-56-789012-3",
        "Fantasy",
        author="Alice Jones",
        bookfile="test.books.list",
    )
    Book(
        "Generic title",
        125,
        "321-4-57-787812-3",
        "Biography",
        author="John Smith",
        bookfile="test.books.list",
    )
    Book(
        "Sample text 2",
        254,
        "213-5-46-779812-3",
        "Fantasy",
        author="Alice Jones",
        bookfile="test.books.list",
    )
    Book.books = []
    Book.initialise_list("test.books.list")


def test_search_method():
    assert list(map(lambda x: x.title, Book.search("Alice Jones"))) == [
        "Sample text",
        "Sample text 2",
    ]
    assert list(map(lambda x: x.title, Book.search("John Smith"))) == ["Generic title"]
    assert Book.search("not a real author") == []


def test_isbn_checker():
    assert Book.valid_isbn("978-0-00-821843-0")
    assert not Book.valid_isbn("978-0-00-821843-1")


def test_scifi_subclass():
    SciFiNovel(
        "lorem ipsum",
        300,
        "123-4-56-789012-5",
        author="Bob Stevens",
        bookfile="test.books.list",
    )
    SciFiNovel(
        "lorem ipsum 2",
        546,
        "123-4-56-789012-7",
        author="Bob Stevens",
        bookfile="test.books.list",
    )
    assert list(map(lambda x: x.title, Book.search("Bob Stevens"))) == [
        "lorem ipsum",
        "lorem ipsum 2",
    ]


def test_fantasy_subclass():
    FantasyNovel(
        "title here",
        300,
        "123-4-56-789032-5",
        author="Jane Doe",
        bookfile="test.books.list",
    )
    FantasyNovel(
        "insert text",
        546,
        "123-5-66-789012-7",
        author="Jane Doe",
        bookfile="test.books.list",
    )
    assert list(map(lambda x: x.title, Book.search("Jane Doe"))) == [
        "title here",
        "insert text",
    ]

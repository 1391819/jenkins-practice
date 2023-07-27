from .book import Book


class Library:
    def __init__(self, books: list[Book] = []) -> None:
        """Initialise a Library instance

        Args:
            books (list[Book], optional): Book instances within the library. Defaults to [].
        """
        self.books = books

    def add_book(self, book: Book) -> None:
        """Add a Book instance to the library

        Args:
            book (Book): Book to be added
        """
        self.books.append(book)
        print("Book added to library!\n")

    def remove_book(self, book: Book) -> None:
        """Remove a Book instance from the library

        Args:
            book (Book): Book to be removed
        """
        self.books.remove(book)
        print("Book removed from library!\n")

    def search_book(self, book: Book) -> Book:
        """Search for a Book instance in the Library

        Args:
            book (Book): Book to be searched

        Returns:
            Book: Book instance if found in the library, None otherwise
        """
        if book in self.books:
            return book
        else:
            return None

    def search_books_by_author(self, author: str) -> list[Book]:
        """Search for Book instances written by a particular author

        Args:
            author (str): Author to be searched

        Returns:
            list[Book]: List of Book instances written by the particular author
        """
        books_by_author = []

        for book in self.books:
            if book.search(author):
                books_by_author.append(book)

        return books_by_author

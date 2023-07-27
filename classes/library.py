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

    def remove_book(self, isbn: str) -> bool:
        """Remove a Book from the library based on ISBN

        Args:
            isbn (str): ISBN to search and delete

        Returns:
            bool: True if Book was removed from Library, False otherwise
        """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def update_book(
        self,
        isbn: str,
        new_title: str = None,
        new_pages: int = None,
        new_genre: str = None,
        new_author: str = None,
    ) -> bool:
        """Update a book based on the specified isbn

        Args:
            isbn (str): ISBN of the book that needs to be updated
            new_title (str, optional): New title of the book. Defaults to None.
            new_pages (int, optional): New number of pages of the book. Defaults to None.
            new_genre (str, optional): New genre of the book. Defaults to None.
            new_author (str, optional): New author of the book. Defaults to None.

        Returns:
            bool: True if the book was updated succesfully, False otherwise
        """
        for book in self.books:
            if book.isbn == isbn:
                if new_title:
                    book.title = new_title

                if new_pages:
                    book.pages = new_pages

                if new_genre:
                    book.genre = new_genre

                if new_author:
                    book.author = new_author

                return True
        return False

    def search_books_by_author(self, author: str) -> list[Book]:
        """Search for Book instances written by a particular author

        Args:
            author (str): Author to be searched

        Returns:
            list[Book]: List of Book instances written by the particular author
        """
        books_by_author = []

        for book in self.books:
            if book.check_author(author):
                books_by_author.append(book)

        return books_by_author

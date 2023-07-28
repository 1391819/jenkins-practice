# imports
from .book import Book

# this is to avoid problems on Python 3.8 (square brackets type annotations)
# had to be added to perform some practice exercise on an AWS instance
# that used Ubuntu 20.04 as OS image.
from typing import List


# Library class
class Library:
    def __init__(self, books: List[Book] = None) -> None:
        """Initialise a Library instance.

        Args:
            books (List[Book], optional): List of Book instances. Defaults to None.
        """

        # avoiding to have problems with mutable default args / shared default values
        if books is None:
            books = []
        self.books = books

    def add_book(self, book: Book) -> None:
        """Add a Book to the Library.

        Args:
            book (Book): Book to be added to the Library.
        """
        self.books.append(book)

    def remove_book(self, isbn: str) -> bool:
        """Remove a Book from the Library based on its ISBN.

        Args:
            isbn (str): ISBN of the Book to search and delete from the Library.

        Returns:
            bool: True if the Book was removed from the Library, False otherwise.
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
        """Update a Book in the Library based on its ISBN.

        Args:
            isbn (str): ISBN of the Book to update
            new_title (str, optional): New title of the Book. Defaults to None.
            new_pages (int, optional): New number of pages of the Book. Defaults to None.
            new_genre (str, optional): New genre of the Book. Defaults to None.
            new_author (str, optional): New author of the Book. Defaults to None.

        Returns:
            bool: True if the Book was updated, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                if new_title is not None:
                    book.title = new_title

                if new_pages is not None:
                    book.pages = new_pages

                if new_genre is not None:
                    book.genre = new_genre

                if new_author is not None:
                    book.author = new_author

                return True
        return False

    def search_books_by_author(self, author: str) -> List[Book]:
        """Search for Books written by a particular author.

        Args:
            author (str): Name of the author that we are looking for.

        Returns:
            List[Book]: List of Books written by the specified author or an empty list if no Books were found.
        """
        books_by_author = []

        for book in self.books:
            if book.check_author(author):
                books_by_author.append(book)

        return books_by_author

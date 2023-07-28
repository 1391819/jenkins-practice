# imports
from typing import Dict


# Book class
class Book:
    def __init__(
        self,
        title: str,
        pages: int,
        isbn: str,
        genre: str,
        author: str = "Unknown",
    ) -> None:
        """Initialise a Book instance.

        Args:
            title (str): Title of the Book.
            pages (int): Number of pages of the Book.
            isbn (str): ISBN of the Book.
            genre (str): Genre of the Book.
            author (str, optional): Author of the Book. Defaults to "Unknown".
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def __str__(self) -> str:
        return f"Written by {self.author}, {self.title} is a gripping {self.pages}-page {self.genre} novel. ISBN: {self.isbn}"

    """
    NOTE:
    
        A static method is a method that belongs to the class itself and does not depend on the instance of the class. Unlike regular instance methods that have access to instance-specific data, static methods only have access to the arguments passed to them and other static attributes or methods within the class.    
        
        You should use @staticmethod in Python when you have a method in a class that:

            - Does not require access to the instance (no self parameter needed).
            - Performs a task that is related to the class, but not to any specific instance.
            - Doesn't rely on or modify any instance-level attributes or state.
    """

    @staticmethod
    def check_isbn(isbn: str) -> bool:
        """Determine the validity of a given isbn.

        Args:
            isbn (str): ISBN to check.

        Returns:
            bool: True if the ISBN is 13 digits long (excluding -), and the check sum is correct, False otherwise.
        """

        # remove - characters
        isbn = isbn.replace("-", "")

        # check that the isbn is 13 in length
        if len(isbn) != 13:
            # removed raise, we just return False
            # raise (ValueError("ISBN must contain 13 digits"))
            return False

        # get check digit
        check_digit = isbn[-1]

        # remove check digit from isbn
        isbn = isbn[:-1]

        # checking that last digit is a number
        if not check_digit.isdigit():
            return False

        # sum var used to check validity of the isbn
        sum = 0

        # go through the whole ISBN
        for idx, char in enumerate(isbn):
            # checking if each char is digit or not
            if not char.isdigit():
                return False

            # alternating weights
            if idx % 2 == 0:
                tmp_sum = int(char) * 1
            else:
                tmp_sum = int(char) * 3

            # adding to sum
            sum += tmp_sum

        # checking if check_digit is valid or not
        if (sum + int(check_digit)) % 10 == 0:
            return True
        else:
            return False

    def check_author(self, author: str) -> bool:
        """Check if specified author is the Book's author.

        Args:
            author (str): Author to be checked.

        Returns:
            bool: True if specified author is Book's author, False otherwise.
        """
        return self.author == author

    def to_dict(self) -> Dict[str, str]:
        """Return the Book information in a Dictionary representation.

        Returns:
            Dict[str, str]: Dictionary containing Book information.
        """
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": str(self.pages),
        }

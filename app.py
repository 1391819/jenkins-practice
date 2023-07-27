# https://github.com/agray998/oop-exercise

from programs.library import Library
from programs.book import Book

if __name__ == "__main__":
    # creating books
    book1 = Book(
        "The Forgotten Garden",
        560,
        "978-1416550549",
        "Historical Fiction",
        "Kate Morton",
    )

    book2 = Book(
        "Dark Matter",
        352,
        "978-1101904220",
        "Science Fiction, Thriller",
        "Blake Crouch",
    )

    book3 = Book(
        "Educated: A Memoir",
        352,
        "978-0399590504",
        "Memoir, Autobiography",
        "Tara Westover",
    )

    book4 = Book(
        "Circe",
        400,
        "978-0316556347",
        "Fantasy, Mythology",
        "Madeline Miller",
    )

    book5 = Book(
        "The Silent Patient",
        336,
        "978-1250301697",
        "Psychological Thriller",
        "Alex Michaelides",
    )

    # testing Book class ------------------------------------------------------------

    # printing book info
    print(book1)
    print()

    # checking isbn
    print(book1.check_isbn("978-1416550549"))
    print()

    # author
    author = "Tara Westover"
    book3.search(author)

    # testing Library class ------------------------------------------------------------

    # creating library
    library = Library([book1, book2, book3, book4, book5])

    # adding book to library
    library.add_book(book5)

    # removing book from library
    library.remove_book(book5)

    # searching for a book in the library
    search = library.search_book(book2)
    if search:
        print("Book found in the library!\n")
        print(search)
        print("------------------------------------")
    else:
        print("Book not found in the library!\n")

    # searching for a particular author's books
    author = "Alex Michaelids"

    # searching books my author
    author_books = library.search_books_by_author(author)

    # displaying books by author
    if author_books:
        print(f"Here are all the books written by {author}:\n")
        for book in author_books:
            print(book)
    else:
        print(f"No books by {author} in our library!")

"""
Using the solution to the OOP exercise from yesterday (the book class), 
create a flask app which allows users to:

- add new books with information supplied via url/query params
- search for books by a given author
- update books that have already been added (stretch goal)
- delete books from the system (stretch goal)
"""

from application import app

if __name__ == "__main__":
    app.run(debug=True)

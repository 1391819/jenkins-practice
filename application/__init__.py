# imports
from flask import Flask
from classes.library import Library

# creating Flask instance
app = Flask(__name__)

# creating empty library
library = Library()

# importing view functions after Flask instance creation
import application.routes

from flask import Flask
from classes.library import Library

app = Flask(__name__)

# creating empty library
library = Library()

import application.routes

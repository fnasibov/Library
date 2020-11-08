from flask import Flask

from LibraryAPI import properties

app = Flask(__name__)

import LibraryAPI.config.db
import LibraryAPI.api.web.BookController

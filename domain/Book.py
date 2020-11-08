import uuid
from collections import namedtuple

from LibraryAPI.config.db import db


class Book(db.Model):
    id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())

    def __init__(self, title):
        self.id = uuid.uuid4().__str__()
        self.title = title

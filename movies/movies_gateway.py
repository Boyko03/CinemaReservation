from ..db import Database
from .models import MovieModel


class MovieGateway:
    def __init__(self):
        self.model = MovieModel()
        self.db = Database()

    def create(self, name, rating):
        query = '''
        INSERT INTO Movies(name, rating) VALUES(?,?)
        '''

        self.db.cursor.execute(query, (name, rating))  # TODO query

        self.db.connection.commit()
        self.db.connection.close()

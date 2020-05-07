from db import Database
from .models import MovieModel


class MovieGateway:
    def __init__(self):
        self.model = MovieModel
        self.db = Database()

    def add_movie(self, name, rating):
        query = '''
        INSERT INTO Movies(name, rating) VALUES(?,?)
        '''

        self.db.cursor.execute(query, (name, rating))  # TODO query

        self.db.connection.commit()
        self.db.connection.close()

    def show_movies(self):
        query = '''SELECT * FROM Movies ORDER BY rating DESC;'''

        self.db.cursor.execute(query)

        movies = self.db.cursor.fetchall()

        self.db.connection.close()

        all_movies = []

        for movie in movies:
            new_movie = self.model(id=movie[0], name=movie[1], rating=movie[2])
            all_movies.append(new_movie)

        return all_movies

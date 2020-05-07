from movies.controllers import MovieController

from movies.movies_gateway import MovieGateway


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def print_movies(self):
        self.controller = MovieGateway.show_movies()

        for movie in self.controller:
            print(f'''
                   [ {movie[0]} ] - {movie[1]} - {movie[2]}
                ''')

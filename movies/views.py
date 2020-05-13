from movies.controllers import MovieController

from movies.movies_gateway import MovieGateway


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def print_movies(self):
        print('\n')
        self.controller = MovieGateway().show_movies()

        for movie in self.controller:
            print(f'[ {movie.id} ] - {movie.name} - {movie.rating}')

        print('\n')

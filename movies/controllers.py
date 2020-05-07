from movies.movies_gateway import MovieGateway


class MovieController:
    def __init__(self):
        self.movies_gateway = MovieGateway()

    def create_movie(self, name, rating):
        name = input('Movie name: ')
        rating = input('Movie rating: ')

        self.movies_gateway.add_movie(name=name, rating=rating)

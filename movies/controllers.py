from .movies_gateway import MoviesGateway


class MovieController:
    def __init__(self):
        self.movies_gateway = MoviesGateway()

    def create_movie(self, name, rating):
        movie = self.movies_gateway.create(name=name, rating=rating)

        # TODO

        return movie

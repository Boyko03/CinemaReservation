from movies.movies_gateway import MovieGateway


class MovieController:
    def __init__(self):
        self.movies_gateway = MovieGateway()

    def create_movie(self, name, rating):
        return self.movies_gateway.add_movie(name=name, rating=rating)

    def get_movies(self):
        movies = self.movies_gateway.select_movies()

        all_movies = []

        for movie in movies:
            all_movies.append(movie)

        return all_movies

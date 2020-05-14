from movies.controllers import MovieController


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def print_movies(self):
        print('\n')
        movies = self.controller.get_movies()

        for movie in movies:
            print(f'[ {movie[0]} ] - {movie[1]} - {movie[2]}')

        print('\n')

    def create_new_movie(self):
        name = input('Movie name: ')
        rating = input('Movie rating: ')

        self.controller.create_movie(name=name, rating=rating)

        print('Movie added successfully')

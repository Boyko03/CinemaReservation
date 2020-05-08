from . controllers import ReservationController
from decorators import login_required


class ReservationView:
    def __init__(self):
        self.controller = ReservationController()

    @login_required
    def make_reservation(self, user):
        tickets_count = self.controller.choose_tickets()
        if tickets_count is None:
            print('Reservation is cancelled.')
            return

        print('Current movies:')
        movies = self.controller.get_movies()
        for movie in movies:
            print(f'[{movie.id}] - {movie.name} ({movie.rating})')

        movie_id = self.controller.choose_movie()
        if movie_id is None:
            print('Reservation is cancelled.')
            return

        movie = self.controller.get_movie_projections()
        print(f'Projectons for movie \'{movie.name}\':')
        for projection in movie.projections:
            print(
                f'[{projection.id}] - {projection.date} {projection.time} ({projection.type}) - {count_free_spaces}')

        projection_id = self.controller.choose_projection()
        if projection_id is None:
            print('Reservation is cancelled.')
            return

        print('Available seats (marked with a dot):')
        hall = self.controller.get_matrix(projection_id)
        print('  1 2 3 4 5 6 7 8 9 10')
        for row, i in enumerate(hall):
            print(f'{i + 1} {" ".join(row)}')

        if self.controller.choose_seats(tickets_count) is None:
            print('Reservation is cancelled.')
            return

        if self.controller.finalize():
            print('Enjoy!')

    def cancel_reservation(self):
        pass

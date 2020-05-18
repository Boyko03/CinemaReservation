from . controllers import ReservationController
# from decorators import login_required


class ReservationView:
    def __init__(self):
        self.controller = ReservationController()

    def make_reservation(self, user):
        tickets_count = self.controller.choose_tickets()
        if tickets_count is None:
            print('Reservation is cancelled.')
            return

        print('Current movies:')
        movies = self.controller.get_movies()
        for movie in movies:
            print(f'[{movie.id}] - {movie.name} ({movie.rating})')

        movie_id, movie_name = self.controller.choose_movie()
        if movie_id is None:
            print('Reservation is cancelled.')
            return

        projections = self.controller.get_movie_projections(movie_id)
        print(f'Projectons for movie \'{movie_name}\':')
        for projection in projections:
            print(
                f'[{projection.id}] - {projection.projection_date} {projection.projection_time} ({projection.projection_type}) - {projection.free_spaces}')

        projection_id = self.controller.choose_projection()
        if projection_id is None:
            print('Reservation is cancelled.')
            return

        print('Available seats (marked with a dot):')
        hall = self.controller.get_matrix(projection_id)
        print('   1 2 3 4 5 6 7 8 9 10')
        for i, row in enumerate(hall):
            print(f'{" " if i != 9 else ""}{i + 1} {" ".join(row)}')

        if self.controller.choose_seats(tickets_count) is None:
            print('Reservation is cancelled.')
            return

        if self.controller.finalize():
            print('Enjoy!')

    def cancel_reservation(self):
        pass

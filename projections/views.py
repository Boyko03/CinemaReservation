from projections.controllers import ProjectionController
# from projections.projections_gateway import ProjectionsGateway
from movies.views import MovieView


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionController()

    def print_all_projections(self):
        MovieView().print_movies()

        movie_id = input('Choose movie id: ')
        print('\n')
        projections = self.controller.get_movie_projections(movie_id)

        for projection in projections:
            print(f'[{projection[0]}] - {projection[3]} - {projection[4]} - {projection[2]}')
        print('\n')

    def print_projections_by_date(self):
        MovieView().print_movies()

        movie_id = input('Choose movie id: ')
        projection_date = input('Date:(yyyy-mm-dd): ')
        print('\n')

        projections = self.controller.get_movie_projections_by_date(movie_id, projection_date)
        if projections == []:
            print('There are no projections for this date!\n')
            return

        for projection in projections:
            print(f'[ {projection[0]} ] - {projection[3]} - {projection[4]} - {projection[2]}')
        print('\n')

    def add_projection(self):
        movie_id = input('Movie id: ')
        movie_type = input('Movie type: ')
        projection_date = input('Date: ')
        projection_time = input('Time: ')

        return self.controller.create_projection(movie_id, movie_type, projection_date, projection_time)

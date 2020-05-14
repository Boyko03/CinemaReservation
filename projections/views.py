from projections.controllers import ProjectionController
from movies.views import MovieView


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionController()

    def print_all_projections(self):
        MovieView().print_movies()

        movie_id = input('Choose movie id: ')
        print('\n')
        projections = self.controller.get_movie_projections(movie_id)

        for p in projections:
            print(f'[{p.id}] - {p.projection_type} - {p.projection_date} - {p.projection_time}')
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

        for p in projections:
            print(f'[ {p.id} ] - {p.projection_type} - {p.projection_date} - {p.projection_time}')
        print('\n')

    def add_projection(self):
        movie_id = input('Movie id: ')
        projection_type = input('Projection type: ')
        projection_date = input('Date: ')
        projection_time = input('Time: ')

        return self.controller.create_projection(movie_id, projection_type, projection_date, projection_time)

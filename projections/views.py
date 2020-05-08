from projections.controllers import ProjectionController
from projections.projections_gateway import ProjectionsGateway


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionController()

    def print_all_projections(self):
        projections = ProjectionsGateway().show_movie_projections()

        for projection in projections:
            print(f'[{projection.id}] - {projection.date} - {projection.time} - {projection.type}')
        print('\n')

    def print_projections_by_date(self):
        self.controller = ProjectionsGateway().show_movie_projections_by_date()
        if self.controller == []:
            print('There are no projections for this date!\n')
            return

        for projection in self.controller:
            print(f'[ {projection.id} ] - {projection.date} - {projection.time} - {projection.type}')
        print('\n')

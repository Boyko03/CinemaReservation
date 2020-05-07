from projections.controllers import ProjectionController
from projections.projections_gateway import ProjectionsGateway


class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionController()

    def print_all_projections(self):
        projections = ProjectionsGateway().show_movie_projections()

        for projection in projections:
            print(f'[{projection.id}] - {projection.date} - {projection.time} - {projection.type}')

    def print_projections_by_date(self):
        self.controller = ProjectionsGateway().show_movie_projections_by_date()

        for projection in self.controller:
            print(f'[ {projection.id} ] - {projection.date} - {projection.time} - {projection.type}')

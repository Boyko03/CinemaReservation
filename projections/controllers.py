from .projections_gateway import ProjectionGateway


class ProjectionController:
    def __init__(self):
        self.projections_gateway = ProjectionGateway()

    def create_projection(self, movie_id, type, date, time):
        projection = self.projections_gateway.create(movie_id=movie_id, type=type, date=date, time=time)

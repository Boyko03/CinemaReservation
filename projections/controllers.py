from projections.projections_gateway import ProjectionsGateway


class ProjectionController:
    def __init__(self):
        self.projections_gateway = ProjectionsGateway()

    def create_projection(self, movie_id, type, date, time):
        movie_id = input('Movie id: ')
        type = input('Movie type: ')
        date = input('Date: ')
        time = input('Time: ')

        self.projections_gateway.add_projection(movie_id=movie_id, type=type, date=date, time=time)

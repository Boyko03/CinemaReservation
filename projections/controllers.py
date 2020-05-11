from projections.projections_gateway import ProjectionsGateway


class ProjectionController:
    def __init__(self):
        self.projections_gateway = ProjectionsGateway()

    def create_projection(self, movie_id, type, date, time):
        self.projections_gateway.add_projection(movie_id=movie_id, type=type, date=date, time=time)

    def get_movie_projections(self, movie_id):
        projections = self.projections_gateway.select_movie_projections(movie_id)

        projection_list = []
        for projection in projections:
            projection_list.append(projection)

        return projection_list

    def get_movie_projections_by_date(self, movie_id, projection_date):
        projections = self.projections_gateway.select_movie_projections(movie_id, projection_date)

        projection_list = []
        for projection in projections:
            projection_list.append(projection)

        return projection_list

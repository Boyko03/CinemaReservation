from .models import ReservationModel
from db import Database
from projections.models import ProjectionsModel


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel
        self.db = Database()

    def take_seat(self, projection, row, col, hall):
        query = """
        UPDATE Projections
        SET hall = ?
        WHERE id = ?;
        """

        hall[row][col] = 'X'
        projection.hall = str(hall)

        self.db.cursor.execute(query, (projection.hall, projection.id))

    def commit(self):
        self.db.connection.commit()

    def get_projections(self, movie_id):
        query = '''
        SELECT * FROM Projections WHERE movie_id = ?;
        '''

        self.db.cursor.execute(query, (movie_id,))

        projections = self.db.cursor.fetchall()

        projection_list = []
        for projection in projections:
            project = ProjectionsModel(id=projection[0],
                                       movie_id=projection[1],
                                       type=projection[2],
                                       date=projection[3],
                                       time=projection[4],
                                       hall=projection[5])

            free_spaces = 0
            for row in project.hall:
                free_spaces += row.count('.')
            project.free_spaces = free_spaces

            projection_list.append(project)

        return projection_list

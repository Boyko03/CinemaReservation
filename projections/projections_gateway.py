from db import Database
from projections.models import ProjectionsModel


from settings import empty_hall


class ProjectionsGateway:
    def __init__(self):
        self.model = ProjectionsModel
        self.db = Database()

    def add_projection(self, movie_id, projection_type, projection_date, projection_time):
        query = '''
        INSERT INTO Projections
        (movie_id, type, date, time, hall)
        VALUES(?, ?, ?, ?, ?)
        '''

        self.db.cursor.execute(query, (movie_id, projection_type, projection_date, projection_time, empty_hall))

        self.db.connection.commit()
        self.db.connection.close()

    def select_movie_projections(self, movie_id, projection_date=None):
        if projection_date is not None:
            query = '''
            SELECT * FROM Projections WHERE movie_id = ? AND date = ?;
            '''
            self.db.cursor.execute(query, (movie_id, projection_date))

        else:
            query = '''
            SELECT * FROM Projections WHERE movie_id = ?;
            '''
            self.db.cursor.execute(query, (movie_id,))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        return projections

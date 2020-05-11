from db import Database
from projections.models import ProjectionsModel


class ProjectionsGateway:
    def __init__(self):
        self.model = ProjectionsModel
        self.db = Database()

    def add_projection(self, movie_id, projection_type, projection_date, projection_time):
        query = '''
        INSERT INTO Projections(movie_id, type, date, time) VALUES(?,?,?,?)
        '''

        self.db.cursor.execute(query, (movie_id, projection_type, projection_date, projection_time))

        self.db.connection.commit()
        self.db.connection.close()

    def select_movie_projections(self, movie_id):
        query = '''
        SELECT * FROM Projections WHERE movie_id = ?;
        '''

        self.db.cursor.execute(query, (movie_id,))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        return projections

    def select_movie_projections_by_date(self, movie_id, projection_date):
        query = '''
        SELECT * FROM Projections WHERE movie_id = ? AND date = ?;
        '''

        self.db.cursor.execute(query, (movie_id, projection_date))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        return projections

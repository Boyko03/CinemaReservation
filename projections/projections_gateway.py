from ..db import Database
from .models import ProjectionsModel


class ProjectionsGateway:
    def __init__(self):
        self.model = ProjectionsModel()
        self.db = Database()

    def create(self, movie_id, type, date, time):
        query = '''
        INSERT INTO Projections(movie_id, type, date, time) VALUES(?,?,?,?)
        '''

        self.db.cursor.execute(query, (movie_id, type, date, time))

        self.db.connection.commit()
        self.db.connection.close()

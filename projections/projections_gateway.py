from db import Database
from projections.models import ProjectionsModel
from movies.views import MovieView


from settings import empty_hall


class ProjectionsGateway:
    def __init__(self):
        self.model = ProjectionsModel
        self.db = Database()

    def add_projection(self, movie_id, type, date, time):
        query = '''
        INSERT INTO Projections
        (movie_id, type, date, time, hall)
        VALUES(?, ?, ?, ?, ?)
        '''

        self.db.cursor.execute(query, (movie_id, type, date, time, empty_hall))

        self.db.connection.commit()
        self.db.connection.close()

    def show_movie_projections(self):
        MovieView().print_movies()

        movie_id = input('Choose movie id: ')
        print('\n')

        query = '''
        SELECT * FROM Projections WHERE movie_id = ?;
        '''

        self.db.cursor.execute(query, (movie_id,))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        projection_list = []
        for projection in projections:
            project = self.model(id=projection[0],
                                 movie_id=projection[1],
                                 type=projection[2],
                                 date=projection[3],
                                 time=projection[4],
                                 hall=projection[5])
            projection_list.append(project)

        return projection_list

    def show_movie_projections_by_date(self):
        MovieView().print_movies()

        movie_id = input('Choose movie id: ')
        date = input('Date:(yyyy-mm-dd): ')
        print('\n')

        query = '''
        SELECT * FROM Projections WHERE movie_id = ? AND date = ?;
        '''

        self.db.cursor.execute(query, (movie_id, date))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        projection_list = []
        for projection in projections:
            project = self.model(id=projection[0],
                                 movie_id=projection[1],
                                 type=projection[2],
                                 date=projection[3],
                                 time=projection[4],
                                 hall=projection[5])
            projection_list.append(project)

        return projection_list

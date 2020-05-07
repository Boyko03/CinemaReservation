from db import Database
from projections.models import ProjectionsModel
from movies.movies_gateway import MovieGateway


class ProjectionsGateway:
    def __init__(self):
        self.model = ProjectionsModel()
        self.db = Database()

    def add_projection(self, movie_id, type, date, time):
        query = '''
        INSERT INTO Projections(movie_id, type, date, time) VALUES(?,?,?,?)
        '''

        self.db.cursor.execute(query, (movie_id, type, date, time))

        self.db.connection.commit()
        self.db.connection.close()

    def show_movie_projections(self):
        print(MovieGateway.show_movies())

        movie_id = input('Choose movie id: ')

        query = '''
        SELECT * FROM Projections WHERE movie_id = ? ORDER BY date;
        '''

        self.db.cursor.execute(query, (movie_id,))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        projection_list = []
        for projection in projections:
            project = self.model(projection[0], projection[1], projection[2], projection[3], projection[4])
            projection_list.append(project)

        return projection_list

    def show_movie_projections_by_date(self):
        print(MovieGateway.show_movies())

        movie_id = input('Choose movie id: ')
        date = input('Date:(yyyy-mm-dd): ')

        query = '''
        SELECT * FROM Projections WHERE movie_id = ? AND date = ?;
        '''

        self.db.cursor.execute(query, (movie_id, date))

        projections = self.db.cursor.fetchall()

        self.db.connection.close()

        projection_list = []
        for projection in projections:
            project = self.model(projection[0], projection[1], projection[2], projection[3], projection[4])
            projection_list.append(project)

        return projection_list


# def main():
#     project = ProjectionsGateway()
#     project.show_movie_projections()


# if __name__ == '__main__':
#     main()

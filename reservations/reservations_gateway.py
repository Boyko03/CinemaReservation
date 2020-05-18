from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from .models import Reservations
from projections.models import Projections


class ReservationGateway:
    def __init__(self):
        self.model = Reservations

        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        self.session = Session()

    def take_seat(self, projection, row, col, hall):
        hall[row][col] = 'X'
        projection.hall = str(hall)

        self.session.query(Projections).filter(Projections.id == projection.id).update({Projections.hall: projection.hall})


    def commit(self):
        self.session.commit()

    def get_projections(self, movie_id):
        projections = self.session.query(Projections).filter(Projections.movie_id == movie_id).all()

        projection_list = []
        for projection in projections:
            project = projection

            free_spaces = 0
            for row in project.hall:
                free_spaces += row.count('.')
            project.free_spaces = free_spaces

            projection_list.append(project)

        return projection_list

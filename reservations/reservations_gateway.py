from .models import Reservations
from projections.models import Projections


class ReservationGateway:
    def __init__(self):
        self.model = Reservations

    def take_seat(self, projection, row, col, hall):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        hall[row][col] = 'X'
        projection.hall = str(hall)

        session.query(self.model).filter(self.model.id == projection.id).update({self.model.hall: projection.hall})


    def commit(self):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        session.commit()

    def get_projections(self, movie_id):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        projections = session.query(Projections).filter(Projections.movie_id == movie_id).all()

        projection_list = []
        for projection in projections:
            project = Projections(id=projection[0],
                                  movie_id=projection[1],
                                  projection_type=projection[2],
                                  projection_date=projection[3],
                                  projection_time=projection[4],
                                  hall=projection[5])

            free_spaces = 0
            for row in project.hall:
                free_spaces += row.count('.')
            project.free_spaces = free_spaces

            projection_list.append(project)

        return projection_list

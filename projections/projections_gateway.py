from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projections.models import Projections

from settings import empty_hall


class ProjectionsGateway:
    def __init__(self):
        self.model = Projections

    def add_projection(self, movie_id, projection_type, projection_date, projection_time):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        print("Adding new projection to the database via the session object")

        new_projection = self.model(movie_id=movie_id,
                                    projection_type=projection_type,
                                    projection_date=projection_date,
                                    projection_time=projection_time,
                                    hall=empty_hall)

        session.add(new_projection)
        session.commit()

    def select_movie_projections(self, movie_id, projection_date=None):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        if projection_date is not None:
            projections = session.query(Projections).filter(Projections.movie_id == movie_id,
                                                            Projections.projection_date == projection_date).all()
        else:
            projections = session.query(Projections).filter(Projections.movie_id == movie_id).all()

        return projections

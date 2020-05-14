from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movies.models import Movies


class MovieGateway:
    def __init__(self):
        self.model = Movies

    def add_movie(self, name, rating):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        print("Adding new movies to the database via the session object")

        new_movie = self.model(name=name, rating=rating)

        session.add(new_movie)
        session.commit()

    def select_movies(self):
        engine = create_engine("sqlite:///cinema.db")

        Session = sessionmaker(bind=engine)

        session = Session()

        all_movies = session.query(Movies).all()

        return all_movies

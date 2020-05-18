import sys
import os

from settings import empty_hall

from db import Base, engine, session
from movies.models import Movies
from projections.models import Projections
from users.models import Users
from reservations.models import Reservations

from index_view import welcome, list_user_options, user_choose_command


class Application:
    @classmethod
    def build(self):
        Base.metadata.create_all(engine)
        session.add_all([
            Movies(name='The Hunger Games: Catching Fire', rating=7.9),
            Movies(name='Wreck-It Ralph', rating=7.8),
            Movies(name='Her', rating=8.3)])
        session.add_all([
            Projections(movie_id=1, projection_type='3D',
                        projection_date='2020-04-01',
                        projection_time='19:10', hall=str(empty_hall)),
            Projections(movie_id=1, projection_type='2D',
                        projection_date='2020-04-01',
                        projection_time='19:00', hall=str(empty_hall)),
            Projections(movie_id=1, projection_type='4DX',
                        projection_date='2020-04-02',
                        projection_time='21:00', hall=str(empty_hall)),
            Projections(movie_id=3, projection_type='2D',
                        projection_date='2020-04-05',
                        projection_time='20:20', hall=str(empty_hall)),
            Projections(movie_id=2, projection_type='3D',
                        projection_date='2020-04-02',
                        projection_time='22:00', hall=str(empty_hall)),
            Projections(movie_id=2, projection_type='2D',
                        projection_date='2020-04-02',
                        projection_time='19:30', hall=str(empty_hall))])

        session.commit()

        print('Done.')

    @classmethod
    def start(self):
        user = None
        while user is None:
            user = welcome()

        os.system('clear')
        print(f'Hello, {user.username}')

        list_user_options()
        # user_choose_command()
        user_choose_command(user)


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(
            f'Unknown command {command}. Valid ones are "build" and "start"')

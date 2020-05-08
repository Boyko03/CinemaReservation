import sys
import os

from db import Database
from db_schema import CREATE_USERS, CREATE_MOVIES, CREATE_PROJECTIONS, CREATE_RESERVATIONS
from db_schema import INSERT_INTO_MOVIES, INSERT_INTO_PROJECTIONS

from index_view import welcome, list_user_options, user_choose_command


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_MOVIES)
        db.cursor.execute(CREATE_PROJECTIONS)
        db.cursor.execute(CREATE_RESERVATIONS)

        db.cursor.execute(INSERT_INTO_MOVIES)
        db.cursor.execute(INSERT_INTO_PROJECTIONS)

        db.connection.commit()
        db.connection.close()

        print('Done.')

    @classmethod
    def start(self):
        welcome()
        os.system('clear')
        list_user_options()
        user_choose_command()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')

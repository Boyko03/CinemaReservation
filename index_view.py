from users.views import UserViews
import os
from settings import user_list_options

from movies.views import MovieView
from projections.views import ProjectionViews


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n\n  Input: '))
    user_views = UserViews()

    if command == 1:
        print('\n')
        return user_views.login()

    if command == 2:
        print('\n')
        return user_views.signup()

    raise ValueError(f'Unknown command {command}.')


def list_user_options():
    print('You can choose from the following commands:')
    print('-------------------------------------------\n')
    for command in user_list_options:
        print(command)

    print('\n-------------------------------------------\n')


def user_choose_command():
    # TODO all functions
    command = ''
    while command != 'exit':
        command = input('> ')
        os.system('clear')
        if command == 'show movies':
            MovieView().print_movies()
        if command == 'show movie projections':
            ProjectionViews().print_all_projections()
        if command == 'show movie projections by date':
            ProjectionViews().print_projections_by_date()
        if command == 'make reservation':
            make_reservation()
        if command == 'finalize':
            finalize()
        if command == 'cancel reservation':
            cancel_reservation()
        if command == 'help':
            list_user_options()
        if command == 'cancel':
            cancel()

    print('\nGoodbye!\n')

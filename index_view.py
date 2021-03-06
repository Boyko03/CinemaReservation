import os
from settings import user_list_options

from users.views import UserViews
from movies.views import MovieView
from projections.views import ProjectionViews
from reservations.views import ReservationView


def welcome():
    print('Welcome to HackCinema!')

    print('Choose a command:')
    print('1 - log in')
    print('2 - sign up')
    print('3 - exit')

    command = input('> ')

    while not command.isalnum() or command not in ['1', '2', '3']:
        print('\nChoose a command:')
        print('1 - log in')
        print('2 - sign up')
        print('3 - exit')
        command = int(input('> '))

    user_views = UserViews()
    command = int(command)

    if command == 1:
        return user_views.login()

    elif command == 2:
        return user_views.signup()

    elif command == 3:
        exit()


def list_user_options():
    print('You can choose from the following commands:')
    print('-------------------------------------------\n')
    for command in user_list_options:
        print(command)

    print('\n-------------------------------------------\n')


def user_choose_command(user):
# def user_choose_command():
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
        if command == 'add new movie':
            MovieView().create_new_movie()
        if command == 'make reservation':
            ReservationView().make_reservation(user)
        if command == 'cancel reservation':
            ReservationView().cancel_reservation(user)
        if command == 'help':
            list_user_options()

    print('\nGoodbye!\n')

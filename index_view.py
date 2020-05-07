# from users.views import UserViews

from settings import user_list_options

from movies.views import MovieView
from projections.views import ProjectionViews


# def welcome():
#     print('Welcome to HackCinema!')
#     command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
#     user_views = UserViews()

#     if command == 1:
#         return user_views.login()

#     if command == 2:
#         return user_views.signup()

#     raise ValueError(f'Unknown command {command}.')


def list_user_options():
    print('You can choose from the following commands:')
    print('-------------------------------------------')
    for command in user_list_options:
        print(command)

    print('-------------------------------------------')


def user_choose_command():
    # TODO all functions
    command = ''
    while command != 'exit':
        command = input('> ')
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

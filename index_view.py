from users.views import UserViews

from settings import user_list_options


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()

    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()

    raise ValueError(f'Unknown command {command}.')


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
            show_movies()
        if command == 'show movie projections <movie_id> [<date>]':
            show_movies_projections(movie_id, date=None)
        if command == 'make reservation':
            make_reservation()
        if command == 'finalize':
            finalize()
        if command == 'cancel reservation <name>':
            cancel_reservation(reservation_name)
        if command == 'help':
            help()  # list_user_options()?
        if command == 'cancel':
            cancel()

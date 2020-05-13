from users.views import UserViews


def login_required(func):
    def inner(self, user, *args, **kwargs):
        if user is None:
            print('You need to be a user in the system to make reservations!')
            UserViews().signup()
        return func(self, user, *args, **kwargs)
    return inner

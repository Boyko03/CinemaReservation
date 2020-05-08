from .controllers import UserController


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        while True:
            username = input('Username: ')
            password = input('Password: ')

            while not self.controller.validate_password(password):
                print('Invalid password!')
                password = input('Password: ')

            user = self.controller.try_to_log_in(username, password)
            if not user:
                print('Wrong email or password.')
            else:
                print(f'Hello, {user.name}')
                return user

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')

        while not self.controller.validate_password(password):
            print('Invalid password!')
            password = input('Password: ')

        user = self.controller.create(username, password)
        print(f'Hello, {user.name}')
        return user

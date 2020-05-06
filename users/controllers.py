from .users_gateway import UserGateway


class UserController:
    def __init__(self):
        self.users_gateway = UserGateway()

    def validate_password(self, password):
        if len(password) < 8:
            return False

        letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

        ok = 0
        for letter in letters:
            if letter in password:
                ok = 1
                break
        if not ok:
            return False

        special_symbols = [
            symbol for symbol in ' !\"#$%&\'()*+,-./:;<=>?@[]\\^`{|}~']

        ok = 0
        for symbol in special_symbols:
            if symbol in password:
                ok = 1
                break

        return True if ok else False

    def try_to_log_in(self, username, password):
        return self.users_gateway.login(username, password)

    def create(self, username, password):
        if self.try_to_log_in(username, password):
            return
        else:
            return self.users_gateway.sign_up(username, password)

import unittest


from .users_gateway import *
from db_schema import CREATE_USERS


class SignUpTests(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.db.cursor.execute(CREATE_USERS)

    def tearDown(self):
        self.db.close()

    def test_sign_up_returns_user_of_type_UserModel(self):
        name = 'TestUser'
        password = 'password'
        users_gateway = UserGateway()

        user = users_gateway.sign_up(name, password)

        self.assertEqual(type(user), UserModel)


class LoginTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

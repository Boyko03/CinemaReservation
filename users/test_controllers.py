import unittest


from .controllers import UserController


class ValidatePasswordTests(unittest.TestCase):
    def setUp(self):
        self.user_controller = UserController()

    def test_returns_false_when_password_is_shorter_than_8_symbols(self):
        password = 'abcd'

        self.assertFalse(self.user_controller.validate_password(password))

    def test_returns_false_when_password_does_not_contain_uppercase(self):
        password = 'asdfghjkl'

        self.assertFalse(self.user_controller.validate_password(password))

    def test_returns_false_when_password_does_not_contain_specials(self):
        password = 'AsdfGhjK'

        self.assertFalse(self.user_controller.validate_password(password))

    def test_returns_true_if_password_is_valid(self):
        password = 'asDf+ghjK'

        self.assertTrue(self.user_controller.validate_password(password))


if __name__ == '__main__':
    unittest.main()

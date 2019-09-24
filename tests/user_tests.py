import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='bea' email = "wambui@gmail.com",password='wambui')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure not None)

    def test_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.pass_secure

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('wambui'))
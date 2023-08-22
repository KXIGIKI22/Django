import unittest
from user import User

class TestUserModel(unittest.TestCase):

    def test_create_user(self):
        user = User.objects.create(name='John', email='john@example.com')
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, 'John')
        self.assertEqual(user.email, 'john@example.com')

if __name__ == '__main__':
    unittest.main()
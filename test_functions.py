import unittest
from user import get_users, create_user

class TestFunctions(unittest.TestCase):

    def test_get_users(self):
        users = get_users()
        self.assertIsInstance(users, list)
        self.assertTrue(len(users) >= 0)

    def test_create_user(self):
        user_data = {
            'name': 'John',
            'email': 'john@example.com'
        }
        response = create_user(user_data)
        self.assertEqual(response, 'User created')

if __name__ == '__main__':
    unittest.main()
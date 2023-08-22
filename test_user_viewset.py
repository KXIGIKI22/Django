from django.test import TestCase
from rest_framework.test import APIRequestFactory
from book import User
from userviews import UserViewSet

class TestUserViewSet(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserViewSet.as_view({'get': 'list', 'post': 'create'})
        self.user_data = {
            'name': 'John',
            'email': 'john@example.com'
        }

    def test_create_user(self):
        request = self.factory.post('/users/', self.user_data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

if __name__ == '__main__':
    unittest.main()
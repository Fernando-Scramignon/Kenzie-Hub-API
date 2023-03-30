from rest_framework.test import APITestCase
from rest_framework import status

from works.models import Work
from users.models import User

class WorkTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.creation_url = '/api/works/'
        cls.login_url = '/api/login/'

        cls.work_data = {
            'title': 'kenzie hub',
            'deploy_url': 'www.deploy.com',
            'description': 'a cool desc'
        }

        cls.user_data = {
            'name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'contact': 'someLinkedin',
            'password': '1234'
        }

        cls.user_data_login = {
            'email': cls.user_data['email'],
            'password': cls.user_data['password']
        }

        cls.user = User.objects.create_user(
            **cls.user_data
        )

        cls.user.save()


    def test_can_create_work(self):
        login_response = self.client.post(self.login_url, self.user_data_login)
        token = login_response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token
        )

        expected_response_fields = [
            'id', 'title', 'deploy_url',
            'description', 'created_at', 'updated_at'
        ]

        response = self.client.post(self.creation_url, self.work_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        is_response_correct = True
        data = response.data
        for key in data.keys():
            if key not in expected_response_fields:
                is_response_correct = False
        
        self.assertTrue(is_response_correct)
    
    def test_can_not_create_unauthenticated(self):
        response = self.client.post(self.creation_url, self.work_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_can_not_create_work_with_same_title(self):
        login_response = self.client.post(self.login_url, self.user_data_login)
        token = login_response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token
        )

        _ = self.client.post(self.creation_url, self.work_data)
        response = self.client.post(self.creation_url, self.work_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
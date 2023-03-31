import ipdb
# rest framework
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from rest_framework import status
from users.models import User

from utils.functions import client_login

# remember to refactor the tests
class TechCreationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.creation_url = '/api/techs/'
        cls.listing_url = cls.creation_url
        cls.login_url = '/api/login/'

        cls.user_data = {
                'name':'John Doe',
                'email': 'johndoe@gmail.com',
                'contact': 'someLinkedin',
                'password': '1234'
        }

        cls.user_data_alt = {
            'name': 'Jack Smith',
            'email': 'jacksmith@gmail.com',
            'contact': 'someLinkedin',
            'password': '1234'
        }

        cls.user_data_login = {
            'email': cls.user_data['email'],
            'password': cls.user_data['password']
        }

        cls.user_data_login_alt = {
            'email': cls.user_data_alt['email'],
            'password': cls.user_data_alt['password']
        }
        
        cls.user = User.objects.create_user(
            **cls.user_data
        )

        cls.user_alt = User.objects.create_user(
            **cls.user_data_alt
        )

        cls.user.save()
        cls.user_alt.save()

        cls.tech_data = {
            'title': 'React',
            'description': 'Most famous front end framework',
            'status': 'Intermediário',
        }

        cls.tech_data_without_status = {
            'title': 'Java',
            'description': 'The language that created minecraft',
            }

    def test_creation_with_defaults(self):
        login_response = self.client.post(self.login_url, self.user_data_login)
        token = login_response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token
        )

        expected_response_fields = ['id', 'title', 'status', 'created_at', 'updated_at']
        is_response_correct = True

        response = self.client.post(self.creation_url, self.tech_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.data
        for key in data.keys():
            if key not in expected_response_fields:
                is_response_correct = False

        self.assertTrue(is_response_correct)
       

    def test_creation_without_authentication(self):
        response = self.client.post(self.creation_url, self.tech_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creating_without_status(self):
        login_response = self.client.post(self.login_url, self.user_data_login)
        token = login_response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token
        )

        expected_status_field = 'Iniciante'

        response = self.client.post(self.creation_url, self.tech_data_without_status)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], expected_status_field)

    def test_creating_tech_with_same_title(self):
        login_response = self.client.post(self.login_url, self.user_data_login)
        token = login_response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token
        )

        _ = self.client.post(self.creation_url, self.tech_data)

        response = self.client.post(self.creation_url, self.tech_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_techs_should_not_be_unique(self):
        # logs in as first user
        client_login(self.client, self.user_data_login, self.login_url)

        _ = self.client.post(self.creation_url, self.tech_data)

        # logs in as second user
        client_login(self.client, self.user_data_login_alt, self.login_url)

        response = self.client.post(self.creation_url, self.tech_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_can_only_list_own_tech(self):

        client_login(self.client, self.user_data_login, self.login_url)
        creation_response = self.client.post(self.creation_url, self.tech_data)
        listing_response = self.client.get(self.listing_url)
        self.assertEqual(len(listing_response.data), 1)
        self.assertEqual(listing_response.data[0]['title'], self.tech_data['title'])

        client_login(self.client, self.user_data_login_alt, self.login_url)
        creation_response = self.client.post(self.creation_url, self.tech_data_without_status)
        listing_response = self.client.get(self.listing_url)
        self.assertEqual(len(listing_response.data), 1)
        self.assertEqual(listing_response.data[0]['title'], self.tech_data_without_status['title'])

from rest_framework.test import APITestCase
from rest_framework import status

from works.models import Work
from users.models import User

import ipdb

class WorkTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.creation_url = '/api/works/'
        cls.listing_url = '/api/works/'
        cls.login_url = '/api/login/'

        cls.work_data = {
            'title': 'kenzie hub',
            'deploy_url': 'www.deploy.com',
            'description': 'a cool desc'
        }

        cls.work_data_alt = {
            'title': 'some api',
            'deploy_url': 'www.api.com',
            'description': 'a bad description'
        }

        cls.user_data = {
            'name': 'John Doe',
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
    
    def test_can_not_create_work_with_same_title_under_the_same_user(self):
        login_response = self.client.post(self.login_url, self.user_data_login)
        token = login_response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + token
        )

        _ = self.client.post(self.creation_url, self.work_data)
        response = self.client.post(self.creation_url, self.work_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_work_should_not_be_unique(self):
        # login as first user and creates work
        client_login(self.client, self.user_data_login, self.login_url)
        creation_response = self.client.post(self.creation_url, self.work_data)
        self.assertEqual(creation_response.status_code, status.HTTP_201_CREATED)

        # login as second user and creates work with same title as the above one
        client_login(self.client, self.user_data_login_alt, self.login_url)
        creation_response = self.client.post(self.creation_url, self.work_data)
        self.assertEqual(creation_response.status_code, status.HTTP_201_CREATED)

    def test_can_only_list_own_work(self):        
        # logs in as first user
        client_login(self.client, self.user_data_login, self.login_url)

        # creates as first user 
        creation_response = self.client.post(self.creation_url, self.work_data)
        listing_response = self.client.get(self.listing_url)

        self.assertEqual(len(listing_response.data), 1)
        self.assertEqual(listing_response.data[0]['title'], self.work_data['title'])

        # logs in as second user
        client_login(self.client, self.user_data_login_alt, self.login_url)        

        # creates work as second user
        creation_response = self.client.post(self.creation_url, self.work_data_alt)
        listing_response = self.client.get(self.listing_url)

        self.assertEqual(len(listing_response.data), 1)
        self.assertEqual(listing_response.data[0]['title'], self.work_data_alt['title'])



def client_login(client, login_data, login_url):
    login_response = client.post(login_url, login_data)
    token = login_response.data['access']

    client.credentials(
        HTTP_AUTHORIZATION='Bearer ' + token
    )
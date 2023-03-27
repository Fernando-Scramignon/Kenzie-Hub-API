import pdb
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User
# from rest_framework.exceptions import ErrorDetail

class TechCreationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.creation_url = '/api/techs/'

        cls.user = User.objects.create_user(
            **{
                'name':'John Doe',
                'email': 'johndoe@gmail.com',
                'contact': 'someLinkedin',
                'password': '1234'
            }
        )
        cls.user.save()

        cls.tech_data_with_defaults = {
            'title': 'React',
            'description': 'Most famous front end framework',
            'status': 'Intermediário',
            'user': cls.user
        }

    def test_creation_with_defaults(self):
        response = self.client.post(self.creation_url, self.tech_data_with_defaults)


        # self.assertIsNotNone()

    def test_creation_without_defaults(self):
        pass

    def test_empty_creation(self):
        pass

    def test_with_some_missing_fields(self):
        pass
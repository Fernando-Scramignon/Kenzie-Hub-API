import ipdb
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.exceptions import ErrorDetail

class UsersRegistrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.register_url = '/api/users/'

        cls.user_data_with_defaults = {
            'name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'contact': 'someLinkedin',
            'password': '1234',
            'course_module': 'Primeiro módulo',
            'bio': 'I am a pretty normal guy',
        }


        cls.user_data_wrong_types = {
            'name': True,
            'email': 'johndoe@gmail.com',
            'contact': True,
            'password': False,
            'course_module': 'Primeiro módulo',
            'bio': 213,
        }

        cls.user_data_without_defaults = {
            'name': 'Jack Smith',
            'email': 'jack@gmail.com',
            'contact': 'someLinkedin2',
            'password': '1234',
        }

        cls.user_data_long_strings = {
            'name': 'John' * 550,
            'email': 'john@gmail.com' * 550,
            'password': '1234' * 550,
            'contact': 'someLinkedin' * 550,
            'course_module': 'Segundo módulo' * 550,
            'bio': 'bio'* 550
        }

        cls.user_data_with_missing_fields = {
            'name': 'john',
            'contact': 'linkedin'
        }

        cls.expected_return_fields = [
            'id',
            'created_at',
            'updated_at',
            'avatar_url',
            'name',
            'email',
            'contact',
            'course_module',
            'bio'
        ]

        cls.required_fields = ['name', 'email', 'password', 'contact']

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data_with_defaults)

        self.assertIsNone(response.data.get('password'))

        for field in self.expected_return_fields:
            self.assertNotEqual(response.data.get(field, -1), -1)
    
    def test_registration_without_defaults(self):
        response = self.client.post(self.register_url, self.user_data_without_defaults)

        self.assertIsNone(response.data.get('password'))

        for field in self.expected_return_fields:
            self.assertNotEqual(response.data.get(field, -1), -1)

    def test_registration_with_long_strings(self):
        response = self.client.post(self.register_url, self.user_data_long_strings)
        fields_tested = self.user_data_long_strings.keys()
        expected_error_codes = ['invalid_choice', 'max_length', 'invalid']

        for field in fields_tested:
            error_list = response.data.get(field)

            self.assertIsNotNone(error_list)

            for error in error_list:
                self.assertEqual(type(error), ErrorDetail)
                self.assertTrue(error.code in expected_error_codes)

    def test_empty_registration(self):
        response = self.client.post(self.register_url, {})
        required_fields = ['name', 'email', 'password', 'contact']
        
        expected_error_code = 'required'
        expected_status_code = 400
        
        self.assertEqual(expected_status_code, 400)
        self.assertEqual(len(response.data), len(required_fields))

        for field in required_fields:
            error_list = response.data.get(field)
            self.assertTrue(error_list)

            self.assertEqual(len(error_list), 1)

            error = error_list[0]
            self.assertEqual(type(error), ErrorDetail)

            self.assertEqual(error.code, expected_error_code)

    def test_registration_with_some_missing_fields(self):
        missing_fields = ['email', 'password']
        expected_status_code = 400
        expected_error_code = 'required'

        response = self.client.post(self.register_url, self.user_data_with_missing_fields)

        self.assertEqual(response.status_code, expected_status_code)
        self.assertEqual(len(response.data), len(missing_fields))

        for field in missing_fields:
            error_list = response.data.get(field)
            self.assertTrue(error_list)

            self.assertEqual(len(error_list), 1)

            error = error_list[0]

            self.assertEqual(type(error), ErrorDetail)

            self.assertEqual(error.code, expected_error_code)

    def test_registration_with_same_email(self):
        self.client.post(self.register_url, self.user_data_without_defaults)
        response = self.client.post(self.register_url, self.user_data_without_defaults)

        expected_error_code = 'unique'

        expected_status_code = 400
        self.assertEqual(response.status_code, expected_status_code)

        error_list = response.data.get('email')
        self.assertTrue(error_list)
        self.assertEqual(len(error_list), 1)

        error = error_list[0]
        self.assertEqual(type(error), ErrorDetail)

        self.assertEqual(error.code, expected_error_code)

    
    def test_registration_course_module_choices(self):
        user_data_wrong_course_module = {**self.user_data_without_defaults, 'course_module': 'wrong choice'}
        response = self.client.post(self.register_url, user_data_wrong_course_module)
        
        expected_error_code = 'invalid_choice'
        expected_status_code = 400

        self.assertEqual(response.status_code, expected_status_code)
    
        error_list = response.data.get('course_module')
        self.assertTrue(error_list)
        self.assertEqual(len(error_list), 1)

        error = error_list[0]
        self.assertEqual(type(error), ErrorDetail)

        self.assertEqual(error.code, expected_error_code)

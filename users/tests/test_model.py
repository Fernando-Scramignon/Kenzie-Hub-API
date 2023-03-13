from django.test import TestCase

from ..models import User

class UserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data_with_defaults = {
            'name': 'John Doe',
            'email': 'johndoe@gmail.com',
            'contact': 'someLinkedin',
            'password': '1234',
            'course_module': 'Primeiro módulo',
            'bio': 'I am a pretty normal guy'
        }

        cls.user_data_without_defaults = {
            'name': 'Jack Smith',
            'email':'jack@gmail.com',
            'contact':'someLinkedin2',
            'password': '1234'
        }

        cls.defaults = {
            'bio': 'A cool bio',
            'course_module': 'Não especificado'
        }

        cls.field_expected_length = {
            'email': 256,
            'name': 256,
            'course_module': 20,
            'bio': 512,
            'contact': 256,
        }

        cls.course_module_choices = [
            'Primeiro módulo',
            'Segundo módulo',
            'Terceiro módulo',
            'Quarto módulo',
            'Não especificado'
        ]

        cls.user_with_defaults = User.objects.create_user(**cls.user_data_with_defaults)
        cls.user_without_defaults = User.objects.create_user(**cls.user_data_without_defaults)


    def test_course_modules_choices(self):
        field_choices = User._meta.get_field('course_module').choices

        for choice in self.course_module_choices:
            choice in field_choices

    def test_fields_defaults(self):
        fields = self.defaults.keys()

        for field in fields:
            self.assertEqual(User._meta.get_field(field).default, self.defaults[field])

    def test_email_unique_property(self):
        self.assertTrue(User._meta.get_field('email').unique)

    def test_avatar_url_null_property(self):
        self.assertTrue(User._meta.get_field('avatar_url').null)

    def test_max_length_rule(self):
        fields = self.field_expected_length.keys()

        for field in fields:
            self.assertEqual(User._meta.get_field(field).max_length, self.field_expected_length[field])

    def test_creation_with_defaults(self):
        self.assertEqual(self.user_with_defaults.name, self.user_data_with_defaults['name'])
        self.assertEqual(self.user_with_defaults.email, self.user_data_with_defaults['email'])
        self.assertEqual(self.user_with_defaults.contact, self.user_data_with_defaults['contact'])
        self.assertEqual(self.user_with_defaults.course_module, self.user_data_with_defaults['course_module'])
        self.assertEqual(self.user_with_defaults.bio, self.user_data_with_defaults['bio'])

        self.assertTrue(self.user_with_defaults.created_at)
        self.assertTrue(self.user_with_defaults.updated_at)
        self.assertTrue(self.user_with_defaults.id)

        self.assertIsNone(self.user_with_defaults.avatar_url)

    def test_creation_without_defaults(self):
        self.assertEqual(self.user_without_defaults.name, self.user_data_without_defaults['name'])
        self.assertEqual(self.user_without_defaults.email, self.user_data_without_defaults['email'])
        self.assertEqual(self.user_without_defaults.contact, self.user_data_without_defaults['contact'])
        self.assertEqual(self.user_without_defaults.course_module, self.defaults['course_module'])
        self.assertEqual(self.user_without_defaults.bio, self.defaults['bio'])

        self.assertTrue(self.user_without_defaults.created_at)
        self.assertTrue(self.user_without_defaults.updated_at)
        self.assertTrue(self.user_without_defaults.id)

        self.assertIsNone(self.user_without_defaults.avatar_url)
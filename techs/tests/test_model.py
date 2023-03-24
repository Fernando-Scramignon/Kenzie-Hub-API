from django.test import TestCase
from django.db.models import Model
from django.core.exceptions import ValidationError

from ..models import Tech
import pdb

class TechModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tech_data = {'title': 'React', 'status': 'Iniciante'}
        cls.tech_data_wrong_status = {**cls.tech_data, 'status': 'wrong status'}
        cls.tech = Tech.objects.create(**cls.tech_data)
        cls.status_choices = ['Iniciante', 'Intermediário', 'Avançado']

    def test_tech_creation(self):
        self.assertEqual(self.tech.title, self.tech_data['title'])
        self.assertEqual(self.tech.status, self.tech_data['status'])

    def test_id_primary_key(self):
        self.assertTrue(Tech._meta.get_field('id').primary_key)
    
    def test_id_not_editable(self):
        self.assertTrue(Tech._meta.get_field('id').primary_key)

    def test_max_length_property(self):
        self.assertTrue(Tech._meta.get_field('title').max_length)
        self.assertTrue(Tech._meta.get_field('status').max_length)
    
    def test_status_choices(self):
        field_choices = Tech._meta.get_field('status').choices
        for index, choice in enumerate(field_choices):
            self.assertTrue(choice, field_choices[index][0])
    


        
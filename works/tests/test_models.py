from django.test import TestCase
from django.db.models import Model

from uuid import uuid4
from uuid import UUID

from ..models import Work
import pdb

class WorkModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.work_data = {'title': 'kenzie-hub', 'deploy_url': 'www.coolurl.com', 'description': 'A cool description'}
        cls.work = Work.objects.create(**cls.work_data)

    def test_work_creation(self):
        work = self.work
        work_data = self.work_data
        work_data_keys = work_data.keys()

        for key in work_data_keys:
            self.assertEqual(getattr(work, key, None), work_data[key])
        
        self.assertTrue(hasattr(work, 'created_at'))
        self.assertTrue(hasattr(work, 'updated_at'))
        self.assertTrue(hasattr(work, 'id'))
    
    def test_max_length_fields(self):
        expected_output = {'title': 256, 'deploy_url': 512, 'description': 512}
        tested_fields = expected_output.keys()

        for field in tested_fields:
            self.assertEqual(expected_output[field], Work._meta.get_field(field).max_length)
    
    def test_uneditable_fields(self):
        tested_fields = ['id', 'created_at', 'updated_at']

        for field in tested_fields:
            self.assertFalse(Work._meta.get_field(field).editable)
    
    def test_id_is_uuid(self):
        work = self.work
        id = getattr(work, 'id', False)

        self.assertTrue(id)
        self.assertIsInstance(self.work.id, UUID)
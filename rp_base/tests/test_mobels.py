from django.test import TestCase
from rp_base.models import Place


class TestPlaceModel(TestCase):
    def setUp(self):
        self.place = Place.objects.create(name = 'Test')

    def test_model_str(self):
        self.assertEqual(self.place.name, 'Test')

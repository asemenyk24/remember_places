from django.test import TestCase, Client
from django.urls import reverse
from rp_base.models import Place


class PlaceView(TestCase):
    def setUp(self):
        self.place1 = Place.objects.create(name = 'Testing')
        self.client = Client()
        self.new_place_url = reverse('rp_base:new_place')
        self.edit_place_url = reverse('rp_base:edit_place', kwargs = {'place_id': self.place1.id})
        self.delete_place_url = reverse('rp_base:delete_place', kwargs = {'place_id': self.place1.id})

    def test_new_place_POST(self):
        response = self.client.post(self.new_place_url, {'name': 'Testing'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.place1.name, 'Testing')

    def test_edit_place_POST(self):
        response = self.client.post(self.edit_place_url, {'name': 'Testing'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.place1.name, 'Testing')

    def test_delete_place_POST(self):
        response = self.client.delete(self.delete_place_url, {'name': 'Testing'})
        self.assertEquals(response.status_code, 302)

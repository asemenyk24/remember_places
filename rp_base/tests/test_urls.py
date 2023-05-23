from django.test import TestCase
from django.urls import reverse, resolve
from rp_base.views import places, new_place, delete_place, edit_place
from rp_base.models import Place


class TestUrls(TestCase):
    def test_places_url_resolves(self):
        url = reverse('rp_base:places')
        self.assertEquals(resolve(url).func, places)

    def test_new_place_url_resolves(self):
        url = reverse('rp_base:new_place')
        self.assertEquals(resolve(url).func, new_place)

    def test_edit_place_url_resolves(self):
        place = Place.objects.create(name = 'Testing')
        url = reverse('rp_base:edit_place', kwargs = {'place_id': place.id})
        self.assertEquals(resolve(url).func, edit_place)

    def test_delete_place_url_resolves(self):
        place = Place.objects.create(name = 'Testing')
        url = reverse('rp_base:delete_place', kwargs = {'place_id': place.id})
        self.assertEquals(resolve(url).func, delete_place)\

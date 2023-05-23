from django.test import SimpleTestCase
from rp_base.forms import PlaceForm
from mapwidgets.widgets import GooglePointFieldWidget


class TestForms(SimpleTestCase):
    def test_place_form_valid_data(self):
        form = PlaceForm(data ={
            'name': 'Krasnoyarsk',
            'description': 'Testing',
        })
        widget = GooglePointFieldWidget()
        self.assertTrue(form.is_valid())
        self.assertEqual(hasattr(widget, 'settings'), True)

    def test_place_form_empty(self):
        form = PlaceForm(data ={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

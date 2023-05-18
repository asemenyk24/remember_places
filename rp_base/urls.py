"""Handling URL schematics for rp_base."""

from django.urls import path
from . import views

app_name = 'rp_base'
urlpatterns = [
    # Home page.
    path('', views.index, name = 'index'),
    # Page with the list of places.
    path('places/', views.places, name = 'places'),
    # Page for creation of the new place.
    path('new_place/', views.new_place, name = 'new_place'),
    # Place edit page.
    path('edit_place/<int:place_id>/', views.edit_place, name = 'edit_place'),
]

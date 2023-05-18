"""Handling URL schematics for rp_base."""

from django.urls import path
from . import views

app_name = 'rp_base'
urlpatterns = [
    # Home page.
    path('', views.index, name = 'index'),
]

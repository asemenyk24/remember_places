from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User

POINT = Point(56.015283, 92.893248, srid=4326)


class Place(models.Model):
    """Place, which user wants to remember."""
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    location = models.PointField(help_text="To generate the map for your location", null = True, blank = True)

    def __unicode__(self):
        """Text representation of the model."""
        return self.name

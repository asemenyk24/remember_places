from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    """Place, which user wants to remember."""
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Text representation of the model."""
        return self.name

from django.db import models


class Place(models.Model):
    """Place, which user wants to remember."""
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Text representation of the model."""
        return self.name

from .models import Place
from django.contrib.gis import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


class PlaceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': GooglePointFieldWidget}
    }


admin.site.register(Place, PlaceAdmin)

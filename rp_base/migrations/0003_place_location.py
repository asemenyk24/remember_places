# Generated by Django 4.2.1 on 2023-05-22 12:04

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rp_base', '0002_place_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text='To generate the map for your location', null=True, srid=4326),
        ),
    ]

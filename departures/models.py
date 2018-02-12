from __future__ import unicode_literals

from django.db import models


class Departure(models.Model):
    name = models.CharField(max_length=55)
    start_date = models.DateField()
    finish_date = models.DateField()
    category = models.CharField(
        max_length=25,
        choices=(
            ('Adventurous', 'Adventurous'),
            ('Classic', 'Classic'),
            ('Marine', 'Marine'),
        )
    )

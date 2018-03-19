"""
Loads data from `departures.json` into the Departure model
"""

import json
from django.db import migrations, models

def populate_departures(apps, schema_editor):
    Departure = apps.get_model('departures', 'Departure')

    with open('departures.json') as json_data:
        data = json.load(json_data)
        for d in data:
            departure = Departure(
                name=d['name'],
                start_date=d['start_date'],
                finish_date=d['finish_date'],
                category=d['category']
            )
            departure.save()


class Migration(migrations.Migration):

    dependencies = [
        ('departures', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_departures),
    ]

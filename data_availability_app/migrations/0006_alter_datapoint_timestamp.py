# Generated by Django 3.2.3 on 2023-08-25 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_availability_app', '0005_alter_datapoint_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 25, 16, 21, 53, 897008), null=True),
        ),
    ]

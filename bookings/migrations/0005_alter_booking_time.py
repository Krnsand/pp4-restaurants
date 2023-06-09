# Generated by Django 3.2.18 on 2023-03-30 14:26

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20230330_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(blank=True, choices=[(datetime.time(17, 0), '5 PM'), (datetime.time(17, 30), '5:30 PM'), (datetime.time(18, 0), '6 PM'), (datetime.time(18, 30), '6:30 PM'), (datetime.time(19, 0), '7 PM'), (datetime.time(19, 30), '7:30 PM'), (datetime.time(20, 0), '8 PM'), (datetime.time(20, 30), '8:30 PM'), (datetime.time(21, 0), '9 PM'), (datetime.time(21, 30), '9:30 PM')], default=django.utils.timezone.now, max_length=10),
        ),
    ]

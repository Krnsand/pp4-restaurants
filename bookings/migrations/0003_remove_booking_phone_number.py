# Generated by Django 3.2.18 on 2023-03-29 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20230329_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phone_number',
        ),
    ]

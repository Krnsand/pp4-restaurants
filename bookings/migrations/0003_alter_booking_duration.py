# Generated by Django 3.2.18 on 2023-03-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20230328_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='duration',
            field=models.TimeField(default='', max_length=10),
        ),
    ]

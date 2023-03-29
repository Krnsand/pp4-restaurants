# Generated by Django 3.2.18 on 2023-03-29 19:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('opens', models.TimeField()),
                ('closes', models.TimeField()),
                ('active_mon_tues', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(default='', max_length=100, unique=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, max_length=10)),
                ('time', models.TimeField(blank=True, choices=[(datetime.time(5, 0), '5 PM'), (datetime.time(5, 30), '5:30 PM'), (datetime.time(6, 0), '6 PM'), (datetime.time(6, 30), '6:30 PM'), (datetime.time(7, 0), '7 PM'), (datetime.time(7, 30), '7:30 PM'), (datetime.time(8, 0), '8 PM'), (datetime.time(8, 30), '8:30 PM'), (datetime.time(9, 0), '9 PM'), (datetime.time(9, 30), '9:30 PM')], default=django.utils.timezone.now, max_length=10)),
                ('guests', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True)),
                ('comment', models.TextField(blank=True, default='', max_length=200)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.restaurant')),
            ],
        ),
    ]

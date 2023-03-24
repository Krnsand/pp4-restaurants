from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.db.models import IntegerField, Model


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(blank=True)


TIME_CHOICES = (
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8 PM", "8 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9 PM", "9 PM"),
    ("9:30 PM", "9:30 PM"),
)


GUEST_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)


RST_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)


class Booking(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    restaurant = models.CharField(max_length=100, choices=RST_CHOICES, blank=True)
    date = models.DateField(max_length=10, default=timezone.now, blank=True)
    time = models.TimeField(max_length=10, choices=TIME_CHOICES, default=timezone.now, blank=True)
    guests = models.IntegerField(choices=GUEST_CHOICES, default=False, blank=True)
    comment = models.TextField(max_length=200, default=False, blank=True)
    # created_on = models.DateTimeField(auto_now=True)

    # class Meta():
    #    """To display the recipes by created_on in descending order"""
    #    ordering = ['-created_on']

    def __str__(self):
        return 'Booking for {{ guests }} at {{ restaurant }} on {{ date }}'.format(party=self.party_size,
                                                                      restaurant=self.restaurant,
                                                                      date=self.time)


class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    settings_id = models.IntegerField(default=False)


class Settings():
    opens = models.IntegerField()
    closes = models.IntegerField()
    active_mon_tues = models.BooleanField(default=False)

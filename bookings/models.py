from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(unique=True, primary_key=True)
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


class Booking(models.Model):
    booking_id = models.IntegerField(unique=True, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_id')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    rst_location = models.CharField(max_length=100)
    date = models.DateField(max_length=10, default=timezone.now)
    time = models.TimeField(max_length=10, choices=TIME_CHOICES, default=timezone.now)
    comment = models.TextField(max_length=200, blank=True, default=False)

# class Meta():

    def __str__(self):
        return self.first_name


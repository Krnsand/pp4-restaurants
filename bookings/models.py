from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.db.models import IntegerField, Model
import datetime as dt


# Create your models here.

# class User(models.Model):
#    first_name = models.CharField(max_length=100, null=True, blank=True)
#    last_name = models.CharField(max_length=100, null=True, blank=True)
#    email = models.EmailField(max_length=100, unique=True)
#    phone_number = PhoneNumberField(blank=True)


TIME_CHOICES = (
    (dt.time(hour=5, minute=0), "5 PM"),
    (dt.time(hour=5, minute=30), "5:30 PM"),
    (dt.time(hour=6, minute=0), "6 PM"),
    (dt.time(hour=6, minute=30), "6:30 PM"),
    (dt.time(hour=7, minute=0), "7 PM"),
    (dt.time(hour=7, minute=30), "7:30 PM"),
    (dt.time(hour=8, minute=0), "8 PM"),
    (dt.time(hour=8, minute=30), "8:30 PM"),
    (dt.time(hour=9, minute=0), "9 PM"),
    (dt.time(hour=9, minute=30), "9:30 PM"),
)


GUEST_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
)


# RST_CHOICES = (
#    ("1", "1"),
#    ("2", "2"),
#    ("3", "3"),
# )


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    opens = models.TimeField()
    closes = models.TimeField()
    active_mon_tues = models.BooleanField(default=False)


class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField(max_length=10, default=timezone.now, blank=True)
    time = models.TimeField(max_length=10, choices=TIME_CHOICES, default=timezone.now, blank=True)
    guests = models.IntegerField(choices=GUEST_CHOICES, blank=True, null=True)
    comment = models.TextField(max_length=200, default="", blank=True)

    def __str__(self):
        return 'Booking for {guests} guests at {restaurant} on {date} at {time}'.format(guests=self.guests,
                                                                       restaurant=self.restaurant,
                                                                       date=self.date,
                                                                       time=self.time)


# class Reservation(models.Model):
#       model = Article
#       fields = ['pub_date', 'headline', 'content', 'reporter']


# class ViewBookings(models.Model):
    # class Meta():
    #    """To display the recipes by created_on in descending order"""
    #    ordering = ['-date']

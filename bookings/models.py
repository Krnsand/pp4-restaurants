from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.db.models import IntegerField, Model
import datetime as dt


TIME_CHOICES = (
    (dt.time(hour=17, minute=0), "5 PM"),
    (dt.time(hour=17, minute=30), "5:30 PM"),
    (dt.time(hour=18, minute=0), "6 PM"),
    (dt.time(hour=18, minute=30), "6:30 PM"),
    (dt.time(hour=19, minute=0), "7 PM"),
    (dt.time(hour=19, minute=30), "7:30 PM"),
    (dt.time(hour=20, minute=0), "8 PM"),
    (dt.time(hour=20, minute=30), "8:30 PM"),
    (dt.time(hour=21, minute=0), "9 PM"),
    (dt.time(hour=21, minute=30), "9:30 PM"),
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


class Restaurant(models.Model):
    name = models.CharField("Restaurant Name", max_length=100)
    adress = models.CharField(max_length=100)
    opens = models.TimeField()
    closes = models.TimeField()
    active_mon_tues = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, default="")
    date = models.DateField(max_length=10, default=timezone.now, blank=True)
    time = models.TimeField(
        max_length=10, choices=TIME_CHOICES, default=timezone.now, blank=True
    )
    guests = models.IntegerField(choices=GUEST_CHOICES, blank=True, null=True)
    comment = models.TextField(max_length=200, default="", blank=True)

    class Meta:
            ordering = ['date']

    def __str__(self):
        return "Booking for {guests} guests at {restaurant} on {date} at {time}".format(
            guests=self.guests,
            restaurant=self.restaurant,
            date=self.date,
            time=self.time,
        )


# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    email = models.EmailField(max_length=100, unique=True)
#    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.first_name + ' ' + self.last_name

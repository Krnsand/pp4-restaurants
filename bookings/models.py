from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Booking(models.Model):
    booking_id = models.AutoField(max_length=10, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_id')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    rst_location = models.CharField()
    date_time = models.DateTimeField()




    class Meta():

    def __str__(self):
        return self.title

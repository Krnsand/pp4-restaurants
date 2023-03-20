from django.shortcuts import render
from django.views import generic
from .models import Booking


# look over this
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter()
    template_name = "index.html"

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from .models import Booking


# look over this
# class HomePage(View):
#    def get(request):
#        return render(request, 'index.html')


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter()
    template_name = "index.html"
    context_object_name = 'booking_list'

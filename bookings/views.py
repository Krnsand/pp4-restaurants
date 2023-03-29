from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from .models import Booking
# from .forms import RestaurantForm


# look over this
# class HomePage(View):
#    def get(request):
#        return render(request, 'index.html')

def add_reservation(request):
    from = RestaurantForm
    return render(request, 'add_reservation.html', {'form':form})

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter()
    template_name = "base.html"
    context_object_name = 'booking_list'

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Booking


# class TableListView(ListView):
#    model = Table
#    queryset = Table.objects.filter()
#    template_name = 'index.html'


# class TableDetailView(DetailView):
#    model = Table
#    template_name = 'table_detail.html'


# look over this
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter()
    template_name = "index.html"
    context_object_name = 'booking_list'

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from .models import Booking
from .forms import RestaurantForm


def add_reservation(request):
    submitted = False
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_reservation?submitted=True')

    else:
        form = RestaurantForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_reservation.html', {'form': form,
                                                        'submitted': submitted})


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter()
    template_name = "base.html"
    context_object_name = 'booking_list'


class VioletFusion(View):
    """
    Simple view to render the violet_fusion.html page.
    """

    def get(self, request):
        """
        Get method, renders violet_fusion.html.
        """
        return render(request, "violet_fusion.html")


class GreenDining(View):
    """
    Simple view to render the green_dining.html page.
    """

    def get(self, request):
        """
        Get method, renders green_dining.html.
        """
        return render(request, "green_dining.html")


class OrangeCushion(View):
    """
    Simple view to render the orange_cushion.html.
    """

    def get(self, request):
        """
        Get method, renders orange_cushion.html.
        """
        return render(request, "orange_cushion.html")


# look over this
# class HomePage(View):
#    def get(request):
#        return render(request, 'base.html')

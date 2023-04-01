from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Booking
from .forms import RestaurantForm
from django.views.generic import (
    View,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


class HomePage(View):
    def get(self, request):
        return render(request, "base.html")


def add_reservation(request):
    submitted = False
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return HttpResponseRedirect("/bookings")
    else:
        form = RestaurantForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "add_reservation.html", {"form": form, "submitted": submitted}
    )


@method_decorator(login_required, name='dispatch')
class BookingList(generic.ListView):
    model = Booking
    form_class = RestaurantForm
    queryset = Booking.objects.all().order_by('date')
    template_name = "bookings.html"
    context_object_name = "booking_list"


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


class BookingDetail(DetailView):
    model = Booking
    template_name = 'booking_details.html'


class UpdateBooking(UpdateView):
    model = Booking
    template_name = 'update_booking.html'
    fields = ['date', 'time', 'guests', 'comment']


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('bookings')

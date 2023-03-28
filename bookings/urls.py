from . import views
from django.urls import path

urlpatterns = [
    path("", views.BookingList.as_view(), name="home"),
    path("", views.Booking, name='bookings'),
]

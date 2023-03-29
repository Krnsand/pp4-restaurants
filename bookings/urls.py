from . import views
from django.urls import path
from .views import BookingList

urlpatterns = [
    # path("", views.HomePage, name="home"),
    path("", views.BookingList.as_view(), name="bookings"),
    # path("", views.Booking, name='bookings'),
]

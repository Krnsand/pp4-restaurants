from . import views
from django.urls import path
from .views import BookingList
# from .views import HomePage

urlpatterns = [
    # path("", views.HomePage, name="home"),
    path("", views.BookingList.as_view(), name="bookings"),
    # path("", views.Booking, name='bookings'),
    path('add_reservation', views.add_reservation, name="add-reservation"),
]

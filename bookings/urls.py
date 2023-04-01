from . import views
from django.urls import path
from .views import (
    HomePage,
    BookingList,
    VioletFusion,
    GreenDining,
    OrangeCushion,
    BookingDetail,
    UpdateBooking,
    DeleteBooking,
    Error,
)

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("bookings", views.BookingList.as_view(), name="bookings"),
    path("add_reservation", views.add_reservation, name="add-reservation"),
    path("violet_fusion", views.VioletFusion.as_view(), name="violet"),
    path("green_dining", views.GreenDining.as_view(), name="green"),
    path("orange_cushion", views.OrangeCushion.as_view(), name="orange"),
    path("bookings/<int:pk>", views.BookingDetail.as_view(), name="details"),
    path("bookings/edit/<int:pk>", views.UpdateBooking.as_view(), name="update-booking"),
    path("bookings/edit/<int:pk>/remove", views.DeleteBooking.as_view(), name="delete-booking"),
    path("404", views.Error.as_view(), name="error"),
]

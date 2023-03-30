from . import views
from django.urls import path
from .views import HomePage, BookingList, VioletFusion, GreenDining, OrangeCushion 

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    # path("restaurants", views.HomePage.as_view(), name="restaurants"),
    path("booking_list", views.BookingList.as_view(), name="bookings"),
    path('add_reservation', views.add_reservation, name="add-reservation"),
    path('violet_fusion', views.VioletFusion.as_view(), name="violet"),
    path('green_dining', views.GreenDining.as_view(), name="green"),
    path('orange_cushion', views.OrangeCushion.as_view(), name="orange"),
]

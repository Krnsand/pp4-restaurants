from . import views
from django.urls import path
from .views import BookingList, VioletFusion, GreenDining, OrangeCushion
# from .views import HomePage

urlpatterns = [
    # path("", views.HomePage, name="home"),
    path("", views.BookingList.as_view(), name="bookings"),
    # path("", views.Booking, name='bookings'),
    path('add_reservation', views.add_reservation, name="add-reservation"),
    path('violet_fusion', views.VioletFusion.as_view(), name="violet"),
    path('green_dining', views.GreenDining.as_view(), name="green"),
    path('orange_cushion', views.OrangeCushion.as_view(), name="orange"),
]

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Booking, Restaurant
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ("user", "restaurant", "date", "time")
    search_fields = ["user", "restaurant", "date", "time"]
    list_filter = ("user", "restaurant", "date", "time")
    summernote_fields = "comment"


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

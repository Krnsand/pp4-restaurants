from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Booking, Restaurant
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ("restaurant", "date", "time")
    search_fields = ["restaurant", "date", "time"]
    list_filter = ("restaurant", "date", "time")
    summernote_fields = "comment"


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#    pass

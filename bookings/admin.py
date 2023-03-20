from django.contrib import admin
from .models import Booking, User
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('restaurant', 'date', 'time')
    search_fields = ['restaurant', 'date', 'time']
    list_filter = ('restaurant', 'date', 'time')
    summernote_fields = ('comment')


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin)
from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_filter = ('rst_location', 'date', 'time')
    summernote_fields = ('comment')

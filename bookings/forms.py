from django import forms
from django.forms import ModelForm
from datetime import datetime
from .models import Booking
from allauth.account.forms import SignupForm
from bootstrap_datepicker_plus.widgets import DatePickerInput, MonthPickerInput


# Create a Restaurant booking form


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            "restaurant",
            "name",
            "email",
            "date",
            "time",
            "guests",
            "comment",
        )
        labels = {
            "restaurant": "",
            "name": "",
            "email": "",
            "date": "",
            "time": "",
            "guests": "",
            "comment": "",
        }
        widgets = {
            "restaurant": forms.Select(
                attrs={"class": "form-control", "placeholder": "Restaurant"}
            ),
            "name": forms.TextInput(
               attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "date": DatePickerInput(
               attrs={"class": "form-control", "placeholder": "Date"}
            ),
            "time": forms.Select(
                attrs={"class": "form-control", "placeholder": "Time"}
            ),
            "guests": forms.Select(
                attrs={"class": "form-control", "placeholder": "# of Guests"}
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Comment anything we might need to know for your visit",
                }
            ),
        }

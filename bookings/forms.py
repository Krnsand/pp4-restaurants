from django import forms
from django.forms import ModelForm
# from datetime import datetime
from .models import Booking


# Create a Restaurant booking form

class RestaurantForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = ('restaurant', 'name', 'email', 'date',
                  'time', 'guests', 'comment')
        labels = {
            'restaurant': '',
            'name': '',
            'email': '',
            'date': '',
            'time': '',
            'guests': '',
            'comment': '',
        }
        widgets = {
            'restaurant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Restaurant'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
            'guests': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# of Guests'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment anything we might need to know for your visit'}),
        }






# class ContactForm(forms.Form):

#    Form for contacting owner.

"""
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 150)
    subject = forms.CharField(max_length = 200)
    message = forms.CharField(widget = forms.Textarea(attrs={
        'class': 'custom-form-field'
        }), max_length = 2000)
    email.required = True
    first_name.required = True
    last_name.required = True
    first_name.widget.attrs.update({'class': 'custom-form-field'})
    last_name.widget.attrs.update({'class': 'custom-form-field'})
    email.widget.attrs.update({'class': 'custom-form-field'})
    subject.widget.attrs.update({'class': 'custom-form-field'})
"""
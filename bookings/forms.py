# from django import forms
# from django.forms import ModelForm
# from datetime import datetime
# from .models import RestaurantForm


# Create a Restaurant booking form
"""
 class RestaurantForm(forms.ModelForm):
    class Meta():
        model = Reservation
        fields = ('restaurant', 'name', 'email_adress', 'phone_number', 'date',
        'time', 'guests', 'comment')



    """


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
from . import views
from django.urls import path
from .views import UserRegistration


urlpatterns = [
    path('signup/', UserRegistration.as_view(), name='signup'),
]

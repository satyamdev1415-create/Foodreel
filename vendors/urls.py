from django.urls import path
from .views import *

urlpatterns = [
    path('register/',vendor_register, name='vendor-register'),
]

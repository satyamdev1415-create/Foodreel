from django.urls import path
from .views import *

urlpatterns = [

    path(
        "add/",
        add_address,
        name="add-address"
    ),

    path(
        "",
        address_list,
        name="address-list"
    ),

]
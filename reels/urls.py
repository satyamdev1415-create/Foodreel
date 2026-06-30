from django.urls import path
from .views import *

urlpatterns = [

    path(
        "",
        reel_list,
        name="reel-list"
    ),

    path(
        "add/",
        add_reel,
        name="add-reel"
    ),

]
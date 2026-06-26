from django.urls import path
from .views import *

urlpatterns = [

    path(
        "add/",
        add_food,
        name="add-food"
    ),

    path(
        "list/",
        food_list,
        name="food-list"
    ),
]
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

    path(
       "update/<int:pk>/",
        update_food,
        name="update-food"
    ),

    path(
       "delete/<int:pk>/",
        delete_food,
        name="delete-food"
    ),
    path("",home, name="home"),

    path('detail/<int:pk>/',food_detail,name="food-detail"),
]
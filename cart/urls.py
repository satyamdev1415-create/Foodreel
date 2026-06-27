from django.urls import path
from .views import *


urlpatterns = [
    path("add/<int:pk>/",add_to_cart, name="add-cart"),
    path("",cart_list, name="cart-list"),
    path("remove/<int:pk>/",remove_cart,name="remove-cart"),
    path("increase/<int:pk>/",increase_quantity, name="increase-cart"),
    path("decrease/<int:id>/",decrease_quantity, name="decrease-cart"),
]

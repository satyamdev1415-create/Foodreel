from django.urls import path
from .views import place_order, order_success

urlpatterns = [

    path(
        "place/",
        place_order,
        name="place-order"
    ),

    path(
        "success/",
        order_success,
        name="order-success"
    ),

]
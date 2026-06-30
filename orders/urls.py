from django.urls import path
from .views import *

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

    path("my-orders/",my_orders, name="my-orders"),
    path("detail/<int:pk>/",order_detail,name="order-detail"),

    path("vendor/",vendor_orders, name="vendor-orders"),

    path("status/<int:pk>/<str:status>/",update_order_status, name="update-order-status"),

    path("vendor/detail/<int:pk>/",vendor_order_detail, name="vendor-order-deatils"),

    
]
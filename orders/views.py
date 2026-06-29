from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from addresses.models import Address
from .models import Order, OrderItem


@login_required
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect("cart-list")

    address = Address.objects.filter(
        user=request.user,
        is_default=True
    ).first()

    if not address:
        return redirect("add-address")

    total = sum(item.total_price() for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        address=address,
        total_amount=total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            food=item.food,
            quantity=item.quantity,
            price=item.food.price
        )

    cart_items.delete()

    return redirect("order-success")


@login_required
def order_success(request):

    return render(
        request,
        "orders/order_success.html"
    )
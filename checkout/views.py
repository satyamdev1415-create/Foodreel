from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from addresses.models import Address


@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items)

    address = Address.objects.filter(
        user=request.user,
        is_default=True
    ).first()

    context = {

        "cart_items": cart_items,

        "total": total,

        "address": address,

    }

    return render(
        request,
        "checkout/checkout.html",
        context
    )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from foods.models import FoodItem
from .models import Cart

# Create your views here.
@login_required
def add_to_cart(request, pk):
    food = get_object_or_404(FoodItem, id=pk)
    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        food=food
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart-list")


@login_required
def cart_list(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.total_price()
    for item in cart_items)

    return render(request, "cart/cart_list.html", {
        "cart_items":cart_items,
        "total": total
    })


@login_required
def remove_cart(request, pk):
    item = get_object_or_404(
        Cart,
        id=pk,
        user=request.user
    )
    item.delete()

    return render("cart-list")


@login_required
def increase_quantity(request, pk):
    cart_item = get_object_or_404(
        Cart,
        id=pk,
        user=request.user
    )
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart-list")

@login_required
def decrease_quantity(request, pk):
    cart_item = get_object_or_404(
        Cart,
        id=pk,
        user=request.user
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect("cart-list")
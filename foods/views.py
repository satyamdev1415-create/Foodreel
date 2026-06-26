from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from vendors.models import Vendor
from .forms import FoodForm
from .models import FoodItem


@login_required
def add_food(request):

    vendor = Vendor.objects.get(owner=request.user)

    if request.method == "POST":

        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():

            food = form.save(commit=False)

            food.vendor = vendor

            food.save()

            return redirect("food-list")

    else:
        form = FoodForm()

    return render(request, "foods/add_food.html", {"form": form})

@login_required
def food_list(request):

    vendor = Vendor.objects.get(owner=request.user)

    foods = FoodItem.objects.filter(vendor=vendor)

    return render(
        request,
        "foods/food_list.html",
        {"foods": foods}
    )
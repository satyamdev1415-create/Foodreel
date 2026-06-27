from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from vendors.models import Vendor
from .forms import FoodForm
from .models import FoodItem , Category


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


@login_required
def update_food(request,pk):
    vendor = Vendor.objects.get(owner=request.user)
    food = get_object_or_404(
        FoodItem,
        id=pk,
        vendor=vendor
    )

    form = FoodForm(
        request.POST or None,
        request.FILES or None,
        instance=food
    )

    if form.is_valid():
        form.save()

        return redirect("food-list")

    return render(request,  "foods/update_food.html",{"form": form})


@login_required
def delete_food(request, pk):

    vendor = Vendor.objects.get(owner=request.user)

    food = get_object_or_404(
        FoodItem,
        id=pk,
        vendor=vendor
    )

    if request.method == "POST":

        food.delete()

        return redirect("food-list")

    return render(
        request,
        "foods/delete_food.html",
        {"food": food}
    )


def home(request):

    categories = Category.objects.all()

    foods = FoodItem.objects.filter(
        is_available=True
    ).order_by("-created_at")

    context = {

        "categories": categories,

        "foods": foods,

    }

    return render(
        request,
        "foods/home.html",
        context
    )

def food_detail(request,pk):
    food = get_object_or_404(
        FoodItem,
        id=pk,
        is_available = True
    )

    related_foods = FoodItem.objects.filter(
        category= food.category,
        is_available=True
    ).exclude(id=food.id)[:4]


    context = {
        "food":food,
        "related_food" : related_foods,
    }

    return render(request, "foods/food_detail.html",context)
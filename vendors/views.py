from django.shortcuts import render, redirect
from .forms import VendorForm
from .models import Vendor
from foods.models import FoodItem

from django.contrib.auth.decorators import login_required

def vendor_register(request):

    if request.method == "POST":

        form = VendorForm(request.POST)

        if form.is_valid():

            vendor = form.save(commit=False)

            vendor.owner = request.user

            vendor.save()

            return redirect('profile')

    else:
        form = VendorForm()

    return render(
        request,
        'vendors/register_vendor.html',
        {'form': form}
    )

@login_required
def vendor_dashboard(request):

    vendor = get_object_or_404(
        Vendor,
        owner=request.user
    )

    total_products = FoodItem.objects.filter(
        vendor=vendor
    ).count()

    context = {

        "vendor": vendor,

        "total_products": total_products,

        "total_reels": 0,

        "total_orders": 0,

        "total_revenue": 0,

    }

    return render(
        request,
        "vendors/dashboard.html",
        context
    )
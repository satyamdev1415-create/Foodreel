from django.shortcuts import render, redirect
from .forms import VendorForm
from .models import Vendor

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

    vendor = Vendor.objects.get(
        owner=request.user
    )

    context = {
        'vendor': vendor
    }

    return render(
        request,
        'vendors/dashboard.html',
        context
    )
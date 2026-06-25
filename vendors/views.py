from django.shortcuts import render, redirect
from .forms import VendorForm

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
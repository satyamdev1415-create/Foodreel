from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddressForm
from .models import Address


@login_required
def add_address(request):

    if request.method == "POST":

        form = AddressForm(request.POST)

        if form.is_valid():

            address = form.save(commit=False)

            address.user = request.user

            if address.is_default:

                Address.objects.filter(
                    user=request.user
                ).update(
                    is_default=False
                )

            address.save()

            return redirect("address-list")

    else:

        form = AddressForm()

    return render(
        request,
        "addresses/add_address.html",
        {"form": form}
    )


@login_required
def address_list(request):

    addresses = Address.objects.filter(
        user=request.user
    )

    return render(
        request,
        "addresses/address_list.html",
        {
            "addresses": addresses
        }
    )
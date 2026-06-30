from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Reel
from .forms import ReelForm


@login_required
def reel_list(request):

    reels = Reel.objects.filter(
        is_active=True
    )

    return render(
        request,
        "reels/reel_list.html",
        {
            "reels": reels
        }
    )


@login_required
def add_reel(request):

    if request.method == "POST":

        form = ReelForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            reel = form.save(commit=False)

            reel.vendor = request.user.vendor

            reel.save()

            return redirect("reel-list")

    else:

        form = ReelForm()

    return render(
        request,
        "reels/add_reel.html",
        {
            "form": form
        }
    )
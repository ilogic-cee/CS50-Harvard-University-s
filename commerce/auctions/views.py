from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ListingForm
from django.contrib.auth.decorators import login_required
from .models import User, Category, Listing


from .models import User


def index(request):
    return render(request, "auctions/index.html")

from django.shortcuts import render, redirect
from .models import Listing
from .forms import CreateListingForm

def createListing(request):
    if request.method == "POST":
        # Creating and validating the form
        form = CreateListingForm(request.POST)
        if form.is_valid():
            # Extracting data from the validated form
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image_url = form.cleaned_data['image_url']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            starting_bid = form.cleaned_data['starting_bid']

            # Creating a new listing with the form data
            new_listing = Listing(
                title=title,
                description=description,
                imageurl=imageurl,
                price=price,
                category=category,
                starting_bid=starting_bid,
            )

            # Saving the new listing
            new_listing.save()

            return redirect('index')
    else:
        # Rendering the form for a GET request
        form = CreateListingForm()

    return render(request, 'auctions/create.html', {'form': form})







def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

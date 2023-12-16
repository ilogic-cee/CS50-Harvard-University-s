from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid




def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments,
        "isOwner": isOwner
    })




def closeAuction(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    isOwner = request.user.username == listingData.owner.username
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments,
        "isOwner": isOwner,
        "update": True,
        "message": "Congratulations! Your auction is closed."
    })







def addBid(request, id):
    print("Received ID:", id)
    newBid = request.POST['newBid']
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username

    # Check if the listing has a price (Bid instance) associated with it
    if listingData.price:
        # Access the bid attribute only if the price is not None
        if int(newBid) > listingData.price.bid:
            updateBid = Bid(user=request.user, bid=int(newBid))
            updateBid.save()
            listingData.price = updateBid
            listingData.save()
            return render(request, "auctions/listing.html", {
                "listing": listingData,
                "message": "Bid was updated successfully",
                "update": True,
                "isListingInWatchlist": isListingInWatchlist,
                "allComments": allComments,
                "isOwner": isOwner,
            })
        else:
            return render(request, "auctions/listing.html", {
                "listing": listingData,
                "message": "Bid was not updated. Please enter a higher bid.",
                "update": False,
                "isListingInWatchlist": isListingInWatchlist,
                "allComments": allComments,
                "isOwner": isOwner,
            })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Bid was not updated. Please try again later.",
            "update": False,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments,
            "isOwner": isOwner,
        })





def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['newComment']

    newComment = Comment(
        author = currentUser,
        listing = listingData,
        message = message
    )

    newComment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))




def displayWatchlist(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })






def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))



def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))



def index(request):
      # Get all active listings (where isActive is True)
    activeListings = Listing.objects.filter(isActive=True)

     # Get all categories
    allCategories = Category.objects.all()
    # Render the index.html template with the list of active listings and all categories
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": allCategories,
    })


def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        activeListings = Listing.objects.filter(isActive=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listings": activeListings,
            "categories": allCategories,
        })


def createListing(request):
    # Check if the request method is GET
    if request.method == "GET":
        # Retrieve all categories for rendering in the create.html template
        allCategories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories": allCategories,
        })
    # Check if the request method is POST
    else:
        title = request.POST['title']
        description = request.POST['description']
        imageurl = request.POST['imageurl']
        price = request.POST['price']
        category = request.POST['category']

        # Get the current user
        currentUser = request.user
        # Get the category data based on the selected category name
        categoryData = Category.objects.get(categoryName=category)

        # Create a new bid for the listing
        bid = Bid(bid=int(price), user=currentUser)
        bid.save()

        # Create a new listing with the bid
        newListing = Listing(
            title=title,
            description=description,
            imageUrl=imageurl,
            price=bid,
            category=categoryData,
            owner=currentUser
        )
        # Save the new listing to the database
        newListing.save()

        # Redirect to the index page after successful listing creation
        return HttpResponseRedirect(reverse('index'))


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

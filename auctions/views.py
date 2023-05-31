from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .auction_forms import *
from .utils import is_valid_image_url
from .auctions_const import *

from .models import *


def index(request):
    return render(request, "auctions/index.html")


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


# last finished
def add_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        end_time = request.POST['end_time']
        starting_price = request.POST['starting_price']
        photo_url = request.POST['photo_url']

        if not title or not description or len(title) > LONG_TEXT or not is_valid_image_url(photo_url):
            return render(request, 'auctions/add_listing.html', {
                'categories': CATEGORIES,
                'title': title,
                'description': description,
                'category': category,
                'end_time': end_time,
                'starting_price': starting_price,
                'photo_url': photo_url,
                'error_msg': 'Please provide correct input'
            })
        else: 
            seller_id = request.user
            listing = Listing(title=title, description=description, category=category, end_time=end_time, starting_price=starting_price, photo_url=photo_url, current_bid=starting_price, seller=seller_id)
            listing.save()
            
    return render(request, 'auctions/add_listing.html', {
        'categories': CATEGORIES,
    })
    

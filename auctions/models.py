from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from .auctions_const import *


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=LONG_TEXT, null=False)
    description = models.TextField()
    category = models.CharField(max_length=SHORT_TEXT, choices=CATEGORIES, null=True)
    seller = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'listings')
    current_bid = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    starting_price = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    time_added = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    photo_url = models.URLField(blank=True, null=True)
    active = models.BooleanField(auto_created=True)
    
    def __str__(self):
        return self.title
    

class Coments(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = 'listing_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.timestamp}'
    

class Bids(models.Model):
    bid_amount = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, default=10)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bids')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_bids')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bid placed by {self.bidder.username}, on {self.listing.title}'
    

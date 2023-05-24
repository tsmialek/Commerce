from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORIES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('sport', 'Sport'),
        ('home', 'Home'),
        ('health', 'Health')
    ]
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    category = models.CharField(max_length=64, choices=CATEGORIES, null=True)
    seller = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'listings')
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()
    photo_url = models.URLField(blank=True, null=True)
    
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
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bids')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_bids')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bid placed by {self.bidder.username}, on {self.listing.title}'
    

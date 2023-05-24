from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


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
    name = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=200, )
    category = models.CharField(max_length=64, choices=CATEGORIES)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'listings')

class Coments(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name = 'listing_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')

class Bids(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bids')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_bids')

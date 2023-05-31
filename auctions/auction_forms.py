from django import forms
from . import models
from .auctions_const import *

class CreateListingForm(forms.Form):
    title = forms.CharField(label='Auction title: ', required=True, max_length=255)
    description = forms.CharField(label='Provide description for your auction: ', 
        widget=forms.Textarea(attrs={'rows': 4}))
    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.Select())
    end_time = forms.DateTimeField()
    starting_price = forms.DecimalField(max_digits=10, decimal_places=2)
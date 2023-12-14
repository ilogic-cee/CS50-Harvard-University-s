# auctions/forms.py
from django import forms
from .models import ListingForm  



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'imageUrl', 'starting_bid', 'category']

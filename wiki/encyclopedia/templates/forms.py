# /workspaces/81265920/wiki/wiki/encyclopedia/forms.py

from django import forms

class CreateEntryForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

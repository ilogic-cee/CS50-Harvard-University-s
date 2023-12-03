from django import forms

class CreateEntryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(widget=forms.Textarea, label='Content')

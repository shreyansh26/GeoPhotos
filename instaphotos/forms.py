from django import forms

class PostForm(forms.Form):
    location = forms.CharField(label='location', max_length=100)

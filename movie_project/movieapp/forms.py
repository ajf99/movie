from django import forms
from.models import Movie


class Movie_form(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','dscr','year','img']
from django import forms
from . import models


class AddMeal(forms.ModelForm):
    class Meta:
        model = models.Meal
        fields = ['name', 'image', 'price', 'description', 'slug','category']


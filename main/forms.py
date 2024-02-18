from django import forms
from .models import Recipe

class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'content', 'steps', 'time_to_cook', 'img', 'author']
        

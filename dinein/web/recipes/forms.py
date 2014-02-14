from django import forms
from dinein.web.models import Recipe, Ingredient


class AddRecipeForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Name your recipe'
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        help_text="No...")

    class Meta:
        model = Recipe
        exclude = ('description', )


class EditRecipeForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Name your recipe'
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        help_text="No...")

    class Meta:
        model = Recipe

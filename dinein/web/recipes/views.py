from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from dinein.web.models import UserRecipe
from dinein.web.recipes.forms import AddRecipeForm


@login_required
def home(request):
    return render(request, 'recipes/home.html')


@login_required
def add(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            UserRecipe.objects.get_or_create(user=request.user, recipe=recipe)
            messages.success(
                request,
                "Thank you, your project has been added."
            )
            return redirect(reverse('recipe:edit', recipe.slug))
    else:
        form = AddRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'recipes/add.html', context)

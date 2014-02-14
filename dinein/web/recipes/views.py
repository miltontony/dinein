from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from dinein.web.models import UserRecipe
from dinein.web.recipes.forms import AddRecipeForm, EditRecipeForm


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
            return redirect(reverse('recipes:edit', args=[recipe.slug, ]))
    else:
        form = AddRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'recipes/add.html', context)


@login_required
def edit(request, slug):
    recipe = get_object_or_404(UserRecipe, recipe__slug=slug)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe.recipe)
        if form.is_valid():
            recipe = form.save()
            messages.success(
                request,
                "Thank you, your project has been edited"
            )
            return redirect(reverse('recipes:home'))
    else:
        form = EditRecipeForm(instance=recipe.recipe)

    context = {
        'form': form,
    }
    return render(request, 'recipes/edit.html', context)

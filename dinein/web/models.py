from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey('web.Ingredient')
    quantity = models.CharField(max_length=20, default='1')


class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    preparation = models.TextField(default='')
    ingredients = models.ManyToManyField(
        'web.RecipeIngredient',
        blank=True,
        null=True,
        default=None)


class UserRecipes(models.Model):
    user = models.ForeignKey('auth.User')
    recipes = models.ManyToManyField(
        'web.Recipe',
        blank=True,
        null=True,
        default=None,
        related_name='recipes')

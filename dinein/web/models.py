from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField(default='')
    preparation = models.TextField(default='')
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        null=True,
        default=None)


class UserRecipe(models.Model):
    user = models.ForeignKey('auth.User', related_name='recipes')
    recipe = models.ForeignKey('web.Recipe')

from django.db import models
from dinein.web.utils import generate_slug


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    title = models.TextField()
    slug = models.SlugField(editable=False, max_length=255,)
    description = models.TextField(default='')
    preparation = models.TextField(default='')
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        null=True,
        default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(Recipe, self, self.title)
        super(Recipe, self).save(*args, **kwargs)


class UserRecipe(models.Model):
    user = models.ForeignKey('auth.User', related_name='recipes')
    recipe = models.ForeignKey('web.Recipe')
    created = models.DateTimeField(auto_now_add=True)

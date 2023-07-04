from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    recipe_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, default='Name of recipe')
    ingridients = models.TextField(
        default='Ingredients list not found, but will be soon...'
    )
    image = models.ImageField(
        upload_to='recipes/media',
        blank=True,
        null=True,
        default='default_value'
    )
    cooking_steps = models.TextField(
        default='Steps not found, but will be soon...'
    )
    cooking_time = models.TextField(
        default='Time not found, but will be soon...'
    )
    sourceUrl = models.URLField(
        blank=True,
        null=True,
        default='https://spoonacular.com/'
    )
    save_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.user.username}'

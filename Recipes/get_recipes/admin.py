from django.contrib import admin

from .models import Recipe

admin.site.register(Recipe)


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'user',
        'recipe_id',
        'ingridients',
        'pub_date',
        'image',
        'cooking_steps',
        'sourceUrl',
    )
    # list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

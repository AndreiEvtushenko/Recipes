import ast
import os

import requests
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from get_recipes.models import Recipe

from dotenv import load_dotenv

load_dotenv()

X_API_KEY = os.getenv('X_API_KEY')


def index(request):
    """
    Shows the main page of the project with random recipes and a random quote.
    """

    template = 'get_recipes/index.html'
    quote, author = get_random_quote(request)
    recipes = get_random_recipes(request)
    context = {
        'quote': quote,
        'author': author,
        'recipes': recipes,
    }

    return render(request, template, context)


# in developing
def get_recipes(request, ingridients):
    """
    Requests from the API a list of recipes with the necessary ingredients.
    Returns a dictionary with recipes.
    """

    pass


def list_recipes(request):
    """
    Gets a dictionary of recipes and generates a page with a list of recipes.
    """

    ingredients = request.GET.get('ingredients')
    recipes = get_recipes_by_ingridients(request, ingredients)
    template = 'get_recipes/list_recipes.html'
    context = {
        'recipes': recipes,
    }

    return render(request, template, context)


def recipe_detail(request, recipe_id):
    """
    Accepts a recipe ID,
    requests information from the database by ID,
    generates a page with detailed information about the recipe.
    """

    recipe_exists = Recipe.objects.filter(recipe_id=recipe_id).exists()

    if recipe_exists:
        template = 'get_recipes/profile_recipe_detail.html'
        recipe = get_object_or_404(Recipe, recipe_id=recipe_id)
        ingridients = ast.literal_eval(recipe.ingridients)
        names = []

        for i in ingridients:
            names.append(i['name'])
        context = {
            'names': names,
            'recipe': recipe,
        }
        return render(request, template, context)

    else:
        template = 'get_recipes/recipe_detail.html'
        recipe = get_recipe(request, recipe_id)
        context = {
            'recipe': recipe,
        }

        return render(request, template, context)


def profile(request, user_id):
    """
    If the user is authorized,
    it receives the user's ID from the request,
    queries the database for the recipes saved by the user
    displays the list of the user's recipes on the page.
    """

    template = 'get_recipes/profile.html'
    recipes = Recipe.objects.filter(user_id=user_id)
    context = {
        'recipes': recipes,
        }

    return render(request, template, context)


def save_recipe(request, recipe_id):
    """
    Receives a recipe ID.
    Saves a recipe the database.
    """

    recipe = cache.get(recipe_id)

    if not recipe:
        headers = {'X-Api-Key': X_API_KEY}
        response = requests.get(
            f'https://api.spoonacular.com/recipes/{recipe_id}/'
            f'information?includeNutrition=false',
            headers=headers
            )

        if response.status_code == 200:
            recipe = response.json()
            cache.set(recipe_id, recipe, timeout=86400)

    recipe = cache.get(recipe_id)
    recipe_ingridient = []

    for ingredient in recipe['extendedIngredients']:
        recipe_ingridient.append(ingredient)

    str_recipe_ingridient = str(recipe_ingridient)

    Recipe.objects.create(
        user=request.user,
        recipe_id=recipe_id,
        name=recipe['title'],
        ingridients=str_recipe_ingridient,
        image=recipe['image'],
        cooking_steps=recipe['instructions'],
        sourceUrl=recipe['sourceUrl'],
        cooking_time=recipe['readyInMinutes']
    )

    return redirect(reverse('get_recipes:recipe_detail', args=[recipe_id]))


def get_random_quote(request):
    """
    Checks the recipes in hash.
    Gets a random quote from the API about food.
    """

    quote = cache.get('quote')
    author = cache.get('author')

    if not quote:
        response = requests.get(
            'https://zenquotes.io/api/random?category=food'
        )

        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            cache.set('quote', quote, timeout=86400)
            cache.set('author', author, timeout=86400)
            return quote, author

    return quote, author


def get_random_recipes(request):
    """
    Gets a four random recipes from the API.
    """

    recipes = cache.get('recipes')

    if not recipes:
        headers = {'X-Api-Key': X_API_KEY}
        response = requests.get(
            'https://api.spoonacular.com/recipes/random?number=8',
            headers=headers
        )

        if response.status_code == 200:
            recipes = response.json()
            cache.set('recipes', recipes, timeout=86400)
            return recipes

    return recipes


def get_recipe(request, recipe_id):
    """
    Checks the recipe in hash.
    Gets a recipe from the API by id.
    Hashes a four random recipes for 24 hours.
    """

    recipe = cache.get(recipe_id)

    if not recipe:
        headers = {'X-Api-Key': X_API_KEY}
        response = requests.get(
            f'https://api.spoonacular.com/recipes/{recipe_id}/'
            f'information?includeNutrition=false',
            headers=headers
        )

        if response.status_code == 200:
            recipe = response.json()
            cache.set(recipe_id, recipe, timeout=86400)
            return recipe

    return recipe


def get_recipes_by_ingridients(request, ingredients):
    """
    Checks the recipes in hash.
    Gets a recipes from the API by ingredients.
    Hashes a recipes for 24 hours.
    """

    recipes = cache.get(ingredients)

    if not recipes:
        headers = {'X-Api-Key': X_API_KEY}
        params = {'ingredients': ingredients, 'number': 10, 'ranking': 1}
        response = requests.get(
            'https://api.spoonacular.com/recipes/findByIngredients',
            headers=headers, params=params
        )

        if response.status_code == 200:
            recipes = response.json()
            cache.set(ingredients, recipes, timeout=86400)
            return recipes

    return recipes

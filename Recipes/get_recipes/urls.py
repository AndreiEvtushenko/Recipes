from django.urls import path
from get_recipes import views

app_name = 'get_recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_recipes/', views.list_recipes, name='list_recipes'),
    path('recipe_detail/<recipe_id>/',
         views.recipe_detail, name='recipe_detail'
         ),
    path('save_recipe/<recipe_id>/',
         views.save_recipe, name='save_recipe'
         ),
    path('profile/<user_id>/', views.profile, name='profile'),
]

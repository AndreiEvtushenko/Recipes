from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('get_recipes.urls', namespace='get_recipes')),
    path('', include('users.urls', namespace='users')),
    path('about', include('about.urls', namespace='about')),
]

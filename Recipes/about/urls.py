from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('app/', views.AboutAppView.as_view(), name='aboutapp'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('send/form/', views.save_help_form, name='send_message'),
]

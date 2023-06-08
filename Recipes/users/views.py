from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUpView(CreateView):
    template_name = 'users/signup.html'
    form_class = CreationForm
    success_url = reverse_lazy('get_recipes:index')


def logout_view(request):
    logout(request)
    return redirect(reverse('get_recipes:index'))


class MyLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('get_recipes:index')

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('get_recipes:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_password(form.cleaned_data.get('password'))
        self.object.save()
        return response


def logout_view(request):
    logout(request)
    return redirect(reverse('get_recipes:index'))


class MyLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('get_recipes:index', urlconf=self.request.urlconf)

class MyLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        return next_url or reverse_lazy('get_recipes:index')
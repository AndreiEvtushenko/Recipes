from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import HelpForm
from .models import HelpFormModel
from send_message.views import send_message


class AboutAppView(TemplateView):
    template_name = 'about/about.html'


class HelpView(CreateView):
    form_class = HelpForm
    success_url = reverse_lazy('get_recipes:index')
    template_name = 'about/help.html'


def save_help_form(request):
    if request.method == 'POST':
        form = HelpFormModel(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            form.save()
            send_message(name, text, email)
    else:
        form = HelpFormModel()
    return redirect('get_recipes:index')

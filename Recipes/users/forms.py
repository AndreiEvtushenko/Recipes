from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()


class CreationForm(UserCreationForm):
    telegram = PhoneNumberField(required=True)
    image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 'username', 'email',
            'telegram', 'image', 'password1', 'password2')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

def clean_email(self):
    e = self.clenaed_data['email']
    if User.objects.filter(email=e).exists():
        raise ValidationError("O Email {} já está em uso.".format(e))
    return e

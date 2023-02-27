from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'password')
from django.core.exceptions import ValidationError

def validate_email_unique(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError("This email address is already in use.")

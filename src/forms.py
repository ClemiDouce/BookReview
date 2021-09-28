from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "id": "username-input",
                "placeholder": "Nom d'utilisateur"
            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
        attrs={
            "id": "password-input",
            "placeholder": "Mot de passe"
        }
    ))

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'id': "password1_input",
                "placeholder": "Mot de passe",
                "autocomplete": "new_password"
            }),
        strip=False
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "id": "password2_input",
                "placeholder": "Confirmer mot de passe",
                "autocomplete": "new_password",
            }),
        strip=False
    )
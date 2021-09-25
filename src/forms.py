from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "username-input",
                "placeholder": "Nom d'utilisateur"
            }
        )
    )

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "id": "password-input",
            "placeholder": "Mot de passe"
        }
    ))

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Comments
from django.contrib.auth.forms import UsernameField

class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        required=True, 
        widget=forms.TextInput(attrs={"class": "form-control", "id": "login-username", "name": "username"}))
    
    password = forms.CharField(
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "login-password", "name": "password" })
    )


class CreateCommmentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"
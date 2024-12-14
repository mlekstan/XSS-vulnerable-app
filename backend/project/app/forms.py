from django import forms
from django.contrib.auth.forms import 
from django.contrib.auth.models import User
from .models import Comments
from .classes import MyBaseUserCreationForm

class MyUserCreationForm(MyBaseUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "id": "reg-username", "name": "username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "id": "reg-email", "name": "email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "id": "reg-password", "name": "password"}),
        }

class 

class CreateCommmentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"
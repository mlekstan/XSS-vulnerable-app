from django import forms

class SignUpForm(forms.Form):
    user_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=320)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)

class SignInForm(forms.Form):
    user_name = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)
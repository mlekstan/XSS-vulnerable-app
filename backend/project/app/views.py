from django.shortcuts import render
from .forms import SignInForm, SignUpForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)

        if sign_up_form.is_valid():
            user_name = sign_up_form.cleaned_data["user_name"]
            email = sign_up_form.cleaned_data["email"]
            pasword = sign_up_form.cleaned_data["password"]

            return HttpResponseRedirect(reverse("app:tasks"))


    else:
        sign_up_form = SignUpForm()
        
        return render(request, "app/index.html", {"sign_up_form": sign_up_form})
    

def tasks(request):
    render(request, "app/tasks.html")
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, CreateCommmentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if request.method == "POST":
        sign_up_form = MyUserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            return redirect("app:tasks")

    else:
        sign_up_form = MyUserCreationForm()
    
    context = {"sign_up_form": sign_up_form}
    return render(request, "app/index.html", context)
    

def tasks(request):
    return render(request, "app/tasks.html")

def reflected_xss(request):
    pass

def stored_xss(request):
    pass

def dom_xss(request):
    pass
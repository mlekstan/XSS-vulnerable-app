from django.shortcuts import render, redirect
from .forms import MyAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .classes import MyBaseUserCreationForm

def index(request):

    if request.user.is_authenticated:
        return redirect("app:tasks")

    if request.method == "POST": 
        
        if "signup" in request.POST:
            sign_up_form = MyBaseUserCreationForm(request.POST)
            sign_in_form = MyAuthenticationForm()
            
            if sign_up_form.is_valid():
                user = sign_up_form.save()
                login(request, user)
                return redirect("app:tasks")
        

        if "signin" in request.POST:
            sign_in_form = MyAuthenticationForm(request, data=request.POST)
            sign_up_form = MyBaseUserCreationForm()
            
            if sign_in_form.is_valid():
                user = sign_in_form.get_user()
                login(request, user)
                return redirect("app:tasks")
    
    else:
        sign_up_form = MyBaseUserCreationForm()
        sign_in_form = MyAuthenticationForm()

    context = {
        "sign_up_form": sign_up_form,
        "sign_in_form": sign_in_form
    }

    return render(request, "app/index.html", context)
    
@login_required
def tasks(request):
    username = request.user.username
    
    context = {"username": username}
    return render(request, "app/tasks.html", context)

def logout_view(request):
    logout(request)
    return redirect("app:index")


def reflected_xss(request):
    pass

def stored_xss(request):
    pass

def dom_xss(request):
    pass
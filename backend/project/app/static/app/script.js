function openModal() {
    document.getElementById('modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

function closeModalOnOutsideClick(event) {
    const modal = document.getElementById('modal');
    const modalContent = document.querySelector('.modal-content');

    if (event.target === modal) {
        closeModal();
    }
}

function addComment(event) {
    event.preventDefault();

    const author = 'autor nieznany';
    const commentText = document.getElementById('commentText').value;

    const commentSection = document.querySelector('.comments-section');
    const newComment = document.createElement('div');
    newComment.classList.add('comment');

    newComment.innerHTML = `
        <div class="comment-header">
            <div class="author">Autor: ${author}</div>
            <button class="delete-button" onclick="this.parentElement.parentElement.remove();">Usuń</button>
        </div>
        <div class="text">${commentText}</div>
    `;

    commentSection.appendChild(newComment);

    closeModal();

    document.getElementById('addCommentForm').reset();
}


document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal-hint");
    const modalText = document.getElementById("modal-hint-text");
    const closeButton = document.querySelector(".close-button");
    const hintButtons = document.querySelectorAll(".hint-button");


    const hints = {
        1: `Przykładowa funkcja która zdobędzie token csrf dla logowania:
<pre><code>
session = requests.Session()

def get_csrf_token(url):
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
</code></pre>
<button id="copy-code-1" style="margin-top: 10px;">Skopiuj kod</button>
`,
        2: `Pojedyncza próba logowania wygląda następująco:
<pre><code>
payload = {
    "csrfmiddlewaretoken": csrf_token,
    "username": username,
    "password": password,
    "signin": "Sign in",
}
response = session.post(LOGIN_URL, data=payload)
</code></pre>
<button id="copy-code-2" style="margin-top: 10px;">Skopiuj kod</button>
        `,
        3: "Pozostaje tylko stworzyć pętle i porównywać przekierowywanie url aż trafimy na /app/tasks",
    };


    const openModalHint = (hintId) => {
        modalText.innerHTML = hints[hintId];
        modal.classList.remove("hidden");
        modal.style.display = "flex";

        if (hintId === "1") {
            const copyButton1 = document.getElementById("copy-code-1");
            copyButton1.addEventListener("click", () => {
                const codeToCopy = `session = requests.Session()

def get_csrf_token(url):
    response = session.get(url)
    if response.status_code == 200:
        # Parse the CSRF token from the HTML
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"}).get("value")
        return csrf_token
    else:
        print(f"Failed to load the login page. Status code: {response.status_code}")
        return None`;
                navigator.clipboard.writeText(codeToCopy).then(() => {
                    copyButton1.textContent = "Skopiowano!";
                    setTimeout(() => {
                        copyButton1.textContent = "Skopiuj kod";
                    }, 2000);
                });
            });
        }

        if (hintId === "2") {
            const copyButton2 = document.getElementById("copy-code-2");
            copyButton2.addEventListener("click", () => {
                const codeToCopy = `payload = {
    "csrfmiddlewaretoken": csrf_token,
    "username": username,
    "password": password,
    "signin": "Sign in",  
}
response = session.post(LOGIN_URL, data=payload)`;
                navigator.clipboard.writeText(codeToCopy).then(() => {
                    copyButton2.textContent = "Skopiowano!";
                    setTimeout(() => {
                        copyButton2.textContent = "Skopiuj kod";
                    }, 2000);
                });
            });
        }
    };


    const closeModalHint = () => {
        modal.classList.add("hidden");
        modal.style.display = "none";
    };

    hintButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const hintId = button.getAttribute("data-hint");
            openModalHint(hintId);
        });
    });

    closeButton.addEventListener("click", closeModal);


    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            closeModalHint();
        }
    });
});

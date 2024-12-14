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


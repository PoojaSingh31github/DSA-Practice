document.getElementById('cardForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const title = document.getElementById('titleInput').value;
    const message = document.getElementById('messageInput').value;

    document.getElementById('cardTitle').textContent = title;
    document.getElementById('cardMessage').textContent = message;

    // Clear inputs
    document.getElementById('titleInput').value = '';
    document.getElementById('messageInput').value = '';
});

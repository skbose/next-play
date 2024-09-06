document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.getElementById('loginButton');
    if (loginButton) {
        loginButton.addEventListener('click', function(event) {
            event.preventDefault();
            console.log('Login button clicked');
            // Redirect to login page
            window.location.href = '/login';
        });
    }
});

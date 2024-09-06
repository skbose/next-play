document.addEventListener('DOMContentLoaded', function() {
    const signInButton = document.getElementById('sign-in');
    if (signInButton) {
        signInButton.addEventListener('click', function(event) {
            event.preventDefault();
            console.log('Sign-in button clicked');
            // TODO: Add sign-in logic here
        });
    }
});

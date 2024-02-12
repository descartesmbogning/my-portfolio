
// Enhanced script.js

// Functionality for interactive elements
document.addEventListener('DOMContentLoaded', function() {
    // Example: Toggle class on click for a menu button
    const menuButton = document.querySelector('.menu-button');
    if (menuButton) {
        menuButton.addEventListener('click', function() {
            document.querySelector('.menu').classList.toggle('is-active');
        });
    }

    // More interactive functionalities can be added here
});

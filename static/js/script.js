
// script.js - Add this content to your main JS file

// Function to handle the responsive navbar toggle
function toggleNavbar(collapseID) {
    document.getElementById(collapseID).classList.toggle("hidden");
    document.getElementById(collapseID).classList.toggle("block");// JavaScript for responsive navbar toggling

}

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

document.addEventListener('DOMContentLoaded', function () {
    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function () {
        navbarCollapse.classList.toggle('active');
    });
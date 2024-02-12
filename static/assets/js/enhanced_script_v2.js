
// Enhanced script.js with responsive navbar toggling

// Include Bootstrap JS for responsive design
import 'https://code.jquery.com/jquery-3.5.1.slim.min.js';
import 'https://cdn.jsdelivr.net/npm/@popperjs/core@2.4.3/dist/umd/popper.min.js';
import 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js';

document.addEventListener('DOMContentLoaded', function () {
    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function () {
        navbarCollapse.classList.toggle('active');
    });
});

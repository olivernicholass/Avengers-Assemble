document.addEventListener('DOMContentLoaded', function() {

    const stars = document.querySelectorAll('.fa-star');

    stars.forEach(function(star) {
        star.addEventListener('mouseenter', function() {
            const rating = this.getAttribute('data-rating');
            highlight(rating);
        });

        star.addEventListener('click', function() {
            const rating = this.getAttribute('data-rating');
            document.getElementById('rating-value').value = rating;
            highlight(rating);
        });
        

        star.addEventListener('mouseleave', function() {
            const selectedRating = document.getElementById('rating-value').value;
            highlight(selectedRating);
        });
    });

    // Function to highlight the users rating selection
    // and convert it to stars. User wants to give a rating of 3:
    // they can select 3 stars, etc.

    function highlight(rating) {
        stars.forEach(function(s) {
            if (s.getAttribute('data-rating') <= rating) {
                s.style.color = '#03256C';
            } else {
                s.style.color = '';
            }
        });
    }

    var modal = document.getElementById('popup-modal');
    var homeButton = document.getElementById("home");

    // Redirection back to the home page POST review

    homeButton.addEventListener('click', function() {
        modal.style.display = 'none'; 
        window.location.href = "/";
    });

    // Function to ensure that the user leaves a star rating before submitting their review.

    function validateRating() {
        console.log("Validating rating...");
        const ratingValue = parseInt(document.getElementById("rating-value").value);
        if (ratingValue <= 0) {
            alert("Please select a rating.");
            return false;
        }
        return true;
    }

});

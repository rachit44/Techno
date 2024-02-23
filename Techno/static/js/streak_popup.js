document.addEventListener('DOMContentLoaded', function() {
    var popup = document.querySelector('.popup');
    var closeButton = document.querySelector('.close');

    // Open popup
    // Add event listener to trigger popup opening (e.g., a button click)
    // Example: document.getElementById('openPopupButton').addEventListener('click', openPopup);

    // Close popup when close button is clicked
    closeButton.addEventListener('click', closePopup);

    // Close popup when clicking outside of it
    window.addEventListener('click', function(event) {
        if (event.target == popup) {
            closePopup();
        }
    });

    // Function to open popup
    function openPopup() {
        popup.style.display = 'block';
    }

    // Function to close popup
    function closePopup() {
        popup.style.display = 'none';
    }
});

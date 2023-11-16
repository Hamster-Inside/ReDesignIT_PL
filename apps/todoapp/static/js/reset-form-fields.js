$(document).ready(function() {
    // Function to reset the form fields
    function resetFormFields() {
        $('form input[type="text"]').val('');
        $('form textarea').val('');
        // Add additional selectors if needed for other form elements
    }

    // Reset the form fields on document ready
    resetFormFields();

    // Reset the form fields when the page is shown (including when navigating back)
    $(window).on('pageshow', function(event) {
        if (event.originalEvent.persisted) {
            // Page was retrieved from the bfcache (back-forward cache)
            resetFormFields();
        }
    });
});
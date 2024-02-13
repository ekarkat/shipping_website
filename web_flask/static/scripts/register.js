

$(document).ready(function() {
    $('#states').change(function() {
        var stateId = $(this).val();
        // Make AJAX request to retrieve cities
        $.ajax({
            url: 'http://localhost:5600/api/v1/states/cities/' + stateId,
            type: 'GET',
            success: function(data) {
                // Clear existing options in cities dropdown
                $('#cities').empty();
                // Add new options for cities
                $.each(data, function(index, city) {
                    $('#cities').append($('<option>', {
                        value: city.id,
                        text: city.name
                    }));
                });
            },
            error: function(xhr, status, error) {
                // Handle error
                console.error(error);
            }
        });
    });
});
$.ajax({
    url: '',
    type: 'POST',
    data: $(this).serialize(),
    success: function(response) {
        if (response.success) {
            $('#responseMessage').html('<p style="color: green;">' + response.message + '</p>');
            $('#myForm')[0].reset(); // Reset the form
        } else {
            let errors = '';
            for (let field in response.errors) {
                errors += field + ': ' + response.errors[field].join(', ') + '<br>';
            }
            $('#responseMessage').html('<p style="color: red;">' + errors + '</p>');
        }
    },
    error: function(xhr, errmsg, err) {
        $('#responseMessage').html('<p style="color: red;">An error occurred while submitting the form.</p>');
    }
});

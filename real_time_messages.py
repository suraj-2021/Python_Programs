function fetchMessages() {
    $.ajax({
        url: '{url "message_app:inbox"}',  // URL to the inbox view
        method: 'GET',
        success: function(data) {
        
            $('#inbox').empty();

            
            data.forEach(function(message) {
                $('#inbox').append(
                    `<div class="message">
                        <strong>${message.sender}</strong>: ${message.message} <br>
                        <small>${message.timestamp}</small>
                    </div>`
                );
            });
        },
        error: function(xhr, status, error) {
            console.error('Error fetching messages:', error);
        }
    });
}

//fetch messages every 5 seconds
setInterval(fetchMessages, 5000);

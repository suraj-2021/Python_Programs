<html>
    <head>
        
        <meta name="csrf-token" content="{{ csrf_token() }}">
    </head>
    <body>
        <img src = "/static/rama.jpg" width = "20%" hight = "auto"/>
        
        <form action="{{ url_for('protected_form') }}" method="POST" name ="form">
            <input type="text" name="Name" placeholder="Enter your name"/>
            
            {{ form.csrf_token }}
            <input type="submit" value="Submit"/>
        </form>

       
        <form action="{{ url_for('unprotected_form') }}" method="POST">
            <input type="text" name="Name" placeholder="Enter your name"/>
            <button type="submit">Submit</button>
        </form>
    </body>
</html>

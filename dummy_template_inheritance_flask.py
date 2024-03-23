from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home()
    render_template('home.html')

if __name__ == '__main__':
   app.run(debug= True)

#creating a Html File
#base.html

<!DOCTYPE html>
<html lang = "en">
<head> 
<title> Template Inheritance Example </title>
</head>
<body>
  <h1> This heading is common in all webpages </h1>
  {%block content%}
   {%endblock%}
</body>
</html>

#extending our base.html file to welcome.html
{% extends "base.html" %}
   {%block content%}
     <h1> This html inherit from base.html and creates welcome.html <h1>
    {%endblock%}

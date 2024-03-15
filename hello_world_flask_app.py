from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "WSGI Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications. Werkzeug It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases."

if __name__ == "__main__":
    app.run()

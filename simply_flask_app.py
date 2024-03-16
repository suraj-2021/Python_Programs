from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def sunday():
    return 'Hello Welcom to our Site'

@app.route("/")
def index():
    return '<html>    <body>         <form action = "http://127.0.0.1:5000/login" method = "post">    <p> Enter Name: </p>  <p> <input type = "text" name = "nm"/> </p>    <p><input type = "submit" value = "submit"/> </p>  </form>  </body> </html>'

if __name__ == '__main__':
    app.run(debug= True)


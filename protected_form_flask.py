from flask import Flask, render_template, request
import secrets
from flask_wtf import CSRFProtect

app = Flask(__name__,template_folder='templates')


app.secret_key = secrets.token_hex(16)
csrf = CSRFProtect(app)

@app.route('/protected_form', methods=['GET', 'POST'])
def protected_form():
    
    if request.method == 'POST':
       
        name = request.form['Name']
        return "Hello " + name + "!!!"
    return render_template('index.html')

@app.route('/unprotected_form', methods=['GET', 'POST'])
def unprotected_form():
    
    if request.method == 'POST':
       
        name = request.form['Name']
        return "Hello " + name + "!!!"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

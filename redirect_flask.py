from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def welcome_admin():
    return "Welcome Admin"

@app.route('/guest/<guest>')
def welcome_guest(guest):
    return "Welcome %s as guest" % guest

@app.route('/user/<name>')
def hello_user(name):
 
    if name == 'admin':
        return redirect(url_for('welcoime_admin'))
    else:
        return redirect(url_for('welcome_guest'
                                , guest=name))
 
if __name__ == '__main__':
    app.run(debug=True)

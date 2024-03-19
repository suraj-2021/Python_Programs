from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return "HELLO THIS IS INDEX PAGE"

@app.route('/vstring/<name>')
def user_name(name):
  return "Hello %s" % name

@app.route('/vint/<int:age>')
def user_age(age):
  return "Your age is %d years old" % age

@app.route('/vfloat/<float:grade>')
def user_grade(grade):
  return "You obtain %f in your exam" % age


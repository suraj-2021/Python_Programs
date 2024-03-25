from flask import *
from distutils.log import debug
from fileinput import filename


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index1.html')

@app.route('/success', methods = ['POSt'])
def success():
   if request.method == "POST":
      f = request.files['file']
      f.save(f.filename)
      return render_template("acknowledge.html", name = f.filename)
   
if __name__ == '__main__':
   app.run(debug = True)

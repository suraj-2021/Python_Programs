from flask import Flask,request,render_template
import jinja2
app = Flask(__name__, template_folder='templates')


@app.route('/', methods = ['GET'])
def squarenumber():
    if request.method == 'GET':
       if (request.args.get("num")== None):
           return render_template("s.html")
       elif(request.args.get("num")== ' '):
           return "<h1> Invalid Number </h1>"
       else:
           number = request.args.get("num")
           sq = int(number) * int(number)

           return render_template('answer.html',squarenum = sq, num = number )

if __name__ == '__main__':
    app.run(debug = True)  

from flask import Flask 
from flask_mail import Mail, Message 

app = Flask(__name__) 
mail = Mail(app) 

# configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myemailId@gmail.com'
app.config['MAIL_PASSWORD'] = 'my_email_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

@app.route("/") 
def index(): 
msg = Message( 
				'Hello', 
				sender ='yourId@gmail.com', 
				recipients = ['receiver’sid1@gmail.com','receiver'sid2@gmail.com','receiver'sid3@gmail.com'] 
			) 
msg.body = 'This message is sent from Flask-Mail'
mail.send(msg) 
return 'Sent'

if __name__ == '__main__': 
app.run(debug = True) 

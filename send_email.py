from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'preetampatel22699@gmail.com'
app.config['MAIL_PASSWORD'] = '7019407078'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'preetampatel22699@gmail.com', recipients = ['preetmcit@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

   
if  __name__ == '__main__':
    app.run(debug=True, port=5000)
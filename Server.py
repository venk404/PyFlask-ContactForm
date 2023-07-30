from flask import Flask, render_template,request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



sender_email = ''
sender_password = ''
receiver_email = ''


app = Flask(__name__)


@app.route('/Login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        if (request.form['name'],request.form['email'],request.form['phone'],request.form['msgs']):
            if(send_email(request.form['name'],request.form['email'],request.form['phone'],request.form['msgs'])):
                return render_template('Thanks.html')
        else:
            error = 'Invalid username/password'
    elif request.method == 'GET':
        return render_template("index.html")



def send_email(name, email, number,message):
    subject = 'Contact Details'
    body = f'Name: {name}\nEmail: {email}\nPhone number: {number}\nMessage: {message}'

  
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
  
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  
        smtp_server.starttls() 

        smtp_server.login(sender_email, sender_password)

        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')

        smtp_server.quit()
    except Exception as e:
        print('Error: Unable to send email.')


if __name__ == "__main__":
    app.run(debug=False)
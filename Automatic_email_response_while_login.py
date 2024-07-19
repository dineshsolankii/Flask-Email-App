from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def send_welcome_email(sender_email, app_password, recipient_email, username):
    subject = "Welcome to Affirmation App"
    message = f"""
    <html>
    <body>
        <p>Dear {username},</p>
        <p>Welcome to Affirmation App! We are excited to have you on board.</p>
        <p>Feel free to explore our features and let us know if you have any questions.</p>
        <p>Best regards,<br>The Affirmation App Team</p>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        sender_email = " " # enter the sender's email
        app_password = " " # enter the app password obtained after 2-step verfication

        send_welcome_email(sender_email, app_password, email, username)
        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

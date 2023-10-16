import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailAutomation:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, receiver_email, text)
        server.quit()

# Usage
# email_automation = EmailAutomation('sender@gmail.com', 'password')
# email_automation.send_email('receiver@gmail.com', 'Subject', 'Email body')
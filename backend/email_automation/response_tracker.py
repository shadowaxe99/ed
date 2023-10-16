```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from backend.database.models.email import Email

class ResponseTracker:
    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.mail = smtplib.SMTP(self.server, self.port)
        self.mail.ehlo()
        self.mail.starttls()
        self.mail.login(self.username, self.password)

    def send_email(self, to_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        self.mail.sendmail(self.username, to_email, msg.as_string())

    def track_response(self, email_id, status):
        email = Email.query.get(email_id)
        if email:
            email.status = status
            email.save()

    def close_connection(self):
        self.mail.quit()
```
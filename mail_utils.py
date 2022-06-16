import time
import smtplib
import ssl
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(data):
    print("Sending mail to " + data[config.NAME_COLUMN] + " (" + data[config.EMAIL_COLUMN] + ")")
    code_list = [code for code in data[config.PAYLOAD_COLUMNS]]
    html_code_list ="""
    <b>
        <ul>
            <li>{}</li>
        </ul>
    </b>""".format("</li><li>".join(code_list))
    body = config.EMAIL_BODY.format(codes = html_code_list)
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = "Casai"
    message["To"] = data[config.EMAIL_COLUMN]
    message["Subject"] = config.EMAIL_SUBJECT

    # Add body to email
    message.attach(MIMEText(body, "html"))

    # Add attachment to message and convert message to string
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(config.SENDER_EMAIL, config.SENDER_PASSWORD)
        server.sendmail(config.SENDER_EMAIL, data[config.EMAIL_COLUMN], text)
    time.sleep(config.WAIT_TIME)
    return
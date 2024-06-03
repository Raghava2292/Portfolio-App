import smtplib as sm, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = 'raaghava92@gmail.com'
    password = os.getenv("PASSWORD")

    receiver = 'ragh9156@gmail.com'
    context = ssl.create_default_context()

    with sm.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
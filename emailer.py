import os

import smtplib
from email.message import EmailMessage


# Get credential from environmental variables.
# Not as secured, please be cautious about this.
PASSWORD = os.environ.get('emailer_password')
USER = os.environ.get('emailer_user')


def get_msg(to, subject, content):

    msg = EmailMessage()
    msg['Subject'] = f'{subject}'
    msg['From'] = USER
    msg['To'] = f'{to}'
    msg.set_content(f'{content}',)

    return msg

def send_email_to(to=USER, subject='title', content ='content'):

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
    
    except Exception as e:
        print(e)

    # login
    server.login(
        user=USER,
        password=PASSWORD,
    )

    server.send_message(
        msg=get_msg(to, subject, content)
    )

    server.quit()

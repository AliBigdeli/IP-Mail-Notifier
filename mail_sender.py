from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import smtplib
import sys


def sendmail(sender,passwd,recipients,sub,text):
    msg = MIMEMultipart()
    if (sub != None):
        msg['Subject'] = sub
    msg['From'] = sender
    msg['Reply-to'] = recipients

    msg.preamble = 'Multipart massage.\n' 
    part = MIMEText(text)
    msg.attach(part)
    #server = smtplib.SMTP('smtp_address', port)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(sender,passwd)
    try:
        server.sendmail(msg['From'], recipients , msg.as_string())
        print('email sent and ip have been notified')
    except:
        print('something went wrong and not sent')     
    server.quit()


#sendmail("address of the sender","password of sender","reciever","subject","body text")
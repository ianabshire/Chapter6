import smtplib, imaplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read():
    
    mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    username = 'ianabshire@gmail.com'
    password = 'abshire1'
    mailserver.login(username, password)

    status, count = mailserver.select('Inbox')
    status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')

    print(data[0][1])

    mailserver.close()
    mailserver.logout()

def send():
    
    fromaddr = "ianabshire@gmail.com"
    toaddr = "bigboard1080@sbcglobal.net"
    text = "Test message sent from Python"
    username = "ianabshire@gmail.com"
    password = "abshire1"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Test'
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()

import smtplib
from datetime import datetime
# import getpass

SMTP_SERVER = YOUR_MAIL_SERVER
SMTP_TLS_PORT = YOUR_SMTP_PORT
MAIL_APP_PASSWORD = YOUR_MAIL_APP_PASSWORD
SMTP_DEBUG = False
SMTP_LOG = True

fromEmail = YOUR_SENDER_EMAIL
fromName = Your_SENDER_NAME
toMail =  YOUR_RECIPIENT_EMAIL 
#password = getpass.getpass("password") # the password for smtp server 

subject = "What is Lorem Ipsum?"
mailbody = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \r\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \r\nIt was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
msg = f"From: {fromName}  <{fromEmail}>\nTo: {toMail}\nSubject: {subject}\n\n {mailbody}"

smtp = smtplib.SMTP(SMTP_SERVER,SMTP_TLS_PORT) 
if SMTP_DEBUG :
    smtp.set_debuglevel(True) 
smtpGreet   = smtp.ehlo() 
smtptls     = smtp.starttls() 
smtpLogin   = smtp.login(fromEmail,MAIL_APP_PASSWORD)
sent        = smtp.sendmail(fromEmail, toMail, msg)
# print(smtp.getreply())
smtpClose   = smtp.quit()

if len(sent) > 0 :
    print("Mail could not be sent. please check the debug for further info")
else:
    print(f"yupiee!! Mail is sent to {toMail}")


#debug log 
if SMTP_LOG :
    logString = f"[{datetime.now()}]: {str(smtp)}\r\n[{datetime.now()}]: {str(smtpGreet) } \r\n[{datetime.now()}]: {str(smtptls) } \r\n[{datetime.now()}]: {str(smtpLogin) } \r\n[{datetime.now()}]: {str(sent) } \r\n[{datetime.now()}]:{str(smtpClose)}"
    f = open("smtp.log", "a")
    f.write(logString)
    f.close()







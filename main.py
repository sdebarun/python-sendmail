import smtplib

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_TLS_PORT = 587
MAIL_APP_PASSWORD = <MAIL_APP_PASSWORD>
SMTP_DEBUG = False #set the smtp debug level

fromEmail = <SENDER_EMAIL>
toMail =  <RECIPIENT_EMAIL> # the to email

subject = "Test python mail"
mailbody = "This is a test email sent form python script I have wrote in repl.it"
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromEmail, toMail, subject, '29/09/2021', mailbody )

subject1 = "python mail with f string literal"
mailbody1 = "lorem ipsum dolor sit ammet"
msg1 = f"From: {fromEmail}\nTo: {toMail}\nSubject: {subject1}\n\n {mailbody1}"

smtp = smtplib.SMTP(SMTP_SERVER,SMTP_TLS_PORT) #settig up smtp server
if SMTP_DEBUG :
    smtp.set_debuglevel(True) 
smtp.ehlo() # establishing the connection with server
smtp.starttls() # starting the tls connection 
smtp.login(fromEmail,MAIL_APP_PASSWORD)

smtp.sendmail(fromEmail, toMail, msg)
smtp.sendmail(fromEmail, toMail, msg1)

print(smtp.getreply())
smtp.quit()




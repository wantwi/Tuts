import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username ="bill.kobbyacc@gmail.com"
password ='Kobby@123'



def send_mail(text="Email body", subject="Hello Kobby",from_email =username,to_emails=[]):
    #if isinstance(to_emails,list):
    assert isinstance(to_emails,list)

    msg =MIMEMultipart('alternative')
    msg['From']= from_email
    msg['To'] =", ".join(to_emails)
    msg ['Subject'] = subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part = MIMEText("<h1>Could this working</h1>",'html')
    msg.attach(html_part)

    msgStr =msg.as_string()

    server = smtplib.SMTP(host="smtp.gmail.com",port=587)

    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email, to_emails,msgStr)
    server.quit()




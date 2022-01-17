import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .email_conf import EMAIL_LOGIN, EMAIL_PASSWORD

def registration_email(reciever, csrfmiddlewaretoken):

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = EMAIL_LOGIN
        msg['To'] = reciever



        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = f"""\
                <html>
                        <head></head>
                        <body>
                                <p>Hi!<br>
                                How are you?<br>
                                Here is the <a href="vk.com">link</a> you wanted.
                                </p>
                        </body>
                </html>
                """

        part1 = MIMEText(text,'plain')
        part2 = MIMEText(html,'html')

        msg.attach(part1)
        msg.attach(part2)

        # Конфигурация SMTP сервера
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        # Логининимься к почте
        smtpObj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        # Отправляем сообщение от EMAIL_LOGIN к reciever
        smtpObj.sendmail(EMAIL_LOGIN, reciever, f"Your registration link: 127.0.0.1:8000/^email_verif/$?csrfmiddlewaretoken={csrfmiddlewaretoken}&email={reciever.replace('@', '%40')}")
        smtpObj.sendmail(EMAIL_LOGIN, reciever, msg.as_string())
        # Отключаемся от SMTP сервера
        smtpObj.quit()

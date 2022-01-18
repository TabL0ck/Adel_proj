import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .email_conf import EMAIL_LOGIN, EMAIL_PASSWORD

def registration_email(reciever, csrfmiddlewaretoken):

        html = f"""\
                <html>
                        <head></head>
                        <body>
                                <h1>Регистрация</h1>
                                <h3>Для перехода на страницу регистрации перейдите по ссылке: </h3>
                                <h3><a href="http://127.0.0.1:8000/^email_verif/$?csrfmiddlewaretoken={csrfmiddlewaretoken}&email={reciever.replace('@', '%40')}">Зарегестрироваться</a></h3>
                                </p>
                        </body>
                </html>
                """
        msg = MIMEText(html,'html')
        msg['Subject'] = "Регистрация на портале АдельПродакшн"
        msg['From'] = EMAIL_LOGIN
        msg['To'] = reciever

        # Конфигурация SMTP сервера
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        # Логининимься к почте
        smtpObj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        print('test')
        # Отправляем сообщение от EMAIL_LOGIN к reciever
        #smtpObj.sendmail(EMAIL_LOGIN, reciever, f"Your registration link: 127.0.0.1:8000/^email_verif/$?csrfmiddlewaretoken={csrfmiddlewaretoken}&email={reciever.replace('@', '%40')}")
        smtpObj.sendmail(EMAIL_LOGIN, reciever, msg.as_string())
        # Отключаемся от SMTP сервера
        smtpObj.quit()

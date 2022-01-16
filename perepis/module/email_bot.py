import smtplib
from .email_conf import EMAIL_LOGIN, EMAIL_PASSWORD

def registration_email(reciever):

        # Конфигурация SMTP сервера
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        # Логининимься к почте
        smtpObj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        # Отправляем сообщение от EMAIL_LOGIN к reciever
        smtpObj.sendmail(EMAIL_LOGIN, reciever, "Your registration link: 127.0.0.1:8000/email_verif")
        # Отключаемся от SMTP сервера
        smtpObj.quit()

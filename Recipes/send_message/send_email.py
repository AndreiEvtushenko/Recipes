import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()

# Параметры SMTP-сервера
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')

# Адреса отправителя и получателя
sender_email = 'evtushenkoad@gmail.com'
receiver_email = 'evtushenkoad@gmail.com'

# Создание объекта сообщения
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Пример отправки почты из Python'

# Текст сообщения
message_text = 'Привет, это пример отправки почты из Python!'
message.attach(MIMEText(message_text, 'plain'))

# Создание SMTP-соединения и отправка сообщения
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
        print('Почта успешно отправлена!')
except Exception as e:
    print('Возникла ошибка при отправке почты:', str(e))

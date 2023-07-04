#На стадии разработки
from django.conf import settings
from django.core.mail import send_mail
import os

import requests
from dotenv import load_dotenv
import telegram
from telegram.error import TelegramError


load_dotenv()

#TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
#bot = telegram.Bot(token=TELEGRAM_TOKEN)


def send_telegram_message(name, text, email):
    pass


def send_email_message(name, text, email):
    subject = f'The massage was sent from:\n {name}\n.'
    message = (
        f'Message text:\n {text}.\n'
        f'Was sent from:\n {email}.'
        )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['lightangel_89@mail.ru'],
    )

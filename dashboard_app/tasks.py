from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives


def send_mail_task(to_mail):
    subject, from_email, to = 'Invite', 'cavidan.mahmudoglu@gmail.com', to_mail
    text_content = f'Bu mesaj {to} mailine ugurla gonderildi'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.send()
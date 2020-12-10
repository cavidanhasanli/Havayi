from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
from dashboard_app.models import BlankCredit
from io import StringIO
import csv


def send_mail_task(instance):

    csv_file = StringIO()
    header = ['Ad/Soyad',
              'Əlaqə Nömrə',
              'Müraciət olunan kredit məbləği',
              'ID',
              'Təsdiqlənmiş kredit məbləği',
              'Status',
              'Kreditin növü',
              'Bank']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    csv_writer.writeheader()

    csv_writer.writerow({'Ad/Soyad': instance.name_surname,
                         'Əlaqə Nömrə': instance.phone_number,
                         'Müraciət olunan kredit məbləği': instance.amount,
                         'ID': instance.user_id.MY_USER_ID,
                         'Kreditin növü': instance.credit_type,
                         'Bank': instance.bank_id})

    subject, from_email, to = 'Invite', 'cavidan.mahmudoglu@gmail.com', instance.bank_id.bank_email
    text_content = f'Bu mesaj {to} mailine ugurla gonderildi'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach('invoice.csv', csv_file.getvalue(), 'text/csv')
    msg.send()

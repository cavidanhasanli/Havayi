from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard_app.tasks import send_mail_task
from threading import Thread
from dashboard_app.models import BankList


@receiver(post_save,sender=BankList)
def bank_send_mail(sender,instance,created,**kwargs):
    print('INSTANCE:',instance)
    background = Thread(target=send_mail_task, args=[instance])
    background.start()

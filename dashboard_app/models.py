from django.db import models
from user_app.models import MyUser


# Create your models here.

class CreditFields(models.Model):
    credit_slug = models.SlugField()
    credit_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.credit_name


class BlankCredit(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    amount = models.IntegerField()
    credit_type = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, auto_created=True)
    send_user_num = models.IntegerField()
    otp_status = models.BooleanField("otp status", default=False)

    def __str__(self):
        return f'{self.name} {self.surname} | Credit Type : {self.credit_type} | User Number : {self.send_user_num}'

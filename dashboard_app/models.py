from django.db import models
from user_app.models import MyUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CreditFields(models.Model):
    credit_slug = models.SlugField()
    credit_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.credit_name


class BankList(models.Model):
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    bank_email = models.EmailField(null=True, blank=True)
    credit_type = models.ForeignKey(CreditFields, on_delete=models.CASCADE, null=True, blank=True)
    interest = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100)], default=0.0, null=True,
                                 blank=True)

    def __str__(self):
        return self.bank_name


class BlankCredit(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name_surname = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    amount = models.IntegerField()
    credit_type = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, auto_created=True)
    send_user_num = models.CharField(max_length=255, null=True, blank=True, default='0')
    otp_status = models.BooleanField("otp status", default=False)
    bank_id = models.ForeignKey(BankList, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name_surname} | Credit Type : {self.credit_type} | User Number : {self.send_user_num}'


class SendedBlank(models.Model):

    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name_surname = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    amount = models.IntegerField()
    credit_type = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, auto_created=True)
    send_user_num = models.CharField(max_length=255, null=True, blank=True, default='0')
    otp_status = models.BooleanField("otp status", default=False)
    bank_id = models.ForeignKey(BankList, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name_surname} | Credit Type : {self.credit_type} | User Number : {self.send_user_num}'

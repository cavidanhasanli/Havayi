from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class MyUser(AbstractUser):
    phone = models.CharField(max_length=100, blank=True, null=True, unique=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    is_phone_status = models.BooleanField("phone status", default=False)
    MY_USER_ID = models.CharField(max_length=255,null=True,blank=True,default=None)
    cash_back = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100000)], default=0.0,null=True,blank=True)

    def __str__(self):
        return self.username


class PhoneOTP(models.Model):
    phone = models.CharField(max_length=100, unique=True)
    otp = models.CharField(max_length=9, null=True, blank=True)
    count = models.IntegerField(default=0, help_text="Nomreye otp code gonderildi")
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.phone} / otp code : {self.otp}"

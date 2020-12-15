# models.py
from django.db import models



class BankFiles(models.Model):
    files = models.FileField(upload_to='Bank_Inovice',null=True,blank=True)

    def __str__(self):
        return f'{self.files}'
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.

CHOICE = (('現金','現金'),('カード','カード'),('タクシーチケット','チケット'),('paypay','PayPay'),('その他','その他'))



class TaxiModel(models.Model):
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
        ) 
    regist_date = models.DateTimeField(default=timezone.now)
    myinteger = models.IntegerField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    

    def __str__(self):
        return self.priority
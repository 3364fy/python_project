from django.db import models

# Create your models here.

class class1(models.Model):
    buy_date=models.DateField(null=False,blank=False)
    # name = models.CharField(max_length=32)
    # password = models.CharField(max_length=64)
    # age = models.IntegerField()
    def __str__(self):
        return str(self.buy_date)

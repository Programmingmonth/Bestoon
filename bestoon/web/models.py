from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __unicode__(self):
        return "{}_token".format(self.user)


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __unicode__(self):
        return "{}-{}".format(self.date, self.amount)
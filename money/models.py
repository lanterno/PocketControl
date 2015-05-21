import datetime
from django.db import models
from accounts.models import User


class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)


class Income(models.Model):
    user = models.ForeignKey(User, related_name='income')
    money = models.FloatField(default=0)
    category = models.ForeignKey(IncomeCategory)


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    money = models.FloatField(default=0)
    category = models.ForeignKey(ExpenseCategory)
    details = models.CharField(max_length=255, null=True, blank=True)
    date_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.date_time = datetime.datetime.now()
        super(Expense, self).save(*args, **kwargs)

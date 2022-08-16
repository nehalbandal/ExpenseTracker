from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords

from core.models import BaseModelMixin


class MoneyCollection(BaseModelMixin):
    name = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='money_added', null=True,
                                 on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='money_modified', null=True,
                                 on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return "{}({}₹)".format(self.name, int(round(self.amount)))

    class Meta:
        verbose_name = 'Money Collection'
        verbose_name_plural = 'Money Collection'


class Expense(BaseModelMixin):
    expense_name = models.CharField(max_length=300)
    expense_desc = models.CharField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    expense_owner = models.CharField(max_length=300)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='expense_added', null=True,
                                 on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='expense_modified', null=True,
                                 on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return "{}({}₹)".format(self.expense_name, int(round(self.amount)))

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

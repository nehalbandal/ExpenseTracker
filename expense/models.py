from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from core.models import BaseModelMixin


class MoneyCollection(BaseModelMixin):
    BUILDING_CHOICES = [('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'),
                        ('B1', 'B1'), ('B2', 'B2'), ('OTHERS', 'Others')]
    STATUS = [('PENDING', 'Pending'), ('PAID', 'Paid')]

    building = models.CharField(max_length=300, choices=BUILDING_CHOICES, default='OTHERS')
    flat_no = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=300)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=300, choices=STATUS, default='PENDING')
    note = models.CharField(max_length=500, blank=True, null=True)
    attachment = models.FileField(_("Attachment"), upload_to='collection/%Y/%m/%d/', blank=True, max_length=255)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='money_added', null=True,
                                 on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='money_modified', null=True,
                                    on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return "{}-{}({}₹)".format(self.building, self.flat_no, int(round(self.amount)))

    class Meta:
        verbose_name = 'Money Collection'
        verbose_name_plural = 'Money Collection'


class Expense(BaseModelMixin):
    expense_name = models.CharField(max_length=300)
    expense_desc = models.CharField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    expense_owner = models.CharField(max_length=300)
    note = models.CharField(max_length=500, blank=True, null=True)
    attachment = models.FileField(_("Attachment Path"), upload_to='expenses/%Y/%m/%d/', blank=True, max_length=255)
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


@receiver(post_save, sender=MoneyCollection)
def update_status(sender, instance, created, **kwargs):
    print("In signal...", created)
    if created and instance.building != 'OTHERS':
        already_paid = MoneyCollection.objects.filter(building=instance.building,
                                                      flat_no=instance.flat_no).count()
        if already_paid > 1:
            print("Deleting..because record is already created")
            instance.delete()

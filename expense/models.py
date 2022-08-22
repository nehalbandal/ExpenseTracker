import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from core.models import BaseModelMixin
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class MoneyCollection(BaseModelMixin):
    BUILDING_CHOICES = [('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'),
                        ('B1', 'B1'), ('B2', 'B2'), ('OTHERS', 'Others')]
    STATUS = [('PENDING', 'Pending'), ('PAID', 'Paid')]
    COLLECTION_TYPE = [('VARGANI', 'Vargani'), ('SAVING', 'Saving'), ('OTHERS', 'Others')]
    PAYMENT_METHOD = [('CASH', 'Cash'), ('UPI', 'UPI')]

    building = models.CharField(max_length=300, choices=BUILDING_CHOICES, default='OTHERS')
    flat_no = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=300)
    amount = models.PositiveIntegerField(default=0)
    type = models.CharField(_('Collection Type'), max_length=300, choices=COLLECTION_TYPE, default='VARGANI')
    payment_method = models.CharField(_('Payment Method'), max_length=300, choices=PAYMENT_METHOD, default='CASH')
    collection_date = models.DateField(_("Collection Date"), blank=True, null=True, default=datetime.date.today)
    status = models.CharField(max_length=300, choices=STATUS, default='PENDING')
    note = models.CharField(max_length=500, blank=True, null=True)
    attachment = models.ImageField(_("Attachment"), upload_to='collection/%Y/%m/%d/', blank=True, max_length=255)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='money_added', null=True,
                                 on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='money_modified', null=True,
                                    on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return "{}-{}({}₹)".format(self.building, self.flat_no, int(round(self.amount)))

    def save(self, *args, **kwargs):
        if self.attachment:
            new_image = compress(self.attachment)
            self.attachment = new_image
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Money Collection'
        verbose_name_plural = 'Money Collection'


class Expense(BaseModelMixin):
    expense_name = models.CharField(max_length=300)
    expense_desc = models.CharField(max_length=500, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    expense_owner = models.CharField(max_length=300)
    note = models.CharField(max_length=500, blank=True, null=True)
    expense_date = models.DateField(_("Expense Date"), blank=True, null=True, default=datetime.date.today)
    attachment = models.ImageField(_("Attachment"), upload_to='expenses/%Y/%m/%d/', blank=True, max_length=255)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='expense_added', null=True,
                                 on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='expense_modified', null=True,
                                    on_delete=models.SET_NULL)
    history = HistoricalRecords()

    def __str__(self):
        return "{}({}₹)".format(self.expense_name, int(round(self.amount)))

    def save(self, *args, **kwargs):
        if self.attachment:
            new_image = compress(self.attachment)
            self.attachment = new_image
        super().save(*args, **kwargs)

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

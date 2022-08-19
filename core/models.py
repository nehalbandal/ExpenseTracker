from django.contrib.auth.models import User, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class BaseModelMixin(models.Model):
    modification_date = models.DateTimeField(_("Modification Date"), auto_now=True)
    creation_date = models.DateTimeField(_("Creation Date"), auto_now_add=True)

    class Meta:
        abstract = True


# @receiver(post_save, sender=User)
# def user_saved(sender, instance, created, **kwargs):
#     all_perms = []
#     for grp in instance.groups.all():
#         all_perms += grp.permissions.values_list('id')
#     all_perms = [a[0] for a in all_perms]
#     perms = Permission.objects.filter(id__in=all_perms)
#     print(instance.user_permissions.all())
#     instance.user_permissions.set({})
#     print(instance.user_permissions.all())
#     instance.user_permissions.add(*perms)
#     instance.save()
#     print(instance.user_permissions.all())

import os
import sys

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission

from datetime import date


class CustomUserAdmin(UserAdmin):
    list_display = ('username',)
    search_fields = ()
    list_filter = []

    def save_related(self, request, form, formsets, change):
        try:
            super(CustomUserAdmin, self).save_related(request, form, formsets, change)
            if 'groups' in form.changed_data:
                user = User.objects.get(username=form.cleaned_data['username'])
                # print("Groups: ", user.groups.all())
                # print("Old: ", user.user_permissions.all())
                all_perms = []
                for grp in user.groups.all():
                    all_perms += grp.permissions.values_list('id')
                all_perms = [a[0] for a in all_perms]
                perms = Permission.objects.filter(id__in=all_perms)
                user.user_permissions.set({})
                user.user_permissions.add(*perms)
                # print("New: ", user.user_permissions.all())
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("#" * 10)
            print("Exception: ", e)
            print(exc_type, fname, exc_tb.tb_lineno)
            print("#" * 10)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(LogEntry)
admin.site.site_header = f'Kamal Residency: Ganpati {date.today().year}'
admin.site.index_title = 'Money Management'

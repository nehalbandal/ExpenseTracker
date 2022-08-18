from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username',)
    search_fields = ()
    list_filter = []


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(LogEntry)
admin.site.site_header = 'Kamal Residency: Ganpati 2022'
admin.site.index_title = 'Money Management'

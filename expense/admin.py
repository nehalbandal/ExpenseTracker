from django.contrib import admin
from .models import *


class MoneyAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_amount', 'added_by', 'modified_by']
    fieldsets = (
        (None, {'fields': ('name', 'amount',), }),
    )

    def get_amount(self, obj):
        return int(round(obj.amount))

    get_amount.short_description = 'Amount(₹)'

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.modified_by = request.user
        instance.save()


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['expense_name', 'get_amount', 'expense_owner', 'added_by', 'modified_by']
    fieldsets = (
        (None, {'fields': ('expense_name', 'amount', 'expense_owner',), }),
    )

    def get_amount(self, obj):
        return int(round(obj.amount))

    get_amount.short_description = 'Amount(₹)'

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.modified_by = request.user
        instance.save()


admin.site.register(MoneyCollection, MoneyAdmin)
admin.site.register(Expense, ExpenseAdmin)

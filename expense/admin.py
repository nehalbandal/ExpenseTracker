from django.contrib import admin
from .models import *
from django.contrib.admin.filters import AllValuesFieldListFilter
from .forms import CollectionForm


class DropdownFilter(AllValuesFieldListFilter):
    template = 'admin/dropdown_filters.html'


class MoneyAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_flat_no', 'status', 'amount']
    fieldsets = (
        (None, {'fields': ('building', 'flat_no', 'name', 'amount', 'note', 'attachment', 'added_by', 'modified_by'), }),
    )
    readonly_fields = ['added_by', 'modified_by']
    list_filter = [('building', DropdownFilter)]
    search_fields = ('name',)
    # list_editable = ['amount']
    # form = CollectionForm

    def get_flat_no(self, obj):
        return "{}-{}".format(obj.building, obj.flat_no)

    get_flat_no.short_description = 'Flat No.'

    def get_queryset(self, request):
        queryset = super(MoneyAdmin, self).get_queryset(request)
        return queryset.order_by('building', 'flat_no')

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.modified_by = request.user
        if instance.amount > 0:
            instance.status = 'PAID'
        else:
            instance.status = 'PENDING'
        instance.save()


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['expense_name', 'get_amount', 'expense_owner',]
    fieldsets = (
        (None, {'fields': ('expense_name', 'amount', 'expense_owner', 'note', 'attachment', 'added_by', 'modified_by'),
                }),
    )
    readonly_fields = ['added_by', 'modified_by']

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

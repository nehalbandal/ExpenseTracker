import csv
import time

from django.contrib import admin
from django.http import HttpResponse

from .models import *
from django.contrib.admin.filters import AllValuesFieldListFilter
from .forms import CollectionForm


class DropdownFilter(AllValuesFieldListFilter):
    template = 'admin/dropdown_filters.html'


class MoneyAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_flat_no', 'status', 'amount']
    fieldsets = (
        (None, {'fields': ('building', 'flat_no', 'name', 'amount', 'type', 'payment_method', 'note', 'attachment',
                           'added_by', 'modified_by'), }),
    )
    readonly_fields = ['added_by', 'modified_by']
    list_filter = [('building', DropdownFilter)]
    search_fields = ('name',)
    form = CollectionForm
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        field_names = ['building', 'flat_no', 'name', 'amount', 'type', 'payment_method', 'status', 'note',
                       'attachment', 'added_by', 'modified_by', 'creation_date', 'modification_date', ]

        response = HttpResponse(content_type='text/csv')
        datetime = time.strftime("%Y%m%d_%H%M%S")
        filename =  "money_collection_" + datetime
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(filename)
        writer = csv.writer(response)
        print(field_names)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

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
        (None, {'fields': ('expense_name', 'amount', 'expense_owner', 'note', 'attachment', 'added_by',
                           'modified_by'),
                }),
    )
    readonly_fields = ['added_by', 'modified_by']

    def get_amount(self, obj):
        return int(round(obj.amount))

    get_amount.short_description = 'Amount(₹)'

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        field_names = ['expense_name', 'expense_desc', 'amount', 'expense_owner', 'note', 'attachment', 'added_by',
                       'modified_by', 'creation_date', 'modification_date', ]

        response = HttpResponse(content_type='text/csv')
        datetime = time.strftime("%Y%m%d_%H%M%S")
        filename = "expenses_" + datetime
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(filename)
        writer = csv.writer(response)
        print(field_names)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.modified_by = request.user
        instance.save()


admin.site.register(MoneyCollection, MoneyAdmin)
admin.site.register(Expense, ExpenseAdmin)

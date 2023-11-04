import csv
import time

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from .models import *
from django.contrib.admin.filters import AllValuesFieldListFilter
from .forms import CollectionForm, ExpenseForm


class DropdownFilter(AllValuesFieldListFilter):
    template = 'admin/dropdown_filters.html'


class MoneyAdmin(admin.ModelAdmin):
    list_display = ['get_flat_no', 'collection_date', 'type', 'amount']
    fieldsets = (
        (None, {'fields': ('year', 'collection_date', 'building', 'flat_no', 'name', 'amount', 'type', 'payment_method', 'note', 'attachment',
                           'added_by', 'modified_by'), }),
    )
    readonly_fields = ['added_by', 'modified_by']
    list_filter = [('building', DropdownFilter), ('year', DropdownFilter)]
    search_fields = ('name',)
    form = CollectionForm
    actions = ["export_as_csv"]
    sortable_by = ['collection_date', 'status', 'amount']

    def export_as_csv(self, request, queryset):
        field_names = ['collection_date', 'building', 'flat_no', 'name', 'amount', 'type', 'payment_method', 'status', 'note',
                       'attachment', 'added_by', 'modified_by', 'creation_date', 'modification_date', ]

        response = HttpResponse(content_type='text/csv')
        curr_datetime = time.strftime("%Y%m%d_%H%M%S")
        filename = "money_collection_" + curr_datetime
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(filename)
        writer = csv.writer(response)
        print(field_names)
        writer.writerow(field_names)
        for obj in queryset.order_by('collection_date'):
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

    def get_flat_no(self, obj):
        if obj.name != "":
            return obj.name
        return "{}-{}".format(obj.building, obj.flat_no) if obj.building != "OTHERS" else obj.name

    get_flat_no.short_description = 'Name'

    def get_queryset(self, request):
        queryset = super(MoneyAdmin, self).get_queryset(request)
        return queryset.order_by('-year', 'building', 'flat_no')

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
    list_display = ['expense_name', 'expense_type', 'get_amount', 'get_attachment']
    fieldsets = (
        (None, {'fields': ('year', 'expense_date', 'expense_name', 'expense_type', 'amount', 'expense_owner', 'note', 'attachment', 'added_by',
                           'modified_by'),
                }),
    )
    readonly_fields = ['added_by', 'modified_by']
    list_filter = [('year', DropdownFilter)]
    form = ExpenseForm
    actions = ["export_as_csv"]

    def get_amount(self, obj):
        return int(round(obj.amount))

    get_amount.short_description = 'Amount(₹)'

    def get_attachment(self, obj):
        if obj.attachment:
            return format_html('<a href="{}">Bill</a>'.format(obj.attachment.url))
        return "-"

    get_attachment.short_description = 'Attachment'

    def export_as_csv(self, request, queryset):
        field_names = ['expense_date', 'expense_name', 'expense_desc', 'amount', 'expense_owner', 'note', 'attachment', 'added_by',
                       'modified_by', 'creation_date', 'modification_date', ]

        response = HttpResponse(content_type='text/csv')
        curr_datetime = time.strftime("%Y%m%d_%H%M%S")
        filename = "expenses_" + curr_datetime
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(filename)
        writer = csv.writer(response)
        print(field_names)
        writer.writerow(field_names)
        for obj in queryset.order_by('expense_date'):
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

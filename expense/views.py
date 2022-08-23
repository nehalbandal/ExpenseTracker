from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


@login_required
def add_default_flat_data(request):
    try:
        buildings = {
            'A1': 14,
            'A2': 14,
            'A3': 14,
            'A4': 14,
            'B1': 16,
            'B2': 16
        }

        for wing, flats in buildings.items():
            for i in range(1, flats+1):
                name = "{}-{}".format(wing, i)
                MoneyCollection.objects.create(building=wing, flat_no=i, name=name,
                                               added_by=request.user, modified_by=request.user)

        return HttpResponse("Data Added Successfully!")
    except Exception as e:
        print(e)
        return HttpResponse("Data Loading Failed! ")


def show_summary(request):
    collection_result = MoneyCollection.objects.filter(type='VARGANI', status="PAID")\
        .values('collection_date')\
        .annotate(total_collection=Sum('amount')) \
        .annotate(total_count=Count('collection_date')) \
        .order_by()
    total_collection_count = MoneyCollection.objects.filter(type='VARGANI', status="PAID").count()
    expense_result = Expense.objects.values('expense_date')\
        .annotate(total_expense=Sum('amount'))\
        .order_by()
    print(total_collection_count)
    return render(request, template_name='summary.html', context={'collection_result': collection_result,
                                                                  'expense_result': expense_result,
                                                                  'total_collection_count': total_collection_count})

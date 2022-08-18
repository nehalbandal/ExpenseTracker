# django imports
from django.conf import settings
from django.db.models import Sum

from expense.models import MoneyCollection, Expense


def settings_media(request):
    total_expense = Expense.objects.all().aggregate(Sum('amount'))
    total_collection = MoneyCollection.objects.filter(status='PAID').aggregate(Sum('amount'))
    total_collection = total_collection.get('amount__sum', 0) if total_collection.get('amount__sum', 0) else 0
    total_expense = total_expense.get('amount__sum', 0) if total_expense.get('amount__sum', 0) else 0
    return {'setting': settings, 'total_collection': total_collection, 'total_expense': total_expense, }


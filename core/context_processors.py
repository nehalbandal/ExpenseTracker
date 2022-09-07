# django imports
from django.conf import settings
from django.db.models import Sum

from expense.models import MoneyCollection, Expense


def settings_media(request):
    total_expense = Expense.objects.all().aggregate(Sum('amount'))
    total_expense = total_expense.get('amount__sum', 0) if total_expense.get('amount__sum', 0) else 0

    total_collection = MoneyCollection.objects.filter(status='PAID').aggregate(Sum('amount'))
    total_collection = total_collection.get('amount__sum', 0) if total_collection.get('amount__sum', 0) else 0

    total_vargani_collection = MoneyCollection.objects.filter(type='VARGANI', status='PAID').aggregate(Sum('amount'))
    total_vargani_collection = total_vargani_collection.get('amount__sum', 0) if total_vargani_collection.get('amount__sum', 0) else 0
    total_vargani_count = MoneyCollection.objects.filter(type='VARGANI', status='PAID').count()

    total_m_vargani_collection = MoneyCollection.objects.filter(type='MAHA_PRASAD_VARGANI', status='PAID').aggregate(
        Sum('amount'))
    total_m_vargani_collection = total_m_vargani_collection.get('amount__sum', 0) if total_m_vargani_collection.get(
        'amount__sum', 0) else 0
    total_m_vargani_count = MoneyCollection.objects.filter(type='MAHA_PRASAD_VARGANI', status='PAID').count()

    remaining = total_collection-total_expense

    return {
        'setting': settings,
        'total_collection': total_collection,
        'total_expense': total_expense,
        'total_vargani_collection': total_vargani_collection,
        'total_vargani_count': total_vargani_count,
        'total_m_vargani_collection': total_m_vargani_collection,
        'total_m_vargani_count': total_m_vargani_count,
        'remaining': remaining
    }


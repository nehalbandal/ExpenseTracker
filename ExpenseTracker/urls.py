"""ExpenseTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db.models import Sum
from django.urls import path

from expense.models import MoneyCollection, Expense

total_expense = Expense.objects.all().aggregate(Sum('amount'))
total_collection = MoneyCollection.objects.all().aggregate(Sum('amount'))

urlpatterns = [
    path('admin/', admin.site.urls, {'extra_context': {'total_expense': total_expense.get('amount__sum', 0),
                                                       'total_collection': total_collection.get('amount__sum', 0)}
                                     }
         ),
]

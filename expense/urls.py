from django.urls import path
from .views import *

urlpatterns = [
    path('load-data/', add_default_flat_data, name='add_default_flat_data')
]
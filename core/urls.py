# django imports
from django.urls import path, include
from .views import index, view_only


urlpatterns = [
    path('', index, name="index"),
    path('show-data/', view_only, name='view_only'),
]
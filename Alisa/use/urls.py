from django.urls import path
from . import api

urlpatterns = [
    path('', api.main, name='main'),
]
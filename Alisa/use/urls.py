from django.urls import path
from . import api, views

urlpatterns = [
    path('', views.post, name='main'),
]
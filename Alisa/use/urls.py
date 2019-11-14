from django.urls import path
from . import api

urlpatterns = [
    path('', api.handle_dialog, name='handle_dialog'),
]
from django.utils.http import is_safe_url, urlunquote
from django.shortcuts import render
from django.http import JsonResponse
from .api import main
import requests


def post(request):


    return JsonResponse({'foo': 'bar'})


from django.utils.http import is_safe_url, urlunquote
from django.shortcuts import render
from django.http import JsonResponse
from .api import main
import requests


def post(request):

    if request.method == "POST":
        return JsonResponse({'foo': 'bar'})
        word = "post"

    else:
        word = "hello"
    return render(request, 'use/main.html', {'word': word})

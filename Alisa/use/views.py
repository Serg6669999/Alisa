from django.utils.http import is_safe_url, urlunquote
from django.shortcuts import render
import requests


def post(request):

    if request.method == "POST":
        post_data = {'name': 'Да'}
        response = requests.post('https://dialogs.yandex.ru/developer/skills/f8eb61f3-8faf-4180-a9f5-0cd2b76c52ff/draft/test', data=post_data)
        content = response.content
        word = "post"

    else:
        word = "hello"

    return render(request, 'use/main.html', {'word': word})

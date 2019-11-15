from django.utils.http import is_safe_url, urlunquote
from django.shortcuts import render


def post(request):

    if request.method == "POST":

       data = "post"

    else:
        data = "hello"




    return render(request, 'use/main.html', {'data': data})

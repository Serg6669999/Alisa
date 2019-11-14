from django.shortcuts import render
from .api import main

def post(request):

    if request.method == "POST":
       data = "post"
       print(main())
    else:
        data = "hello"

    return render(request, 'use/main.html', {'data': data})

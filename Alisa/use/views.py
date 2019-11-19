from django.utils.http import is_safe_url, urlunquote
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest, QueryDict
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from .api import main

import requests, json


@csrf_exempt
def post(request):
    if request.method == 'POST':
        body = request.body
        print('body=', body)
        data = json.loads(body)

        session = data['session']
        session_id = session["session_id"]
        message_id = session["message_id"]
        user_id = session["user_id"]

        response = {
            'response': {
                'text': 'Да',
                'end_session': 'false'
            },
            'session': {
                'session_id': session_id,
                'message_id': message_id,
                'user_id': user_id,

            },
            'version': '1.0'
        }
        return JsonResponse(response)
    data_post = Post(title=body_post)
    data_post.save()
    # data_post = Post.objects.all()
    return render(request, 'use/main.html', {'form': data_post})

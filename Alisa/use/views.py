from django.utils.http import is_safe_url, urlunquote
from django.shortcuts import render
from django.http import JsonResponse
from .api import main
import requests


def post(request):

    text = {'text': 'Да'}

    end_session = {'end_session': 'false'}
    session = request.POST.get("session")
    session_id = session["session_id"]
    message_id = session["message_id"]
    user_id = session["user_id"]
    version = {"1.0"}
    response = {'response': text, 'end_session': end_session,
                                      'session': {'session_id':session_id,
                                      'message_id': message_id,
                                      'user_id': user_id,
                                      'version': version,}}
    return JsonResponse(response)


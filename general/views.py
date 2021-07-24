from django.shortcuts import render, HttpResponse, redirect
from general import decode_jwt
from decouple import config
import requests
import hashlib
import base64


# Create your views here.


def home(request):
    context = {}
    try:
        code = request.GET.get('code')
        userData = getTokens(code)
        context['status'] = 1
        context['name'] = userData['name']
        response = render(request, 'index.html', context)
        response.set_cookie(
            'sessiontoken', userData['id_token'], max_age=60*60*24, httponly=True)
        return response
    except:
        token = getSession(request)
        if token is not None:
            userData = decode_jwt.lambda_handler(token, None)
            context['status'] = 1
            context['name'] = userData['name']
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', {'status': 0})


def getTokens(code):
    TOKEN_ENDPOINT = config('TOKEN_ENDPOINT')
    REDIRECT_URI = config('REDIRECT_URI')
    CLIENT_ID = config('CLIENT_ID')
    CLIENT_SECRET = config('CLIENT_SECRET')

    encodedData = base64.b64encode(
        bytes(f"{CLIENT_ID}:{CLIENT_SECRET}", "ISO-8859-1")).decode("ascii")

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encodedData}'
    }
    body = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(TOKEN_ENDPOINT, data=body, headers=headers)
    id_token = response.json()['id_token']

    userData = decode_jwt.lambda_handler(id_token, None)

    if not userData:
        return False

    user = {
        'id_token': id_token,
        'name': userData['name'],
        'email': userData['email'],
    }
    return user


def getSession(request):
    try:
        response = request.COOKIES["sessiontoken"]
        return response
    except:
        return None


def leave(request):
    response = render(request, 'index.html', {'status':0})
    response.delete_cookie('sessiontoken')
    return response


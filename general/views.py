from django.shortcuts import render, HttpResponse, redirect
from general import decode_jwt
from decouple import config
import requests
import hashlib
import base64


# Create your views here.


def home(request):
    try:
        code = request.GET['code']
        userData = getTokens(code)
        response = render(request, 'index.html', {'name': userData['name']})
        response.set_cookie(
            'sessiontoken', userData['id_token'], max_age=60*60*24, httponly=True)
        return response
    except:
        token = getSession(request)
        if token is not None:
            userData = decode_jwt.lambda_handler(token, None)
            return HttpResponse(userData)
        else:
            return HttpResponse('Error 404. Page Not Found!')


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

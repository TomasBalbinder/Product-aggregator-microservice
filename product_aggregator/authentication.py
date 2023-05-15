import requests
from .models import AccessToken


def get_access_token():
    url = "https://python.exercise.applifting.cz/api/v1/auth/"

    headers = {
        "accept": "application/json",
        "Bearer": "token",
    }
    response = requests.post(url, headers=headers)
    json_data = response.json()
    
    if response.status_code == 201:
        access_token = json_data['access_token']
        AccessToken.objects.create(access_token=access_token)
        return access_token
    else:
        last_access_token = AccessToken.objects.last()
        access_token = last_access_token.access_token
        return access_token

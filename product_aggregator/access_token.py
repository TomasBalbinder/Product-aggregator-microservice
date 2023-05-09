import requests
from private import TOKEN

def get_access_token():
    url = "https://python.exercise.applifting.cz/api/v1/auth/"

    headers = {
        "accept": "application/json",
        "Bearer": TOKEN,
    }
    response = requests.post(url, headers=headers)
    json_text = response.json()
    return json_text





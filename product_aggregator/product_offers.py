import requests
from .authentication import get_access_token

def get_product_offer():
    test = "kod id"
    url = f"https://python.exercise.applifting.cz/api/v1/products/{test}/offers"
    headers = {
        "accept": "application/json",
        "Bearer": get_access_token(),
    }
    response = requests.get(url, headers=headers)
    json_data = response.json()
    if response.status_code == 200:
        print(json_data)
        return json_data
    else:
        print("neco se stalo")
        return json_data['detail']

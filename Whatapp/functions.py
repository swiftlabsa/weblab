import requests
import json
from django.http import HttpResponse
from decouple import config
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#sending message to the user

def send_whatsapp_message(phone_number, message):
    headers = {"authorizations" : config("WHATSAPP_TOKEN")}
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(config("WHATSAPP_URL"), headers=headers, json=payload)
    ans = response.json()
    return ans


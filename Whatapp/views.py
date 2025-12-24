from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .functions import send_whatsapp_message
import json


#receiving the message form webhook


@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "GET":
        VERIFY_TOKEN = config("VERIFY_TOKEN")
        mode = request.GET["hub.mode"]
        token = request.GETt["hub.verify_token"]
        challenge = request.GET["hub.challenge"]

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse("error", status=403)
        
    if request.method == "POST":
        data = json.loads(request.body)
        if "object" in data and "entry" in data:
            if data['object'] == "whatsapp_business_account":
                try:
                    for entry in data['entry']:
                        phone_number = entry["changes"][0]["value"]["metadata"]["display_phone_number"]
                        phone_id = entry["changes"][0]["value"]["metadata"]["phone_number_id"]
                        profile_name = entry["changes"][0]["value"]["contacts"][0]["profile"]["name"]
                        whatsapp_id = entry["changes"][0]["value"]["contacts"][0]["wa_id"]
                        from_id = entry["changes"][0]["value"]["messages"][0]["from"]
                        message_id = entry["changes"][0]["value"]["messages"][0]["id"]
                        timestamp = entry["changes"][0]["value"]["messages"][0]["timestamp"]
                        text = entry["changes"][0]["value"]["messages"][0]["text"]["body"]

                        phone_number = "27731422654"
                        message = f"RE: {text} was received"
                        send_whatsapp_message(phone_number, message)
                except:
                    pass
    

    return HttpResponse('success', status=200)